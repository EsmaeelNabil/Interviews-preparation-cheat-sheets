[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 15. Debugging & Common Bugs

### Most Common Bugs (& Detection)

> **TL;DR:** Top bugs: race conditions (concurrent state updates), NPE (unmounted Composables), memory leaks (GlobalScope), jank (GC on main), stale cache (not invalidated), deadlocks (transaction waits). Each has a detection signal—use logcat, LeakCanary, Perfetto, or manual testing to pinpoint.

Race conditions · NPE in UI · Memory leaks · Jank · Cache staleness · Deadlocks

| Bug | Symptom | Root Cause | Fix | Detection |
|---|---|---|---|---|
| **Race in state** | Inconsistent values, overwrites | Two coroutines update `_state.value` simultaneously | `StateFlow.update { }` (atomic) or `Mutex` | Logs show mismatched thread IDs |
| **NPE in UI** | Crash on recomposition | Composable accessed after parent unmounts | `?.let` or optional types (no force unwrap!) | Stack trace shows line, add null-safety checks |
| **Memory leak** | App memory grows, slow | `GlobalScope.launch` outlives Activity | Use `viewModelScope`, `lifecycleScope` | LeakCanary shows Activity retained after back |
| **Jank (15fps)** | Frame drops, scroll stutters | Allocating objects in draw callback | Pre-allocate, reuse, avoid `new` in recompose | Perfetto trace shows GC pauses every frame |
| **Stale cache** | User sees old data after edit | Cache not invalidated on update | Clear cache after POST/PUT, use timestamps | Manual test: edit, navigate, verify fresh |
| **Deadlock** | App hangs indefinitely | Transaction A waits B; B waits A | Keep transactions short, avoid nested | `adb logcat` shows "deadlock detected" |

<details>
<summary>🔩 Under the Hood</summary>

### Race Condition in State (Concurrency Bug)

**What happens:**
```kotlin
// ViewModel state
private val _state = MutableStateFlow(0)

// Two coroutines racing:
viewModelScope.launch {
    _state.value = 1  // Coroutine A sets to 1
}

viewModelScope.launch {
    _state.value = 2  // Coroutine B sets to 2 (overwrites A)
}

// If B executes after A starts but before A finishes:
// Result: unpredictable (1 or 2, or intermediate)
```

**Why it's problematic:**
```
Thread A: read value (0) → compute (0+1) → write back (1)
Thread B: read value (0) → compute (0+2) → write back (2)
// Both read before either writes → final value is 2, not 3
// Lost update
```

**Solution: Atomic update**
```kotlin
// ✅ GOOD: Update is atomic (no interleaving)
_state.update { it + 1 }  // Reads current, applies function, writes atomically

// ✅ Also good: Mutex for larger critical section
mutex.withLock {
    val current = _state.value
    val updated = current + 1
    _state.value = updated  // Entire block atomic
}
```

### NPE in Composables (Lifecycle Bug)

**When it happens:**
```kotlin
@Composable
fun UserCard(userId: Int) {
    val user = remember { mutableStateOf<User?>(null) }

    LaunchedEffect(userId) {
        user.value = repo.getUser(userId)  // Async load
    }

    Text(user.value!!.name)  // ❌ NPE if parent unmounts before load completes
}
```

**Why:**
- Async load starts
- Parent unmounts before result arrives
- Composable still tries to access `user.value!!`
- user.value is still null → NPE

**Fix: Null-safe**
```kotlin
Text(user.value?.name ?: "Unknown")  // Safe
// Or optional
user.value?.let { Text(it.name) }  // Safe
```

### Memory Leak (Lifecycle Escape)

**The leak:**
```kotlin
// ❌ BAD: GlobalScope outlives Activity
viewModel.loadData() {
    GlobalScope.launch {  // Lives forever
        val data = api.fetch()
        updateUI(data)  // Reference to Activity this captured
    }
}
// Activity destroyed, but GlobalScope.launch still running
// Activity held in memory → leak
```

**Detection:**
```
LeakCanary logcat: "LeakCanary: FOUND LEAK [Activity] retained 123KB"
→ Shows Activity retained after back press
→ Manual: adb logcat | grep "FATAL" → stack trace shows Activity reference
```

**Fix: Scoped**
```kotlin
viewModel.loadData() {
    viewModelScope.launch {  // Cancelled when ViewModel destroyed
        val data = api.fetch()
        updateUI(data)  // Safe: ViewModel scope ensures cleanup
    }
}
```

### Jank (Garbage Collection on Main)

**The problem:**
```kotlin
// ❌ BAD: Allocates new list every frame
@Composable
fun ItemList(items: List<Item>) {
    val filtered = items.filter { it.selected }  // NEW list every recomposition
    LazyColumn {
        items(filtered) { ItemRow(it) }  // Layout pass → recomposition → GC
    }
}
// Result: GC pauses every frame → dropped frames → 15fps jank
```

**Detection: Perfetto trace**
```
Perfetto shows:
- Frame starts at T=0ms
- ItemList recomposes (draws list)
- GC pauses (memory cleanup)
- Frame ends at T=35ms (should be <16ms for 60fps)
→ Dropped frame
```

**Fix: Cache with remember**
```kotlin
@Composable
fun ItemList(items: List<Item>) {
    val filtered = remember(items) { items.filter { it.selected } }
    // Reuses same list if items unchanged
}
```

### What it reuses & relies on

- **JVM threading** — concurrent access, mutex
- **Kotlin coroutine scope** — lifecycle cancellation
- **Android lifecycle** — when Activities destroyed
- **GC (Garbage Collector)** — memory cleanup pauses

### Why these bugs are common

**Race conditions:** Coroutines make concurrency easy (good), but race conditions subtle (bad)
**NPE in UI:** Async loading + lifecycle mismatch = classic Android pattern gone wrong
**Memory leaks:** GlobalScope convenience (bad practice) still popular
**Jank:** Allocating in hot paths (scroll, recompose) forgotten by new devs
**Stale cache:** Easy to cache, hard to remember to invalidate
**Deadlocks:** Long transactions + locks = deadlock waiting to happen

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Race conditions make state wrong" | Lost updates occur when reads/writes interleave. Atomic operations (update) prevent. |
| "NPE crashes on recomposition" | Async result arrives after Composable unmounts. Safe navigation (`?.`) or null coalescing (`?:`) required. |
| "GlobalScope leaks memory" | GlobalScope persists beyond Activity lifetime. Scope cancellation doesn't apply. Use viewModelScope. |
| "Jank = GC on Main" | Allocation in hot paths triggers GC. GC pauses main thread (~5ms per 100MB). Manifests as frame drops. |
| "Cache invalidation hard" | Forgetting to clear = stale data. Add cache clear after mutations (POST/PUT). Or use TTL + timestamps. |
| "Deadlocks from nested transactions" | Transaction A holds lock, waits for B. B waits for A. Neither releases. System hangs. Keep transactions short. |

### Gotchas at depth

- **Atomic doesn't mean instant:** `update { }` is atomic from caller's perspective, but internally acquires lock briefly.
- **LeakCanary overhead:** Adds memory profiling (~5-10% overhead). Run in debug builds only.
- **Perfetto slowdown:** Tracing adds overhead. Don't leave on in production.
- **Race condition timing:** Flaky—only manifests under load or specific timing. Hard to reproduce. Use ThreadSanitizer (debugging tool).

</details>

### Debugging Tools & Techniques

> **TL;DR:** Logcat for finding errors (grep "FATAL"), Android Studio debugger for pausing/inspecting, LeakCanary for memory leaks (auto-detects), Perfetto for performance (frame timing), Chucker for network (in-app HTTP inspector), ThreadLooper for thread checking.

Logcat · Breakpoints · LeakCanary · Perfetto · Chucker · Thread safety checks

**Tool Selection Matrix:**

| Issue | Tool | Command |
|---|---|---|
| **Crash logs** | Logcat | `adb logcat \| grep "FATAL"` |
| **Specific tag** | Logcat filter | `adb logcat "MyTag:I" "*:S"` |
| **Pausing & inspecting** | Studio Debugger | Set breakpoint, watch variables |
| **Memory leak** | LeakCanary | Auto-detects in logcat |
| **Frame drops** | Perfetto | `adb shell perfetto ...` |
| **Network calls** | Chucker | In-app HTTP inspector |
| **Main thread check** | ThreadLooper | `Looper.myLooper() == Main` |

**1. Logcat (Finding errors fast):**

<details>
<summary>💻 Code Example</summary>

```bash
# Filter by tag
adb logcat | grep "MYTAG"

# Errors only
adb logcat *:E

# Specific level: ActivityManager (info only)
adb logcat "ActivityManager:I" "*:S"

# Search for common crash patterns
adb logcat | grep -E "Exception|FATAL|crash"
```

</details>

**2. Android Studio Debugger (Inspect state):**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Breakpoint: Click line number → pauses execution
// Conditional breakpoint: Right-click → condition
// Condition: user.age > 18 (only pauses if true)

// Logpoint: Print without stopping
// Right-click line → "Add Logpoint" → {user}, {state}
// Prints every time line executes

// Evaluate expression: While paused, type in console
// user.name.uppercase()  // Execute expressions live
```

</details>

**3. LeakCanary (Detect memory leaks):**

<details>
<summary>💻 Code Example</summary>

```bash
# Auto-detects in logcat
# Look for: LeakCanary: FOUND LEAK [Activity] retained

# Manual heap dump:
# Android Studio → Memory Profiler → Dump Heap
# Analyzer → search "Activity" → retained reference chain
```

</details>

**4. Perfetto (Performance profiling):**

<details>
<summary>💻 Code Example</summary>

```bash
# Record system trace
adb shell perfetto -c /data/test-trace.pb.txt --out /sdcard/trace.pb

# Or use Studio Profiler (GUI, simpler)
# Android Studio → Profiler → Record → Scroll list
# Shows: frame timing, GC pauses, CPU usage
```

</details>

**5. Chucker (Network inspection):**

<details>
<summary>💻 Code Example</summary>

```gradle
// In-app HTTP inspector
implementation "com.github.chuckerteam.chucker:library:4.1.1"

// Shows: all API calls, response times, bodies, errors
// Access: Notification drawer during debug build
```

</details>

**6. Thread safety check:**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Verify you're on Main thread
if (Looper.myLooper() == Looper.getMainLooper()) {
    Log.w("Threading", "On main! Blocking will ANR")
}

// If you need to switch threads
if (Looper.myLooper() != Looper.getMainLooper()) {
    runOnUiThread { updateUI() }  // Or withContext(Dispatchers.Main)
}
```

</details>

### Quick Debugging Checklist

> **TL;DR:** Crash: find exception in logcat, read stack trace bottom-up, jump to line, reproduce (always? intermittent?). Lag: trace frames with Perfetto, check allocations. Wrong state: add logs to trace divergence from expected path.

Crash workflow · Lag detection · State tracing

**When App Crashes:**
<details>
<summary>💻 Code Example</summary>

```
1. Logcat: adb logcat | grep -E "Exception|FATAL"
2. Stack trace: Read BOTTOM-UP (root cause often buried)
3. Line number: Jump to crash location
4. Reproduce: Always crash? Intermittent? (race condition!)
5. Null check: 90% of crashes = NullPointerException. Check .value accesses.
```

</details>

**When App Lags (15fps instead of 60fps):**
<details>
<summary>💻 Code Example</summary>

```
1. Perfetto: See which frame dropped, which function took time
2. Profiler: CPU-bound or memory-bound? (CPU = too much logic, Memory = GC)
3. Logcat: "skipped 50 frames" message? Too much work on Main thread
4. Allocations: GC running every frame? (LeakCanary for leaks)
```

</details>

**When State is Wrong:**
<details>
<summary>💻 Code Example</summary>

```
1. Add logs: Print state transitions, find divergence
2. StateFlow.collect: Watch value changes before/after
3. Trace critical path: "After API call, state should be X, but is Y"
```

</details>

### Example Debugging Session (Real Interview Question)

**Scenario:** "Profile screen shows old user name after edit. How do you debug?"

**Approach (5 min):**

<details>
<summary>💻 Code Example</summary>

```
1. Reproduce: Does it always happen? Every time? (Helps isolate)

2. Logcat inspection:
   adb logcat | grep "Profile"
   → Look for API call success/failure

3. ViewModel state:
   Add log after API response:
   Log.d("Profile", "API returned: $user")
   _state.value = user
   Log.d("Profile", "State updated to: $_state.value")
   → Check if state actually updated

4. Repository cache:
   Check: Does cache.invalidate(userId) get called after API success?
   If not, next load hits stale cache.

5. Hypothesis: Cache not invalidated
   Fix: Add cache.clear() after successful API call

6. Test: Edit profile → navigate away → navigate back
   → Old name still shows? Or now fixed?

7. Root cause found: Cache invalidation missing
   Fix: cache.invalidate(userId) after POST
```

</details>

**Interview Answer Formula:**
<details>
<summary>💻 Code Example</summary>

```
"I would:
1. Check logcat for API response (is it successful?)
2. Add logs in ViewModel to trace state transitions
3. Check Repository for cache invalidation
4. Hypothesis: Cache not cleared after update
5. Fix: Add cache.invalidate() after API success
6. Test and verify"
```

</details>

This signals: systematic debugging, understanding of layers (Repository), cache considerations.

