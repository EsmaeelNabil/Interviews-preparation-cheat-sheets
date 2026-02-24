[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 3. Concurrency & Kotlin Coroutines

### Threads vs. Coroutines — The Analogy

> **TL;DR:** Threads block (hold OS resources); coroutines suspend (yield to scheduler). ~100K coroutines fit on 8 threads; 8 threads = max ~100 actual OS threads (rest blocked).

`Thread blocks` · `Coroutine suspends` · `~100K on 8 threads` · `No OS context switch` · `State machine under hood`

**Simple analogy:** Thread = waiter standing idle at table. Coroutine = waiter handling many tables (while kitchen cooks for table 1, waiter takes order at table 2).

<details>
<summary>💻 Code Example</summary>

```kotlin
// Thread: blocks, holds OS resource
thread { api.fetch() }  // Thread sleeps here, doing nothing
println("Never runs")   // Until fetch returns

// Coroutine: suspends, releases thread
launch { api.fetch() }  // Suspends, thread freed
println("Runs immediately")  // While fetch is in flight
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### State machine, not actual suspension

**What you write:**
```kotlin
launch {
    val user = api.fetch()  // Suspension point
    updateUI(user)
}
```

**What happens internally:**
```kotlin
// Compiler generates state machine (pseudocode)
when (label) {
    0 -> { api.fetch(continuation) }  // Request API, return control
    1 -> { updateUI(result) }           // Resume here after API done
}
```

The **thread is freed at label 0**. Scheduler uses it for other tasks. When API completes, scheduler resumes the coroutine on an available thread (usually same, but could be different).

### What it reuses & relies on

- **Continuation<T>** protocol — callback interface (JVM standard)
- **CoroutineDispatcher** — thread pool scheduler (Dispatchers.Main, Default, IO)
- **Job hierarchy** — parent/child relationship, cancellation propagation
- **CPS transformation** — compiler converts suspension points to state machine

### Why this design was chosen

**Thread-per-coroutine model** (hypothetical alternative):
- Simple: no state machine transformation needed
- But: 1 thread = 1 MB+ OS memory → max ~1K threads before OOM
- Context switches expensive (microseconds per switch)

**Coroutine (suspension) model:**
- Coroutine state = small heap object (~1 KB) → 100K+ fit in RAM
- No OS context switch (function call instead, nanoseconds)
- Compiler does heavy lifting at compile time (CPS), runtime is lean

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| Coroutines are "lightweight" | Lightweight because they don't consume OS thread; suspended coroutine is just an object with local state |
| Can have 100K coroutines on 8 threads | Thread pool has 8 OS threads; each can resume multiple coroutines (not bound to one) |
| `Dispatchers.Main` runs on UI thread | Main dispatcher uses the UI thread for scheduling; coroutine can suspend/resume multiple times on it |
| Coroutine "runs" in background | Actually: running in thread pool, suspends at I/O call, resumes when I/O done (might be different thread) |

### Gotchas at depth

- **Threads aren't eliminated:** Dispatcher still uses thread pool (I/O = 64 threads, Default = CPU cores). Coroutines don't eliminate threads; they enable **multiplexing** (many coroutines per thread).
- **CPU-bound work:** If coroutine does compute (no suspension), it blocks the thread. 100K CPU-bound coroutines would still block all 8 threads (no benefit over threads). Coroutines shine with I/O-bound work.
- **Dispatcher switching:** Coroutine can resume on different thread than it suspended (if dispatcher changes). User shouldn't care, but affects debugging (stack traces fragmented).

</details>

### Dispatchers — When & Why

> **TL;DR:** Dispatcher = thread pool scheduler. Main = UI thread only. IO = 64 threads (elastic). Default = CPU cores. Choose based on work type.

`Main` UI-safe · `IO` for I/O · `Default` for CPU work · `Unconfined` testing only · `withContext()` to switch

| Dispatcher | Thread Pool | Use For |
|---|---|---|
| **Main** | UI thread (single) | UI updates, StateFlow collection, light work |
| **IO** | 64+ threads (elastic) | Network, disk, database, file I/O |
| **Default** | CPU core count | Sorting, parsing, JSON, heavy compute |
| **Unconfined** | Caller thread (testing only) | Unit tests with `runTest` |

**Decision tree:**
- Networking/DB? → **IO**
- Image decode, sorting, JSON? → **Default**
- UI state/updates? → **Main** (or `collectAsStateWithLifecycle` auto-switches)
- Blocking I/O call? → `withContext(IO) { blockingCall() }`
- Heavy compute only? → **Default**
- Heavy compute + I/O? → Start on **Default**, `withContext(IO)` for I/O

<details>
<summary>🔩 Under the Hood</summary>

### Thread pool mechanics

**Main dispatcher:**
```kotlin
// Compiles to: schedule on Android's Looper.getMainLooper()
withContext(Dispatchers.Main) {
    textView.text = "Hello"  // UI thread guaranteed
}

// Blocking here = ANR (timeout if > 5 sec)
```

**IO dispatcher (elastic pool):**
```kotlin
// Pseudocode: thread pool with queue
pool.execute {
    // Run on thread T1, T2, ..., T64 (or higher if dynamic)
}

// If all 64 threads busy, job waits in queue
// New threads created if load persistent (up to limit)
```

**Default dispatcher (CPU-bound):**
```kotlin
// Thread pool size = CPU core count (usually 8 on modern phones)
// Each thread handles sequentially (no multiplexing within core)
val result = withContext(Dispatchers.Default) {
    JSON.parse(largeString)  // Uses 1 core exclusively
}

// If all cores busy, job waits
```

### What it reuses & relies on

- **Executor framework** (Java standard) — underlying thread pool interface
- **ForkJoinPool** (IO, Default) — work-stealing scheduler (reduces contention)
- **Looper** (Main) — Android message queue
- **Job hierarchy** — dispatcher respects parent scope cancellation

### Why this design was chosen

**Single Main thread:**
- Only 1 UI thread (Android rule, not choice)
- Serializes UI updates (prevents race conditions)
- Alternative would be multi-threaded UI (nightmare for developers)

**IO = 64 threads (not CPU cores):**
- I/O-bound work often **blocks** (waiting for network response)
- More threads than cores = other work can proceed while one thread waits
- Limit = 64 (empirical sweet spot; prevents resource exhaustion)

**Default = CPU cores:**
- CPU-bound work doesn't benefit from more threads (no parallelism within core)
- Context switching cost > benefit
- Keeps CPU hot (better cache locality)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use IO for network" | IO dispatcher has 64 threads so one network call doesn't block others; Default has only CPU cores so CPU-bound work serializes |
| `withContext(IO)` switches threads | Suspends coroutine on current thread, resumes on IO pool thread; transparent to user |
| "Main is the UI thread" | Main dispatcher forwards to Android Looper; blocking = ANR (system kills app if Main blocked > 5 sec) |
| Multiple tasks on IO run "in parallel" | Up to 64 can run simultaneously; 65th waits. All on separate threads but CPU may time-slice |

### Gotchas at depth

- **withContext doesn't switch threads inline:** `withContext(IO) { /* runs on IO */ }` suspends, returns control, resumes later. Not atomic from caller's perspective.
- **Main thread pool size = 1:** Easy to ANR if you don't dispatcher-switch. Common bug: long compute on Main.
- **IO pool dynamic growth:** Not instantaneous. Under load, new threads created lazily (may cause spike latency).
- **Dispatcher stickiness:** Coroutine resumes on same dispatcher, but NOT necessarily same thread. Thread IDs can differ before/after suspension.

</details>

### Exception Handling in Coroutines

> **TL;DR:** Exceptions in launched coroutines don't propagate to try-catch. Instead, use `CoroutineExceptionHandler`. Job hierarchy determines scope: Job cancels all children; SupervisorJob isolates.

`CoroutineExceptionHandler` · `Job cancels siblings` · `SupervisorJob isolates` · `Flow.catch emits` · `Context inheritance`

<details>
<summary>💻 Code Example</summary>

```kotlin
val handler = CoroutineExceptionHandler { _, ex ->
    _errors.update { ex.message }
}
viewModelScope.launch(handler) {
    val user = repo.getUser()  // Exception → handler, not crash
}
```

</details>

| Scenario | Pattern |
|---|---|
| **Single task fails** | `CoroutineExceptionHandler` in launch context |
| **Multiple independent tasks** | `SupervisorJob()` to isolate failures |
| **Flow (stream) error** | `.catch { emit(Result.Error(it)) }` |

<details>
<summary>🔩 Under the Hood</summary>

### Job hierarchy & cancellation propagation

**Job (default):**
```kotlin
val parentJob = Job()
val scope = CoroutineScope(parentJob)

scope.launch { throw Exception() }  // Child fails
scope.launch { println("Still runs?") }  // NO! Parent cancelled all children

// Exception thrown → Job.cancel() called → all children cancelled
```

**SupervisorJob (isolates):**
```kotlin
val supervisor = SupervisorJob()
val scope = CoroutineScope(supervisor)

scope.launch { throw Exception() }  // Child fails
scope.launch { println("Runs!") }  // YES! Sibling survives

// Exception thrown → only that child failed, parent survives
```

**Compiler transformation:**
```kotlin
viewModelScope.launch(exceptionHandler) { }

// Becomes:
launch {
    context = current + exceptionHandler
    try {
        // Your code
    } catch (e: Exception) {
        exceptionHandler.handleException(context, e)
    }
}
```

### Context inheritance

```kotlin
// Parent context:
CoroutineScope(Dispatchers.Main + exceptionHandler)

// Child inherits:
launch {  // Inherits exceptionHandler automatically
    withContext(Dispatchers.IO) {  // Keeps handler, changes dispatcher
        // Still under exceptionHandler
    }
}
```

**Override:** `launch(newHandler) { }` replaces parent's handler.

### What it reuses & relies on

- **CoroutineContext** — map of (Element.Key → Element), handler is one key
- **Job interface** — parent/child relationship, state machine (NEW → ACTIVE → COMPLETED)
- **Cancellation exception** — `CancellationException` thrown when job cancelled
- **Exception handler chain** — context iterates handlers, catches first match

### Why this design was chosen

**Why not try-catch for launched coroutines?**
- Launched coroutines are "fire-and-forget" (no return value)
- Exception bubbles to Job, not to caller (async/await DO use try-catch)
- Handler gives global place to centralize error logic

**Job vs SupervisorJob:**
- Job = fail-fast (one error cancels scope)
- SupervisorJob = resilient (failures isolated)
- Trade-off: Job simpler but loses context on error; SupervisorJob requires manual cleanup

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| Exception in `launch { }` crashes app | Exception triggers `CoroutineExceptionHandler` in context; if no handler, default handler crashes app |
| `SupervisorJob` is for multiple tasks | SupervisorJob stores each child failure but doesn't propagate; parent survives, but child Job is CANCELLED |
| `viewModelScope` uses Job | ViewModelScope uses `SupervisorJob` internally (actually, it's Job wrapped, with error handling) |
| `catch { }` in Flow stops errors | Actually: catch emits error result, doesn't stop collection (unless you return) |

### Gotchas at depth

- **viewModelScope default:** Uses `SupervisorJob()` internally, so one launch failure doesn't crash scope (good!). But you still need handlers for UI error display.
- **Async inherits handler but doesn't trigger it:** `async { throw }` doesn't auto-crash; exception stored in resulting Deferred, thrown on `await()`.
- **Multiple handlers in chain:** Context can have multiple handlers (rare). First one wins; others ignored.
- **CancellationException not caught by handler:** `CancellationException` (from explicit cancel/timeout) not passed to handler (by design). Other exceptions are caught.

</details>

### StateFlow vs SharedFlow

> **TL;DR:** StateFlow = always holds current value (SSOT); replays to new subscribers. SharedFlow = stateless, no replay by default. Use StateFlow for UI state, SharedFlow for events.

`StateFlow` for state · `SharedFlow` for events · `Replay` control · `distinct` built-in · `Hot flow`

| Feature | StateFlow | SharedFlow |
|---|---|---|
| **Holds value?** | Yes (current state) | No (stateless) |
| **New subscriber gets?** | Last emitted value | Nothing (unless `replay > 0`) |
| **`distinctUntilChanged`?** | Built-in | Manual via `.distinctUntilChanged()` |
| **Use for** | UI state, SSOT | Events, broadcasts, no-state flows |
| **Memory overhead** | Single value stored | Replay buffer stored (if replay > 0) |

<details>
<summary>💻 Code Example</summary>

```kotlin
val state = MutableStateFlow("init")
state.collect { println(it) }  // Prints "init" immediately

val events = MutableSharedFlow<String>()
events.collect { println(it) }  // Waits; no replay
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### StateFlow storage & replay

**What you write:**
```kotlin
val state = MutableStateFlow("initial")
val subscriber1 = launch { state.collect { println(it) } }
state.value = "updated"
val subscriber2 = launch { state.collect { println(it) } }
```

**What happens:**
```
Subscriber 1: Prints "initial" (immediately on collect)
State changed to "updated"
Subscriber 2: Prints "updated" (immediately on collect, replay of last value)
```

**Memory layout:**
```kotlin
class StateFlowImpl<T> {
    @Volatile var value: T = initialValue  // Single stored value
    var subscribers: List<Subscriber> = emptyList()
}

// Update triggers:
state.value = newValue  // Notifies all subscribers, overwrites old value
```

### SharedFlow with replay buffer

```kotlin
val events = MutableSharedFlow<String>(replay = 5)
events.emit("event1")
events.emit("event2")
events.emit("event3")

val subscriber = launch { events.collect { } }  // Gets events 1, 2, 3 (replay of last 3)
```

**Memory overhead:**
```kotlin
class SharedFlowImpl<T> {
    var replayBuffer: CircularBuffer<T> = CircularBuffer(capacity = 5)
    // Stores last N emitted items
}
```

### What it reuses & relies on

- **Flow interface** — Hot flow (always running, not lazy)
- **Collector/Subscriber** — stateful listener for updates
- **CoroutineContext** — emits/collects run in scope's dispatcher
- **Mutex (internal)** — ensures thread-safe `.value` access in StateFlow

### Why this design was chosen

**StateFlow for UI state:**
- Holder of current state (Single Source of Truth)
- New subscribers always get latest (no "what is the state?" question)
- Simpler mental model (always has value vs. might have nothing)

**SharedFlow for events:**
- Decoupled broadcast (multiple listeners, not tied to state)
- Optional replay (events that happened in past, useful for logging)
- More flexible (events are ephemeral, state is persistent)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| StateFlow has current value | `.value` is @Volatile field; atomic access but not thread-safe for complex updates |
| New StateFlow subscriber gets last value | On subscribe, collector enters subscriber list and immediately emitted last stored value |
| "SharedFlow with replay=0" = cold | Actually: still hot (emits happen even if no subscribers), just not stored |
| StateFlow replays, SharedFlow doesn't | StateFlow built-in replay; SharedFlow replay optional (circular buffer if `replay > 0`) |

### Gotchas at depth

- **StateFlow.value vs collect race:** Setting `.value` while collecting doesn't skip intermediate values (if set twice rapidly, both emitted). Update is immediate, all subscribers notified.
- **Replay buffer overflow:** If SharedFlow receives more items than buffer size, oldest items dropped. `onBufferOverflow = DROP_OLDEST` (default).
- **StateFlow memory spike:** If state is large object (bitmap, large list), replaying to all subscribers can cause memory pressure.
- **equivalence check:** StateFlow uses `.equals()` for distinctUntilChanged. Custom objects must override equals.

</details>

### collectAsStateWithLifecycle — The 2026 Standard

> **TL;DR:** `collectAsStateWithLifecycle` collects only when lifecycle ≥ STARTED (usually ON_RESUME). Stops automatically in background, preventing wasted work. Better than `collectAsState` (which collects forever).

`Lifecycle-aware` · `Stops in background` · `KMP stable` · `No memory leak` · `Hot flow efficient`

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ Old (2024 and before)
val state = viewModel.state.collectAsState()  // Collects forever, wastes work

// ✅ New (2026+)
val state = viewModel.state.collectAsStateWithLifecycle()  // Stops at PAUSED
Text(state.value)
```

</details>

**Configuration:**
<details>
<summary>💻 Code Example</summary>

```kotlin
collectAsStateWithLifecycle(
    minActiveState = Lifecycle.State.STARTED  // Default: STARTED (collects if STARTED or above)
)
// Options: STARTED, RESUMED, etc.
```

</details>

- **Library:** `lifecycle-runtime-compose:2.9.4` (stable, non-experimental, KMP-compatible)
- **Performance:** Prevents Flow collection when app in background (no unnecessary API calls, less battery drain)

<details>
<summary>🔩 Under the Hood</summary>

### LifecycleOwner observer registration

**What you write:**
```kotlin
@Composable
fun MyScreen(viewModel: MyViewModel) {
    val state = viewModel.state.collectAsStateWithLifecycle()
    // state.value = latest emission
}
```

**What compiler generates (simplified):**
```kotlin
// Under hood:
val lifecycleOwner = LocalLifecycleOwner.current  // From Compose scope

val observer = object : LifecycleEventObserver {
    override fun onStateChanged(source: LifecycleOwner, event: Lifecycle.Event) {
        when (event) {
            ON_RESUME -> startCollecting()  // minActiveState = STARTED → actually ON_START
            ON_PAUSE -> stopCollecting()
        }
    }
}
lifecycleOwner.lifecycle.addObserver(observer)

// Effect cleanup:
DisposableEffect(lifecycleOwner) {
    onDispose { lifecycle.removeObserver(observer) }
}
```

### Lifecycle state machine

```
CREATED → STARTED → RESUMED → PAUSED → STOPPED → DESTROYED

collectAsStateWithLifecycle collects when: STARTED, RESUMED
Stops when: PAUSED, STOPPED

// minActiveState = STARTED → collect if state ≥ STARTED
// minActiveState = RESUMED → collect only if state == RESUMED
```

### What it reuses & relies on

- **LocalLifecycleOwner** (Compose runtime) — injects lifecycle from Activity/Fragment
- **LifecycleEventObserver** (Architecture components) — observer pattern for lifecycle events
- **Compose State** — produces `State<T>` for recomposition on value change
- **DisposableEffect** — cleanup observer when composable left (scoped cleanup)

### Why this design was chosen

**Alternative: collectAsState (old):**
- Collects forever (even in background)
- Waste: API requests, computation, battery drain
- Memory: Flow continues subscription even after onPause

**collectAsStateWithLifecycle (new):**
- Stops collection at onPause (app backgrounded)
- Resumes at onStart
- Automatic cleanup (no manual unsubscribe)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Stops collecting when app backgrounded" | Lifecycle observer removed at ON_PAUSE; DisposableEffect cleanup triggered automatically |
| "collectAsState keeps collecting" | collectAsState uses no lifecycle observer; collection persists even if Activity destroyed (memory leak if ref held) |
| "Non-experimental in 2026" | Stable API; kotlinx.lifecycle:lifecycle-runtime-compose is standard (no breaking changes expected) |
| Works with Compose only | Requires LocalLifecycleOwner (Compose Composable); can't use in non-Compose code directly |

### Gotchas at depth

- **Recomposition timing:** Collection paused at onPause, but recomposition can still happen if state changes mid-pause (rare). Value won't update if not collecting.
- **minActiveState subtlety:** `minActiveState = STARTED` = "collect if lifecycle ≥ STARTED". Not "collect exactly at STARTED"; "at STARTED or any state above".
- **Multiple min states:** If you have multiple flows with different minActiveState, each starts/stops independently (mixing STARTED + RESUMED flows = complex behavior).
- **No livedata equivalence:** Unlike LiveData's automatic onCleared, DisposableEffect must be in effect scope. If Composable leaves without proper scope, might not clean up (rare with Compose best practices).

</details>

---

