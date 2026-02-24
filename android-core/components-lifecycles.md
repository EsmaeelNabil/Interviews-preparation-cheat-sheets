[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 7. Android Components & Lifecycles

### Services vs WorkManager

> **TL;DR:** Foreground Service = user-visible (music, GPS, call). WorkManager = background tasks with system guarantees (sync, upload). Rule: User sees it now → FGS; everything else → WorkManager.

`FGS` user-visible · `WorkManager` system-managed · `Doze-safe` · `Guaranteed execution` · `API 35+ 6h timeout`

| Task | Foreground Service | WorkManager |
|---|---|---|
| **Music playback** | ✅ Required | ❌ |
| **GPS navigation** | ✅ Required | ❌ |
| **Data sync** | ⚠️ 6h timeout (API 35+) | ✅ Preferred |
| **File upload** | ❌ | ✅ CoroutineWorker |
| **Periodic task** | ❌ | ✅ PeriodicWorkRequest |

<details>
<summary>💻 Code Example</summary>

```kotlin
// FGS: user sees notification, process priority boosted
startForegroundService(Intent(this, LocationService::class.java))

// WorkManager: system-guaranteed background task
WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "sync", ExistingPeriodicWorkPolicy.KEEP,
    PeriodicWorkRequestBuilder<SyncWorker>(15, TimeUnit.MINUTES).build()
)
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### FGS notification & process priority

**What FGS does:**
```kotlin
// Must call before 5 seconds (or crash)
startForeground(NOTIFICATION_ID, notification)

// System boost: process priority = FOREGROUND
// OOM killer won't kill app
// Result: guaranteed execution while visible notification shown
```

**Notification channel requirement:**
```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
    val channel = NotificationChannel(
        CHANNEL_ID, "Foreground", NotificationManager.IMPORTANCE_LOW
    )
    getSystemService(NotificationManager::class.java)?.createNotificationChannel(channel)
}
```

**API 35+ (2024) changes:**
- 6-hour timeout for dataSync/mediaProcessing types
- New onTimeout() callback (graceful shutdown required)
- 2-minute timeout for other types

### WorkManager: Scheduler under the hood

**Job scheduling pipeline:**
```
WorkManager request
  ↓ (API 31+) Uses JobScheduler
  ↓ If JobScheduler unavailable: falls back to AlarmManager
  ↓ WorkSpec stored in Room database (persisted across reboots)

On device boot/charge idle:
  ↓ System calls JobScheduler with WorkSpec
  ↓ WorkManager wakes worker, executes
  ↓ Retries with exponential backoff if failed
```

**Doze mode compatibility:**
- WorkManager uses JobScheduler (exempted from Doze restrictions)
- FGS not affected by Doze (user-visible = always runs)

### What each reuses & relies on

**FGS:**
- Notification framework (requires valid channel on API 26+)
- Process priority system (FOREGROUND_APP prevents OOM kill)
- System foreground service whitelist (by type)

**WorkManager:**
- JobScheduler (API 31+) or AlarmManager fallback
- Room database (work persistence)
- Work policy framework (retry, constraints)

### Why this design was chosen

**FGS:**
- User expects immediate action (music, navigation)
- Requires persistent notification (user-initiated, visible)
- System guarantees via priority (foreground process won't be killed)

**WorkManager:**
- Background tasks don't need immediate execution
- System can batch/delay for optimization (battery saving)
- Automatic retry/persistence handles device reboots
- One Work API handles JobScheduler + AlarmManager compatibility

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "FGS keeps app alive" | FGS sets process priority to FOREGROUND; OOM killer won't kill foreground processes (only background after foreground) |
| "WorkManager handles reboots" | Work specs stored in Room DB; JobScheduler re-schedules after reboot from persisted specs |
| "6-hour timeout on API 35+" | FGS.onTimeout() callback gives 2-minute grace period before system kills service (enforce cleanup) |
| "WorkManager uses JobScheduler" | On API 31+, WorkManager maps work to JobScheduler. Pre-API 31, fallback to AlarmManager. |

### Gotchas at depth

- **FGS without notification:** If startForeground() not called in 5 seconds, crash (ANR). Must be immediate in onCreate().
- **WorkManager + Doze:** Workers still run in Doze (system exempts JobScheduler). But UI updates may not show if app backgrounded (use notification for feedback).
- **Periodic work minimum:** PeriodicWorkRequest minimum interval = 15 minutes (system enforces; shorter intervals silently become 15m).
- **Backpressure:** If WorkManager queue overflowed (100+ pending works), system may drop tasks. Monitor via WorkInfo.state = ENQUEUED.

</details>

### Foreground Service Restrictions (2026)

- **API 34+:** Must declare `foregroundServiceType` + `FOREGROUND_SERVICE_*` permission
- **API 35+:** `dataSync`/`mediaProcessing` = **6-hour timeout**. New `onTimeout()` callback.
- **API 36+:** Job quotas on background jobs from FGS. `setImportantWhileForeground()` = no-op.
- **Types:** camera, connectedDevice, dataSync, health, location, mediaPlayback, mediaProcessing, mediaProjection, microphone, phoneCall, remoteMessaging, shortService, specialUse, systemExempted

### Lifecycle Saving & Process Death

> **TL;DR:** SavedStateHandle (ViewModel-integrated) survives process death. onSaveInstanceState() survives config change only. Use SavedStateHandle for state, onDestroy() for cleanup only.

`SavedStateHandle` process-death-safe · `onStop()` always called · `onDestroy()` not guaranteed · `Config change` vs `Process death` · `Binder transaction limit`

<details>
<summary>💻 Code Example</summary>

```kotlin
// SavedStateHandle: survives process death, config change
class MyViewModel(private val savedState: SavedStateHandle) : ViewModel() {
    var userId: Int
        get() = savedState["userId"] ?: 0
        set(value) { savedState["userId"] = value }
}

