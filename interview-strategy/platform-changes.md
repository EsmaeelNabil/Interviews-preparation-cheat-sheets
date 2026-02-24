[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 13. BONUS: Platform Changes & Security (2026)

### Android 16 Breaking Changes (Migration Guide)

|Change|Impact|Action|Testing Strategy|
|---|---|---|---|
|**Adaptive apps** (sw600dp+)|Orientation/resize **ignored** on tablets/foldables. Declared orientation forced.|Test multi-size layouts. `material3.adaptive` for responsive UI.|Run on physical tablet or `resizable-emulator`. Check portrait ↔ landscape.|
|**Predictive back**|Peek animation default, **cannot opt-out**. User sees animation before back triggers.|Use `OnBackPressedCallback` for custom back logic. Coordinate animations with peek.|Test back gesture visually. Ensure animations don't conflict with peek.|
|**16KB page size**|**Native libraries MUST align to 16KB** pages (was 4KB). Misaligned libs fail to load.|Recompile NDK code with latest NDK. Update `CMakeLists.txt`. Verify `.so` alignment.|Test on API 36 device/emulator. Check `adb logcat` for "Failed to dlopen" errors.|
|**Edge-to-edge**|Status/nav bar background colors **ignored**. System draws colors; app draws behind.|Use `WindowInsets` APIs to inset content (padding). `WindowCompat.setDecorFitsSystemWindows(false)`.|Test with light/dark status bar. Check padding on notch devices.|
|**Safer Intents**|Implicit intents **must match exported intent filters**. Unmatched intents throw `ActivityNotFoundException`.|Audit all `startActivity()` calls. Use explicit intents or add matching `<intent-filter>`.|Run `adb logcat`, search for "ActivityNotFoundException". Test intent-receiving apps.|

**Migration checklist for existing apps:**
1. Update `compileSdk = 36`
2. Run lint: `./gradlew lint` → fix hardcoded widths for tablets
3. Test on API 36+ emulator (create multi-size AVD)
4. Update native build if using NDK
5. Audit `startActivity()` calls → add `<intent-filter>` or use explicit Intents
6. Test predictive back gesture (pull from edge, release to cancel)

### Security Quick Hits

|Topic|Key Detail|
|---|---|
|**Credential Manager**|Standard auth. `CredentialManager.getCredential()`|
|**EncryptedSharedPreferences**|`security-crypto` for tokens|
|**Network Security Config**|Cert pinning via XML|
|**R8 full mode**|Default AGP 8+. Know `-keep` rules.|
|**`exported`**|Required since API 31. Default `false`.|

### Common Performance Pitfalls (& Fixes)

|Pitfall|Impact|Symptom|Fix|
|---|---|---|---|
|**Too many recompositions**|60fps → 15fps (jank)|Frames drop during scroll|Use `derivedStateOf`, stable params, `remember` for expensive computations|
|**Large image unoptimized**|Memory spikes, OOM crash|OutOfMemoryError on load|Use `Coil`/`Glide` with `.size(200, 200)` sampling|
|**Blocking I/O on Main**|ANR (App Not Responding) crash after 5s|"App not responding" dialog|Move to `Dispatchers.IO` via `withContext`|
|**Allocating in scroll callback**|GC pauses every frame|Jank during fast scroll|Pre-allocate objects, reuse lists, avoid `new` in callbacks|
|**Database queries N+1**|100 queries instead of 1. 500ms → 50ms|Load screen slow, list items sluggish|Use SQL joins, `@Relation`, Room `.with()` |
|**Flow doesn't unsubscribe**|Memory leak, coroutine runs forever|Battery drain, memory growth|Use `repeatOnLifecycle(STARTED)` or `collectAsStateWithLifecycle()`|

**Common N+1 query example:**
<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ BAD: Fetch users, then loop to fetch posts (100 queries for 100 users)
val users = db.getAllUsers()  // 1 query
for (user in users) {
    user.posts = db.getPostsByUserId(user.id)  // 100 queries!
}

// ✅ GOOD: Fetch in one query
@Entity
data class UserWithPosts(
    @Embedded val user: User,
    @Relation(parentColumn = "id", entityColumn = "userId") val posts: List<Post>
)

val usersWithPosts = db.getUsersWithPosts()  // 1-2 queries total
```

</details>

### Performance Tooling

|Tool|Purpose|How to Read|
|---|---|---|
|**Studio Profiler**|CPU, memory, network (live)|Look for sustained high CPU (>30%), memory spikes. Allocations = garbage collection trigger.|
|**Perfetto** (System Trace)|Frame-level trace. Shows which functions run per frame.|Green = on-time frame (60fps). Red = dropped frame. Drill into to see which function took time.|
|**Baseline Profiles**|AOT compilation → **30-40% faster startup**, 20% less jank|Add via `android.baselineProfileRules`. Run on real device to generate `.txt` profile.|
|**Macrobenchmark**|Measure startup time, scroll FPS, frame compositing time|Baseline against previous version. Target: startup <1s, scroll ≥55fps.|
|**Compose Compiler Metrics**|Stability/skippability per composable. `restartable`, `skippable`, `scheme`|`restartable` = can recompose alone. `skippable` = does if params stable. Find unstable params → cause cascade recompositions.|

**Profiling workflow:**
1. **Identify jank:** Feel sluggish? Run Perfetto → see which frame drops
2. **Profile CPU:** Studio Profiler → CPU tab → record 5s → see top functions
3. **Check memory:** Memory tab → Dump heap → analyze for leaks (retained objects)
4. **Baseline:** Macrobenchmark on release build → startup time, scrolling FPS

**Example: Finding recomposition hotspot:**
<details>
<summary>💻 Code Example</summary>

```bash
./gradlew debugComposeCompilerMetrics
# Generates build/compose-metrics/ComposableMetrics.txt
# Look for `unstable` → find why (e.g., mutableListOf passed as param)
```

</details>

