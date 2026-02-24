[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 22. Common Interview Gotchas

### Process Death vs. App Kill

> **TL;DR:** **Process death** (OOM, system cleanup) = `onDestroy()` NOT called, SavedStateHandle restored. **App kill** (user force-stop) = all state lost, cold start. Must handle both.

Process death · App kill · SavedStateHandle recovery · Singleton loss

| Scenario | onDestroy Called | SavedState | Singletons | Flow |
|---|---|---|---|---|
| Process death | ❌ No | ✅ Restored | ❌ Lost | Activity recreated, ViewModel survives |
| App kill | ❌ No | ❌ Lost | ❌ Lost | Cold start, everything resets |
| User back | ✅ Yes | N/A | N/A | Normal lifecycle |

**Key:** Both must be handled identically—assume nothing persists except SavedStateHandle.

### Preventing ANR (Application Not Responding)

> **TL;DR:** ANR = 5-second Main thread block. Move I/O + heavy compute to background thread. Use `viewModelScope.launch(Dispatchers.IO)` for network, `Dispatchers.Default` for CPU-heavy.

Main thread blocked → ANR dialog · 5-second threshold · Async required

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ BAD: Blocks Main thread
val user = api.getUser().blockingSingle()  // ANR if >5s

// ✅ GOOD: Async I/O
viewModelScope.launch(Dispatchers.IO) {
    val user = repo.getUser()
    withContext(Dispatchers.Main.immediate) {
        _state.value = UiState.Success(user)
    }
}

// ✅ GOOD: Heavy compute off Main
viewModelScope.launch(Dispatchers.Default) {
    val filtered = applyFilters(bitmap)
    withContext(Dispatchers.Main) { updateUI(filtered) }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### ANR Detection

**Mechanism:**
- Main thread starts task → framework sets watchdog timer (5 sec)
- If task completes before timeout → OK
- If timeout → System shows ANR dialog, can kill app

**Watchdog runs on separate thread**, periodically checking Main thread state.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Don't block Main thread" | Framework has internal watchdog (separate thread). If Main blocked >5s, Watchdog fires, shows ANR dialog. |
| "Use Dispatchers.IO for network" | IO dispatcher uses thread pool (limited by CPU cores). Designed for I/O wait. Better than Default (CPU-bound). |
| "Update UI in Main" | Only Main thread can update Views. All other threads must post back via Looper/runOnUiThread. |

### Gotchas at depth

- **Network on UI thread (old code):** Pre-7.0, network on UI thread threw NetworkOnMainThreadException but didn't ANR. Post-7.0, enforced strictly.
- **Slow inflate/layout:** Inflating 100 views on Main = ANR candidate. Consider async inflation or lazy layouts.
- **Callback chains:** If callback spawns another callback (chains), Main can block unexpectedly. Profile to find it.

</details>

### Measuring App Startup Time

> **TL;DR:** **Cold start** = worst (closed → visible). **Warm start** = backgrounded → visible. **Hot start** = paused → resumed. Measure with Studio Profiler or `adb shell am start-profiling`.

Cold/warm/hot start · Profiler tool · Macrobenchmark for CI

<details>
<summary>💻 Code Example</summary>

```
Cold start:  App closed → tap icon → activity visible (worst)
Warm start:  App backgrounded → tap → activity visible
Hot start:   Activity paused → tap → onResume (fastest)

Measure:
1. Android Studio Profiler → App Startup (live, visual)
2. adb: adb shell am start-profiling com.example.app | grep "Total time"
3. Macrobenchmark: @RunWith(MacrobenchmarkRule::class) for CI
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Cold Start Timeline

```
Click app → System creates process → ClassLoader loads app classes →
Application.onCreate() → Activity.onCreate/onStart/onResume → First frame
```

**Bottlenecks:**
- App initialization (lazy? expensive?)
- First Activity inflation (layout complexity)
- Network requests in onCreate()

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Startup time matters" | System tracks startup metric. Poor startup = Android vitals score reduced (affects app store ranking). |
| "Cold start worst" | Process creation + ClassLoader + DI initialization = highest cost. Warm start reuses process (memory already allocated). |
| "Profile with Macrobenchmark" | Macrobenchmark runs in separate process, forces cold start, measures wall-clock time. Reproducible for CI. |

### Gotchas at depth

- **Splash screens:** Badly timed splash screens can mask real startup time or add delay. Use AppCompat's SplashScreen API (defers removal until ready).
- **Content providers:** Content providers initialized before Application.onCreate(). Heavy init = slow startup.
- **R.id references:** Accessing R.id fields triggers resource parsing. Lazy load if not critical path.

</details>

### View Hierarchy & Drawing (View vs. Compose)

> **TL;DR:** **View:** onMeasure() → onLayout() → onDraw() + invalidate() for redraws. **ViewGroup:** measures/positions all children recursively. **Compose:** no hierarchy; recomposition → layout → GPU draw.

Measure/layout/draw · invalidate() triggers redraw · ViewGroup recursion · Compose recomposition

| Lifecycle | Purpose | Call Count |
|---|---|---|
| `onMeasure()` | Determine size (constraints) | Multiple (parent + children) |
| `onLayout()` | Position children, set bounds | Once per measurement |
| `onDraw()` | Render content (Canvas ops) | On invalidate() |
| `invalidate()` | Trigger redraw | On state change |

**Compose differs:** No View instances, no onMeasure/onLayout. Instead: emit Composables → Recompose → Layout phase → GPU draw (RenderNode).

<details>
<summary>🔩 Under the Hood</summary>

### ViewGroup Drawing Flow

```kotlin
// What framework does internally:
ViewGroup.draw() {
    onDraw()  // Draw ViewGroup's own content
    dispatchDraw() {  // Call draw() on each child
        for (child in children) {
            child.draw()  // Recursive: child.onDraw() + child's children
        }
    }
}
```

**Canvas operations:** Draw method receives Canvas object. Canvas talks to low-level graphics (Skia). Skia submits to GPU or software renderer.

### Compose Recomposition & Drawing

**Recompose:** When state changes, affected composables re-execute (return new tree).

**Layout phase:** Measure composables with constraints, determine size/position.

**Draw phase:** Composables emit to RenderNode (GPU-optimized structure).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "onDraw called on invalidate()" | invalidate() calls requestLayout on parent. Parent redraws child in next frame. Handled by Choreographer (syncs to 60Hz). |
| "ViewGroup measures children" | Measure is recursive. Parent constraint = (parent width - padding). Child constraint = remaining space. Child onMeasure sets its size. |
| "Compose skips unchanged branches" | Composables marked @Immutable + skipped if inputs unchanged. Reduces recomposition cost. Not guaranteed (dev error). |

### Gotchas at depth

- **Over-invalidation:** Calling invalidate() too often = Frame drops. Use minimally or batch via Choreographer.
- **Expensive onDraw:** Allocating objects in onDraw() = garbage → jank. Pre-allocate Paints, Paths outside onDraw().
- **Over-recomposition:** If composable state not memoized, recomposes unnecessarily. Use remember { } and .equals() wisely.

</details>

### Configuration Changes

> **TL;DR:** Orientation/locale/font scale change = Activity destroyed + recreated by default. **Solution:** Save in `SavedStateHandle` (auto-persists) OR set `android:configChanges` to skip recreation.

Activity recreation · SavedStateHandle persistence · configChanges flag · ViewModel survival

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ GOOD: Automatic via SavedStateHandle
class MyViewModel(val savedState: SavedStateHandle) : ViewModel() {
    var userId: Int
        get() = savedState.get<Int>("userId") ?: 0
        set(value) { savedState["userId"] = value }
}

// ✅ ALSO GOOD: Skip recreation if not needed
// AndroidManifest.xml
<activity android:name=".MainActivity"
    android:configChanges="orientation|screenSize" />

// Activity.kt
override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)
    // Handle layout changes without full recreation
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Configuration Change Flow

**Default (no configChanges):**
```
Orientation change detected → System calls Activity.onDestroy() → Activity.onCreate() with new config → onStart/onResume
ViewModel survives (held in ViewModelStore)
SavedStateHandle auto-restored (framework serializes Bundle)
UI state lost if only in Activity fields
```

**With configChanges="orientation":**
```
Orientation change → onConfigurationChanged() called INSTEAD of recreate
You handle layout changes manually
No onCreate called, ViewModel not recreated
```

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "SavedStateHandle persists state" | Framework serializes SavedStateHandle to Bundle. On activity recreate, Bundle restored, values available (even if process killed). |
| "configChanges skips recreation" | If you handle configChanges, framework sends onConfigurationChanged(). You DON'T recreate; handle layout manually (cost savings). |
| "ViewModel survives recreation" | ViewModel held by ViewModelStore (separate from Activity). Activity recreate doesn't destroy ViewModel. Process death does. |

### Gotchas at depth

- **Partial configChanges:** If you handle "orientation" but not "locale", locale change still triggers full recreate. Specify all handled changes.
- **Layout inconsistency:** If you manually handle config change but forget layout resource, UI might render wrong. Test on real device.
- **Memory leak from old activity:** If ViewModel holds reference to activity context, old activity not garbage collected post-recreate. Use applicationContext instead.

</details>

---

