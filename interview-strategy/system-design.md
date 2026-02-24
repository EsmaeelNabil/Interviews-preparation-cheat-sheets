[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 10. System & Feature Design (For Bolt)

### The 4-Step Framework

1. **Clarify scope** — "Core use case? Scale? Offline?"
2. **High-level arch** — UI → ViewModel → Repository → (Remote + Local)
3. **Deep dive critical path** — sync, pagination, or caching
4. **Trade-offs** — "Chose X over Y because..."

### Offline-First Architecture

> **TL;DR:** Room is Single Source of Truth (SSOT). Network updates Room; UI always observes Room. Enables offline-first: app works offline, syncs when online.

`Room` SSOT · `Network → Room → UI` · `Flow observes DB` · `Invalidation tracking` · `Automatic sync`

<details>
<summary>💻 Code Example</summary>

```kotlin
// Flow: Network syncs to Room, UI observes Room
val users: Flow<List<User>> = userDao.getAllUsers()  // Always has data, even offline

// On refresh:
viewModelScope.launch {
    try {
        val fresh = api.getUsers()  // May fail offline
        userDao.insertAll(fresh)     // Update Room (notifies UI)
    } catch (e: Exception) {
        // UI still shows stale Room data (works offline!)
    }
}
```

</details>

| Pattern | Purpose | When |
|---|---|---|
| **Offline-first (Room SSOT)** | Always have data | Apps must work offline |
| **Sync via timestamps** | Conflict resolution | Multi-device editing |
| **Pagination 3 + RemoteMediator** | Memory-efficient lists | Large datasets |
| **TTL + Caching** | Reduce API calls | Stable data (profiles, catalogs) |

<details>
<summary>🔩 Under the Hood</summary>

### Room invalidation tracker (automatic Flow updates)

**What happens:**
```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAllUsers(): Flow<List<User>>  // Returns Flow, not List
}

// When Room table modified:
userDao.insertAll(newUsers)
// Room notifies ALL Flow collectors automatically!
// UI re-collects, recomposes with fresh data
```

**Invalidation mechanism:**
```
Room query = SELECT * FROM users
  ↓
Room tracks: "This query depends on 'users' table"
  ↓
Insert/Update/Delete on 'users' table
  ↓
Room notifies all Flow collectors of that query
  ↓
Flow emits new list, UI updates
```

**Why it matters:**
- No manual refresh() calls needed
- UI always in sync with database state
- Single source of truth (network can't get ahead)

### Sync & conflict resolution (LastWrite-Wins)

**Pattern:**
```kotlin
@Entity
data class UserEntity(
    @PrimaryKey val id: Int,
    val name: String,
    @ColumnInfo(name = "last_modified") val lastModified: Long  // Server timestamp
)

// On sync conflict:
val local = userDao.getUser(1)      // lastModified = 1000
val remote = api.getUser(1)         // lastModified = 2000

if (remote.lastModified > local.lastModified) {
    userDao.insert(remote)  // Keep remote (newer)
} else {
    // Keep local (already newer)
}
```

**Why server time matters:**
- User can change device clock → app-level timestamps unreliable
- Server timestamp is source of truth
- Two devices can't conflict if using same server clock

### Paging 3 + RemoteMediator protocol

**LoadState machine:**
```
Initial
  ↓ Load first page
LOADING
  ↓ Page arrived or error
SUCCESS / ERROR
  ↓ User scrolls near end
LOADING (next page)
  ↓ Repeat...
```

**Key-based vs offset pagination:**
```kotlin
// ❌ Offset pagination breaks if data inserted:
// Page 1: items 0-9
// Page 2: items 10-19
// [Meanwhile, new item inserted at position 0]
// Page 2 now: items 11-20 (skipped items 10!)

// ✅ Key-based pagination (cursor):
// Page 1: items where id > 0 and id <= 10
// Page 2: items where id > 10 and id <= 20
// [New item inserted, doesn't affect page boundaries]
```

### Caching with TTL

**Pattern:**
```kotlin
@Entity
data class UserEntity(
    @PrimaryKey val id: Int,
    val name: String,
    @ColumnInfo(name = "last_fetched") val lastFetched: Long
)

// Invalidation check:
val TTL_1_HOUR = 60 * 60 * 1000L
val cached = userDao.getUser(id)
val age = System.currentTimeMillis() - cached.lastFetched

if (age < TTL_1_HOUR) {
    return cached  // Still fresh
} else {
    val fresh = api.getUser(id)
    userDao.insert(fresh.copy(lastFetched = currentTimeMillis()))
    return fresh
}
```

### What it reuses & relies on

- **Room DAO Flow support** — observable queries
- **WorkManager** — reliable background sync
- **Paging 3 library** — RemoteMediator protocol
- **SQLite transactions** — all-or-nothing updates

### Why this design was chosen

**Offline-first:** Network is unreliable. If UI depends on it, app breaks offline. Room SSOT = always functional.

**Server-based timestamps:** Device clocks untrustworthy. Conflicts resolved at sync time using server truth.

**Paging 3 with Room:** Memory efficient. RemoteMediator fetches pages, stores in Room, PagingSource reads from Room. UI sees paginated data with status.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Room is offline cache" | Room flow queries auto-notify on table changes (invalidation tracking). UI observes Room, not network. |
| "Sync uses timestamps" | Server timestamp is truth. On conflict, compare lastModified: higher timestamp wins (Last-Write-Wins). |
| "Pagination loads pages" | RemoteMediator receives page number, fetches from API, stores in Room. PagingSource reads from Room (memory-bounded). |
| "TTL prevents stale data" | Add lastFetched timestamp. On read, check age. If > TTL, fetch fresh from API. |

### Gotchas at depth

- **Room invalidation is query-specific:** If two queries use same table but different filters, both notified (can be wasteful). Consider `@SkipQueryVerification` if intentional.
- **Flow backpressure:** If Room writes faster than UI collects, backpressure can cause delays. Use `conflate()` for latest-only pattern.
- **Timestamp precision:** Server and device clocks may have millisecond drift. Consider server sends "current time" in response, use that as truth.
- **Pagination cursor corruption:** If RemoteMediator loses cursor (app killed), may resume from wrong position. Store cursor in Room or preferences.

</details>

### Database Schema Design (Room)

> **TL;DR:** Design entities with indices on query columns. Use foreign keys with CASCADE for referential integrity. Add timestamps for caching/sync. Test migrations early.

`Entity design` · `Indices` · `Foreign keys + CASCADE` · `Migrations` · `SQLite WAL mode`

<details>
<summary>💻 Code Example</summary>

```kotlin
@Entity(tableName = "users", indices = [Index("email", unique = true)])
data class UserEntity(
    @PrimaryKey val id: Int,
    val name: String,
    val email: String,  // Indexed for fast lookup
    @ColumnInfo(name = "last_fetched") val lastFetched: Long,  // Cache TTL
    @ColumnInfo(name = "last_modified") val lastModified: Long  // Sync timestamps
)
```

</details>

**Query performance:**
<details>
<summary>💻 Code Example</summary>

```kotlin
@Query("SELECT * FROM users WHERE email = :email LIMIT 1")
suspend fun getUserByEmail(email: String): UserEntity?  // Fast with index

@Query("SELECT * FROM users WHERE last_fetched < :threshold")
suspend fun getStaleUsers(threshold: Long): List<UserEntity>  // Index helps here too
```

</details>

| Concern | Pattern | When |
|---|---|---|
| **Fast lookups** | Add Index on query columns | email, userId, timestamp queries |
| **Referential integrity** | ForeignKey with CASCADE | Delete user → auto-delete user's posts |
| **Unique constraints** | `unique = true` in Index | email (can't duplicate) |
| **Writes performance** | Minimize indices | Too many indices = slow inserts |

<details>
<summary>🔩 Under the Hood</summary>

### SQLite internals: B-tree indexing

**Table storage (B-tree):**
```
SELECT * FROM users WHERE email = 'alice@ex.com'

Without index:
  - Sequential scan all rows
  - O(n) time

With index on email:
  - B-tree lookup by email
  - O(log n) time
  - Index stores (email → rowid) pairs, sorted
```

**Index overhead:**
```
CREATE INDEX idx_users_email ON users(email)

// Creates separate B-tree for email values
// Every INSERT/UPDATE/DELETE must update both:
// 1. Main table B-tree
// 2. Index B-tree
// Trade: Fast reads (+), slow writes (-)
```

### Foreign keys & CASCADE delete

**What CASCADE does:**
```kotlin
@Entity(
    tableName = "posts",
    foreignKeys = [
        ForeignKey(
            entity = UserEntity::class,
            parentColumns = ["id"],
            childColumns = ["userId"],
            onDelete = ForeignKey.CASCADE  // Key part
        )
    ]
)
data class PostEntity(val id: Int, val userId: Int, val title: String)

// User deletion:
userDao.delete(user)  // userId = 1

// SQLite executes:
DELETE FROM posts WHERE userId = 1  // Automatic!
DELETE FROM users WHERE id = 1
```

**Without CASCADE (dangling refs):**
```
User deleted but posts remain → orphaned posts
Later queries might crash (FK constraint violation)
Must manually delete posts first (error-prone)
```

### Room migrations (schema changes)

**Problem:** App version 1.0 has `users(id, name)`. Version 2.0 adds `email` column.

```kotlin
// Version 1
@Entity
data class UserEntity(val id: Int, val name: String)

// Version 2 - add email
@Entity
data class UserEntity(val id: Int, val name: String, val email: String)

// Migration (version 1 → 2):
val migration_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL("ALTER TABLE users ADD COLUMN email TEXT DEFAULT ''")
    }
}

// Builder:
Room.databaseBuilder(context, MyDatabase::class.java, "app.db")
    .addMigrations(migration_1_2)
    .build()
```

**Without migration:** onUpgrade() crashes (schema mismatch).

### SQLite WAL mode (Write-Ahead Logging)

**Default mode (Rollback journal):**
```
Write operation:
  1. Lock database
  2. Write changes to temp file
  3. Atomic rename temp → database
  4. Unlock
  Result: Only one writer at a time (sequential)
```

**WAL mode (faster):**
```
Write operation:
  1. Write to WAL (write-ahead log) file
  2. Checkpoint: merge WAL into main DB periodically
  Result: Readers can read main DB while writers write to WAL (concurrent!)

Room enables by default on API 16+
```

**Performance impact:**
- Multiple readers while one writer: faster overall
- Slightly larger disk (WAL file overhead)
- Faster commit (WAL is append-only)

### What it reuses & relies on

- **SQLite query planner** — chooses index if stats say it's faster
- **B-tree algorithms** — underlying data structure for indices + tables
- **ACID transactions** — Room.runInTransaction() ensures all-or-nothing
- **Android SQLiteOpenHelper** — SQLite wrapper

### Why this design was chosen

**Indices:** Without them, every query scans all rows (O(n)). With indices, lookups are O(log n). Trade space (index storage) for speed.

**Foreign keys + CASCADE:** Prevents orphaned data. Enforced at database level (can't violate FK constraints).

**Migrations:** Graceful schema evolution. Existing users can upgrade without data loss.

**WAL mode:** Concurrent reads while writing. Important for apps that read/write frequently.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Add index on email for fast lookup" | Index creates B-tree of (email → rowid). Lookup is tree traversal O(log n) instead of full scan O(n). |
| "CASCADE deletes posts when user deleted" | SQLite triggers automatic DELETE on posts table when parent user deleted. FK constraint enforced. |
| "Migrations let you add columns" | Room generates migration, runs ALTER TABLE. Without it, old schema mismatches new code (crash). |
| "WAL mode is faster" | Writes go to WAL file (append-only, fast). Checkpoint merges WAL into main DB periodically. Readers read main DB (no lock). |

### Gotchas at depth

- **Index bloat:** Too many indices = slow writes, large disk. Profile with EXPLAIN QUERY PLAN to see what indices actually used.
- **Migration mistakes:** If migration SQL has error, app can't upgrade. Test migrations on real database (not in-memory) before release.
- **Foreign key disabled by default (older Android):** Must call `foreignKeys = true` in Room.databaseBuilder. Otherwise FK constraints ignored.
- **WAL checkpoint pause:** Periodic checkpoints can cause brief read delays (background thread merging WAL). Usually <10ms, but noticeable in tight loops.

</details>

---

