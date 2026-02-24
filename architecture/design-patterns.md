[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 12. Design Patterns in Android

### Singleton Pattern (Problem & Solutions)

> **TL;DR:** Singleton = single global instance. **Avoid** for testability (hard to mock). Kotlin `object` = thread-safe, but use Dependency Injection instead. If needed: private constructor + lazy initialization.

`object` keyword · Thread-safe · Avoid global state · DI > Singleton · Defensive copy

**Problem:** Global mutable state, hard to test, thread safety nightmare.

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ Bad: Exposed mutable list
object UserManager {
    private val users = mutableListOf<User>()
    fun getUsers() = users  // Caller can modify!
}

// ✅ Better: Immutable return
object UserManager {
    private val _users = mutableListOf<User>()
    val users: List<User> get() = _users.toList()
}

// ✅ Best: No global state (Dependency Injection)
class UserRepository(private val api: ApiService) {
    suspend fun getUsers() = api.users()
}
```

</details>

| Pattern | Thread-Safe | Testable | Flexible |
|---|---|---|---|
| `object UserManager` | ✅ (compiler) | ❌ (global) | ❌ (fixed) |
| With DI | ✅ (external) | ✅ (injectable) | ✅ (swappable) |

<details>
<summary>🔩 Under the Hood</summary>

### Kotlin `object` Code Generation

**What you write:**
```kotlin
object UserManager {
    fun getUsers() = listOf()
}
```

**What Kotlin compiler generates:**
```java
public final class UserManager {
    public static final UserManager INSTANCE = new UserManager();

    private UserManager() {}  // Private constructor

    public List getUsers() { return Arrays.asList(); }
}

// Usage: UserManager.INSTANCE.getUsers()
// Or simplified: UserManager.getUsers() (Kotlin handles access)
```

**Thread-safety guarantee:**
- ClassLoader initializes `INSTANCE` once
- JVM ensures singleton (atomic, synchronized)
- No double-check locking needed (JVM handles it)

### Why Singletons Harm Testing

**Testing problem:**
```kotlin
// Production code
object UserManager {
    var users = mutableListOf<User>()
}

// Test 1
UserManager.users = listOf(User(1, "Alice"))
assert(getUserCount() == 1)

// Test 2
UserManager.users = listOf(User(1, "Alice"), User(2, "Bob"))
assert(getUserCount() == 2)
// Problem: Test 2 sees leftover state from Test 1!
// Singleton persists across tests
```

**Solution: Dependency Injection**
```kotlin
class UserManager(private val repo: UserRepository)

// Test can inject FakeRepository
val fakeRepo = FakeRepository()
val manager = UserManager(fakeRepo)
// Each test gets fresh instance
```

### What it reuses & relies on

- **Kotlin compiler** — generates private constructor, static field
- **JVM ClassLoader** — initializes static fields once
- **Memory visibility** — volatile semantics for thread-safe access

### Why this design was chosen

**Pre-Java5:** Singletons needed complex double-check locking (hard to get right).

**Java5+:** ClassLoader initialization thread-safe, so `static final` instances safe.

**Kotlin:** Automated with `object` keyword (less boilerplate than Java).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "object = singleton" | Kotlin compiler generates private constructor + static field. ClassLoader initializes once (thread-safe). |
| "Hard to test" | Singleton persists across tests (global mutable state). Test isolation broken. Mock can't replace instance. |
| "Use DI instead" | Inject dependency into constructor. Tests pass mock. Production passes real impl. Same code path. |
| "Kotlin handles thread safety" | Static field initialized by ClassLoader (synchronized). No manual locking needed. |

### Gotchas at depth

- **Singletons + serialization:** Serializing singleton then deserializing creates new instance (not singleton). Use readResolve() to fix.
- **ClassLoader isolation:** Different ClassLoaders = different singletons (jar files, Android processes). Not truly global.
- **Mocking singletons:** Even with reflection, mocking `object` is awkward. DI is cleaner.
- **Memory leaks:** Singleton holds references forever. If reference is listener/callback, memory leak possible (even after app closes).

</details>

### Observer Pattern (Flows vs. Callbacks)

> **TL;DR:** Callbacks = manual lifecycle, memory leaks if unsubscribe forgotten. **Flows** = automatic scope, composable operators (map, filter), backpressure, cancellation safe. Always use Flows in modern Android.

Callback hell · Flow composability · Automatic cleanup · Backpressure · StateFlow for UI state

**Legacy (Callbacks - DON'T USE):**
<details>
<summary>💻 Code Example</summary>

```kotlin
interface UserListener { fun onUserLoaded(user: User) }
class UserManager {
    private val listeners = mutableListOf<UserListener>()
    fun subscribe(listener: UserListener) = listeners.add(listener)
    fun loadUser() { listeners.forEach { it.onUserLoaded(user) } }
}
// Problems: must manually unsubscribe, memory leaks, no operators
```

</details>

**Modern (Flows - USE THIS):**
<details>
<summary>💻 Code Example</summary>

```kotlin
class UserRepository {
    val users: Flow<List<User>> = flow {
        emit(api.getUsers())
    }
}

// In UI: automatic lifecycle, composable
viewModel.users
    .map { it.size }  // Composable operator
    .catch { emit(0) }  // Error handling
    .collect { size -> updateCount(size) }  // Auto-cancels with scope
```

</details>

| Aspect | Callbacks | Flows |
|---|---|---|
| **Unsubscribe** | Manual (easy to forget) | Automatic (scope) |
| **Operators** | None (manual loops) | map, filter, catch, etc. |
| **Memory leaks** | Common (forgot unsubscribe) | Rare (scope handles) |
| **Backpressure** | No | ✅ Built-in |

<details>
<summary>🔩 Under the Hood</summary>

### Callback vs Flow Memory Leaks

**Callback leak:**
```kotlin
// Activity subscribes to global listener
UserManager.subscribe(object : UserListener {
    override fun onUserLoaded(user: User) {
        updateUI(user)  // This lambda captures 'this' (Activity)
    }
})
// Activity destroyed, but listener still in UserManager.listeners
// Activity held in memory (memory leak!)
// Must call unsubscribe() in onDestroy() (easy to forget)
```

**Flow safety:**
```kotlin
// viewModelScope cancellation
viewModel.users.collect { user ->
    updateUI(user)  // Lambda captures 'this'
}
// ViewModel destroyed → scope cancelled
// collect() cancelled → flow unsubscribed
// Activity freed (no leak!)
```

### Flow Composability (Operator Fusion)

**Callbacks (manual composition):**
```kotlin
UserManager.subscribe(object : UserListener {
    override fun onUserLoaded(user: User) {
        if (user.age > 18) {  // Manual filter
            val name = user.name.uppercase()  // Manual map
            updateUI(name)
        }
    }
})
```

**Flows (declarative):**
```kotlin
userFlow
    .filter { it.age > 18 }
    .map { it.name.uppercase() }
    .collect { updateUI(it) }
```

**Difference:** Flow operators create intermediate flows (function composition). Callbacks require manual loops.

### Backpressure (Flow vs Callbacks)

**Callbacks (no backpressure):**
```kotlin
// Fast emitter, slow consumer
for (i in 1..1_000_000) {
    notifyListeners(i)  // All 1M notifications queued
    // Memory: 1M pending callbacks
}
```

**Flow (backpressure):**
```kotlin
flow {
    for (i in 1..1_000_000) {
        emit(i)  // Suspends if collector can't keep up
    }
}
.collect { slowProcessing(it) }
// Emit blocked until collector ready (no memory buildup)
```

### What it reuses & relies on

- **Coroutine scope** — lifecycle tied to ViewModel/Activity scope
- **Suspend functions** — backpressure via coroutine suspension
- **Flow operators** — compose transformations without nesting

### Why this design was chosen

**Problem (callbacks):**
- Manual memory management (easy to leak)
- No operators (imperative code)
- No backpressure (memory issues at scale)

**Solution (Flow):**
- Scope-tied lifecycle (automatic cleanup)
- Declarative operators (clean code)
- Backpressure (safe at scale)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Callbacks leak memory" | Listeners persisted in global list. No automatic cleanup on Activity destroy. |
| "Flows are safer" | Flows tied to CoroutineScope. Scope cancellation cascades (collect cancelled, listener removed). |
| "Use map/filter" | Flow operators suspend collection. Backpressure prevents buffer explosion. |
| "StateFlow for UI" | StateFlow = hot flow with last value cached. UI always sees current state (even late collectors). |

### Gotchas at depth

- **Multiple listeners (callbacks):** Each listener = separate execution (overhead). Flow = single source (efficient).
- **Unsubscribe in onDestroy():** Common mistake: subscribe in onCreate, forget unsubscribe in onDestroy. Scope handles Flow for you.
- **Cold vs Hot flows:** Flow = cold (new collection = rerun). StateFlow = hot (cached value). Different semantics.
- **Exception in collector:** Collector exception cancels flow. Flow doesn't emit exception unless explicit catch. Understand difference.

</details>

### Factory Pattern

> **TL;DR:** Factory = abstraction for object creation. In Kotlin: often prefer **default parameters** or **DSL (Builder pattern)**. Factory pattern rare unless creating many variants or complex logic needed.

Object creation · Builder DSL · Default parameters · Abstraction layer · Variant handling

**Use case:** Creating objects with complex initialization (many parameters, many variants).

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ Verbose: caller must know all parameters
val client = HttpClient(
    timeout = 30000,
    headers = mapOf("User-Agent" to "MyApp"),
    interceptors = listOf(LoggingInterceptor()),
    retryPolicy = RetryPolicy.Exponential
)

// ✅ Factory with sensible defaults
class HttpClientFactory {
    fun create(timeout: Long = 30000, retryCount: Int = 3): HttpClient =
        HttpClient(
            timeout = timeout,
            headers = defaultHeaders(),
            interceptors = listOf(LoggingInterceptor(), RetryInterceptor(retryCount)),
            retryPolicy = RetryPolicy.Exponential
        )
}
val client = HttpClientFactory().create(timeout = 60000)

// ✅✅ Better: Kotlin DSL (most idiomatic)
fun httpClient(block: HttpClientBuilder.() -> Unit = {}): HttpClient {
    val builder = HttpClientBuilder()
    builder.block()
    return builder.build()
}

// Usage: Clean, readable, Kotlin idiom
val client = httpClient {
    timeout = 60000
    retryCount = 5
}
```

</details>

| Approach | Pros | Cons |
|---|---|---|
| **Direct constructor** | Simple | Caller must know all params |
| **Factory class** | Encapsulates logic | Extra class (boilerplate) |
| **DSL (Builder)** | Readable, Kotlin idiomatic | Slightly more setup |

<details>
<summary>🔩 Under the Hood</summary>

### Factory Pattern Use Cases

**When to use Factory:**
1. Complex initialization logic
2. Multiple variants of same object
3. Conditional object creation based on parameters
4. Deferring instantiation

**Example: Retrofit API client factory**
```kotlin
class ApiClientFactory {
    fun create(debug: Boolean): ApiService {
        val client = OkHttpClient.Builder()
            .apply {
                if (debug) {
                    addInterceptor(HttpLoggingInterceptor())
                }
            }
            .build()

        return Retrofit.Builder()
            .baseUrl("https://api.example.com")
            .client(client)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)
    }
}
```

### Kotlin DSL as Builder Pattern

**What Kotlin DSL does:**
```kotlin
// DSL function (higher-order with receiver)
fun httpClient(block: HttpClientBuilder.() -> Unit): HttpClient {
    val builder = HttpClientBuilder()
    builder.block()  // Invoke lambda with builder as receiver
    return builder.build()
}

// Called as:
httpClient {
    // 'this' = HttpClientBuilder
    timeout = 60000  // this.timeout = 60000
    retryCount = 5
}

// Equivalent to:
httpClient { builder ->
    builder.timeout = 60000
    builder.retryCount = 5
}
```

**Why cleaner:**
- No `builder.` prefix needed (receiver scope)
- Looks like domain-specific language
- Very Kotlin idiomatic

### Factory vs Dependency Injection

**Factory (creates objects, hides complexity):**
```kotlin
val httpClient = HttpClientFactory().create(debug = true)
```

**DI (framework provides objects):**
```kotlin
@Provides
fun provideHttpClient(interceptor: LoggingInterceptor): HttpClient {
    return HttpClient(interceptors = listOf(interceptor))
}

// Hilt/Dagger injects automatically
class MyViewModel(private val client: HttpClient)
```

**Key difference:**
- Factory: Manual, explicit, lightweight
- DI: Automatic, declarative, framework-managed

**Hybrid (common):**
```kotlin
@Provides
fun provideHttpClient(factory: HttpClientFactory): HttpClient {
    return factory.create(debug = BuildConfig.DEBUG)
}
```

### What it reuses & relies on

- **Higher-order functions** (Kotlin) — `block: Lambda.() -> Unit`
- **Function types with receiver** — `T.() -> Unit` syntax
- **Builder pattern** — mutable object, build() returns immutable

### Why this design was chosen

**Problem:** Constructors can't have conditional logic (hard to read). Too many parameters (confusion).

**Solution:** Factory encapsulates construction logic.

**Kotlin improvement:** DSL makes factory cleaner than Java Factory Pattern.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Factory creates objects" | Factory method encapsulates construction. Builder accumulates params, returns immutable. |
| "DSL is prettier than Factory" | DSL = higher-order function with receiver. Lambda gets builder as implicit receiver (this). |
| "Use DSL not Factory class" | DSL = function, less boilerplate. Factory class = if multiple variants or complex logic. |
| "Default params help" | Data class with defaults eliminates need for Factory in simple cases. Only use when logic complex. |

### Gotchas at depth

- **DSL overuse:** DSL is pretty but less obvious to Java/new devs. Factory class can be clearer for complex logic.
- **Builder pattern overhead:** Builder must be mutable (setters). Data class with defaults often simpler.
- **Factory method name:** `create()` vs `build()` vs `make()`. Inconsistent naming confusing (pick one convention).
- **Lazy initialization:** Factory creates eagerly. If initialization expensive, use lazy { } or lazy delegates instead.

</details>

### Repository Pattern

> **TL;DR:** Repository = abstraction layer over data sources (API, DB, cache). Single interface, multiple implementations (real, fake). Benefits: testable, swappable logic, centralized caching/sync strategy.

Data abstraction · Cache-through pattern · Sync coordination · Testability · Single source of truth (Room)

<details>
<summary>💻 Code Example</summary>

```kotlin
// Interface: what data the app needs
interface UserRepository {
    suspend fun getUser(id: Int): User
    suspend fun saveUser(user: User)
}

// Implementation: how to get it (cache, DB, API)
class UserRepositoryImpl(
    private val api: UserApi,
    private val db: UserDao,
    private val cache: UserCache
) : UserRepository {
    override suspend fun getUser(id: Int): User {
        cache.get(id)?.let { return it }  // 1. Try cache
        val dbUser = db.getUser(id)
        if (dbUser != null) {
            cache.put(id, dbUser)
            return dbUser  // 2. Try DB
        }
        val apiUser = api.getUser(id)  // 3. Try API
        db.insertUser(apiUser)  // Persist to DB
        cache.put(id, apiUser)  // Update cache
        return apiUser
    }
}

// Fake for testing (no API calls, no DB access)
class FakeUserRepository : UserRepository {
    override suspend fun getUser(id: Int) = User(id, "Test")
}
```

</details>

**Strategy:** Cache-through (check cache → DB → API). Caching transparent to caller.

<details>
<summary>🔩 Under the Hood</summary>

### Repository as Anti-Corruption Layer

**Purpose: Translate between domain and data layer.**

```
UI Layer:
  ↓ expects: User(id, name, email)
  ↓
Repository (anti-corruption):
  ↓ translates
  ↓
Data Layer:
  ├── API returns: { "userId": ..., "fullName": ... } (different field names)
  ├── DB stores: users table with schema
  └── Cache: custom object

Repository maps all to domain User object
```

### Cache-Through vs Cache-Aside

**Cache-Through (automatic caching):**
```kotlin
override suspend fun getUser(id: Int): User {
    cache.get(id)?.let { return it }
    val user = db.getUser(id) ?: api.getUser(id)
    cache.put(id, user)  // Auto-cache
    return user
}
// Caller: val user = repo.getUser(id)
// Caching transparent
```

**Cache-Aside (manual caching):**
```kotlin
override suspend fun getUser(id: Int): User {
    // Caller decides to cache: val cached = cache.get(id)
    return api.getUser(id)
}
// Caller handles caching (boilerplate)
```

**Better:** Cache-Through (repository hides it).

### Testability via Repository

**Without Repository (tightly coupled):**
```kotlin
class UserViewModel : ViewModel() {
    fun loadUser(id: Int) {
        viewModelScope.launch {
            val user = UserApi.INSTANCE.getUser(id)  // Hard-coded API singleton
            state.value = user
        }
    }
}

// Testing: impossible to inject fake API
// API always called (slow, unreliable in tests)
```

**With Repository (testable):**
```kotlin
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    fun loadUser(id: Int) {
        viewModelScope.launch {
            val user = repo.getUser(id)  // Injected
            state.value = user
        }
    }
}

// Testing: inject FakeUserRepository
val fakeRepo = FakeUserRepository()
val viewModel = UserViewModel(fakeRepo)
// No API calls, deterministic
```

### What it reuses & relies on

- **Interface/Abstract class** — enables multiple implementations
- **Dependency injection** — inject repository into ViewModel
- **Room database** — common as local cache (SSOT)
- **OkHttp interceptors** — for logging/retry at API layer

### Why this design was chosen

**Problem:** Logic scattered (API calls in ViewModel, DB logic in multiple places). Hard to test, hard to change.

**Solution:** Repository centralizes data access.

**Benefits:**
- Single place to add caching/retry
- Easy to mock (inject fake)
- Swappable (real vs test vs offline)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Repository abstracts data sources" | Interface defines contract. Implementations hide API/DB/cache details. |
| "Use Repository for testing" | Inject FakeRepository in tests. ViewModel doesn't know it's fake (interface same). |
| "Cache-through pattern" | Repository checks cache → DB → API sequentially. Caller doesn't know (transparent). |
| "Room as SSOT" | API updates Room → UI observes Room. Single source of truth prevents stale UI. |

### Gotchas at depth

- **Over-abstraction:** Every DAO doesn't need Repository. Too many layers = overhead. Repository for app-level data access only.
- **Cache invalidation:** If cache doesn't update when API changes, stale data served. Must coordinate cache expiration.
- **Circular dependency:** Repository depends on DB, API, cache. Be careful of bidirectional dependencies (circular).
- **Error handling:** Repository must decide: retry at API? Fallback to DB? Return error? Centralize strategy here (not in ViewModel).

</details>