// onSaveInstanceState: survives config change only
override fun onSaveInstanceState(bundle: Bundle) {
    super.onSaveInstanceState(bundle)
    bundle.putInt("temp_state", tempValue)  // Lost on process death
}
```

</details>

| Trigger | onSaveInstanceState | SavedStateHandle | onDestroy |
|---|---|---|---|
| **Config change** | ✅ Restored | ✅ Restored | ❌ Not called |
| **Process death** | ❌ Lost | ✅ Restored | ❌ Not called |
| **Back press** | ❌ Lost | ❌ Lost | ✅ Called |

<details>
<summary>🔩 Under the Hood</summary>

### Binder transaction & Bundle serialization

**Config change flow (memory preserved):**
```
Activity destroyed (rotation)
  ↓ onSaveInstanceState() called
  ↓ Bundle serialized (via Binder IPC)
  ↓ Activity created (rotation complete)
  ↓ Bundle deserialized
  ↓ onCreate(bundle) receives it
```

**Bundle serialization:**
```kotlin
// Only Parcelable/Serializable objects fit through Binder
// Limit: ~1 MB per transaction (Binder limit)

onSaveInstanceState { bundle ->
    bundle.putSerializable("user", user)  // Serializes via Java serialization
}

// Large objects risk TransactionTooLargeException
// Mitigation: use SavedStateHandle (stored in app process, not Binder)
```

**Process death flow (disk-persisted):**
```
Activity running
  ↓ SavedStateHandle stores values in app process memory
  ↓ System kills process (memory pressure)
  ↓ User returns to app
  ↓ SavedStateHandle persisted (Room DB or SharedPrefs)
  ↓ ViewModel created, SavedStateHandle restored
  ↓ App resumes where it left off
```

### SavedStateHandle under the hood

**Storage mechanism:**
```kotlin
// SavedStateHandle stores in ViewModel SavedState Registry
// Persisted via SavedState framework (backed by Room or SharedPrefs)
// Survives process death across process boundary (not in Binder transaction)

class SavedStateHandle(initialState: Map<String, Any?>) : MutableMap<String, Any?> {
    private val _state = mutableMapOf<String, Any?>()  // In-process, not Binder
}
```

**Restoration order:**
```
1. SavedStateHandle loaded from disk (if process death)
2. ViewModel factory receives SavedStateHandle
3. ViewModel.__init__() can access restored values
4. Activity.onCreate() called (AFTER ViewModel ready)
5. Activity observes ViewModel (state already available)
```

### What each reuses & relies on

**onSaveInstanceState:**
- Binder transport (IPC mechanism)
- Parcelable/Serializable (object encoding)
- Activity/Fragment lifecycle framework

**SavedStateHandle:**
- ViewModel factory framework (Hilt/manual DI)
- SavedState library (androidx.savedstate)
- App process memory + disk persistence layer

### Lifecycle stage guarantees

**onStop() — ALWAYS called:**
```kotlin
// Config change: onPause → onStop → onCreate
// Process death: onPause → onStop (then killed immediately)
// Back press: onPause → onStop → onDestroy

// Rule: Save transient state in onStop()
override fun onStop() {
    super.onStop()
    savedInstanceState?.putInt("scrollPos", scrollPos)  // Safe here
}
```

**onDestroy() — NOT guaranteed:**
```kotlin
// Config change: onDestroy called (not process death)
// Back press: onDestroy called
// Process death: onDestroy NOT called (process killed immediately)

// Rule: Only do cleanup (close DB, unsubscribe) here
override fun onDestroy() {
    super.onDestroy()
    db.close()  // OK: cleanup, not state save
}
```

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "SavedStateHandle survives process death" | Values stored in app process memory (not in Binder transaction). Persisted to disk via SavedState registry. |
| "onSaveInstanceState for config change" | Bundle serialized via Binder (1MB limit). Deserialized in onCreate() after rotation. |
| "onStop() always called" | onStop() called before both config change AND process death. Safe place to save (onDestroy() may not be called). |
| "SavedStateHandle restored before onCreate()" | ViewModel created with SavedStateHandle before Activity onCreate(). Activity gets fully initialized ViewModel. |

### Gotchas at depth

- **TransactionTooLargeException:** If Bundle >1 MB, crashes. Use SavedStateHandle (no Binder limit) for large objects.
- **SavedStateHandle key collisions:** Multiple ViewModels share same SavedStateHandle by key. Use unique keys or namespaced prefixes.
- **Process death != back press:** Back press calls onDestroy(); process death skips it. Don't rely on onDestroy() for state persistence.
- **ViewModel recreation on process death:** New ViewModel instance created, but SavedStateHandle populated from saved state. __init__ and observers see restored values.

</details>

### Navigation Compose — Type-Safe

<details>
<summary>💻 Code Example</summary>

```kotlin
@Serializable data object Home
@Serializable data class Profile(val userId: String)

NavHost(navController, startDestination = Home) {
    composable<Home> { HomeScreen(onNav = { navController.navigate(Profile("123")) }) }
    composable<Profile> { entry -> ProfileScreen(entry.toRoute<Profile>().userId) }
}
```

</details>

No string routes. Custom types via `typeMap`. Nested graphs via `navigation<Route>()`.

---

