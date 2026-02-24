[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 4. Architecture & Clean Principles

### MVI vs MVVM

> **TL;DR:** MVVM = multiple independent flows (state scattered). MVI = single immutable state (SSOT), all changes funnel through reducer. MVI better for complex UIs, MVVM simpler for small screens.

`MVVM` scattered state · `MVI` unidirectional · `SSOT` single source · `Intent → Reducer → State` · `Deterministic`

| Aspect | MVVM | MVI |
|---|---|---|
| **State** | Multiple flows (loading, user, error) | Single StateFlow<UiState> |
| **Changes** | Direct ViewModel updates | Through Intents + Reducer |
| **Testing** | Many state combos to test | Pure function testing |
| **Debugging** | Hard to track state history | Replay intents |
| **Complexity** | Simpler, fewer types | More boilerplate, clearer flow |

<details>
<summary>💻 Code Example</summary>

```kotlin
// MVVM: scattered
val loading: Flow<Boolean>
val user: Flow<User>
val error: Flow<String?>
// Problem: loading=true && user=loaded simultaneously?

// MVI: unified
data class UiState(val loading: Boolean, val user: User?, val error: String?)
val state: StateFlow<UiState>  // Single source of truth
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### State machine in MVI

**Reducer as pure function:**
```kotlin
private fun reduce(state: UiState, intent: UiIntent): UiState = when (intent) {
    is UiIntent.Search -> state.copy(
        query = intent.q,
        isLoading = true,
        results = emptyList()  // Deterministic: same intent always produces same state change
    )
    is UiIntent.ResultsLoaded -> state.copy(
        isLoading = false,
        results = intent.results
    )
}
```

**Intent collection loop:**
```kotlin
viewModelScope.launch {
    intentFlow.collect { intent ->
        val newState = reduce(_state.value, intent)
        _state.value = newState  // Single write point

        // Side effects (outside reducer)
        when (intent) {
            is UiIntent.Search -> launchSearchEffect(intent.q)
        }
    }
}
```

### Why MVI is deterministic

- **Same intents → same state:** Reducer is pure function (no randomness, no system state)
- **Event sourcing:** Can replay intents to reconstruct any past state
- **Time travel debugging:** Log intents, re-apply to debug specific sequence

**MVVM determinism issue:**
```kotlin
// ❌ MVVM indeterminism
viewModel.load() {
    _loading.value = true
    _user.value = loadUser()  // Meanwhile, error flow also updates
    _error.value = null       // Race: which one executed first?
}
```

### What it reuses & relies on

- **Sealed interfaces** — exhaustive Intent types (compiler ensures all handled)
- **Data classes** — immutable State with .copy() for updates
- **StateFlow** — hot flow for state distribution
- **Coroutine scope** — intentFlow collection in viewModelScope

### Why this design was chosen

**MVVM benefits (why it's used):**
- Less boilerplate for simple screens
- Direct ViewModel.property updates feel natural
- Industry standard (LiveData era)

**MVI benefits (why Netflix, Airbnb, etc. use it):**
- Unidirectional data flow (easier to reason about)
- All changes logged (Intents) → debuggable
- Pure reducers → unit testable (no mocks)
- Prevents state inconsistency (loading + user both true)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "MVI is unidirectional" | All state changes funnel through single reduce() function; no back-channel mutations |
| "Intent → State" | Compiler enforces exhaustiveness; missing intent case = compilation error |
| "Replay intents to debug" | Can capture intent sequence, re-apply reduce() in same order, get exact state history |
| "MVVM is simpler" | MVVM: fewer types + conventions (loose). MVI: more types but compiler + conventions (strict) |

### Gotchas at depth

- **Reducer purity cost:** If reducer needs side effects (API calls), must be outside reduce(). Need separate effect handler.
- **Intent ordering:** If intents arrive out-of-order (coroutines completing non-sequentially), state diverges (need intent queue or sequential dispatcher).
- **State size:** StateFlow with large state object can cause performance issues on heavy recomposition (use data class with value equality).
- **Testing boilerplate:** MVI needs test for every state transition; MVVM can "test by hand" on small screens (doesn't scale).

</details>

### Clean Architecture (Dependency Rule)

> **TL;DR:** 3-layer model: Data (repos, API) → Domain (use cases, pure Kotlin) → Presentation (UI). Each layer depends only on inner layers. Domain is independent.

`3 layers` · `Dependency Rule` · `Testable` · `Domain is pure Kotlin` · `No cross-layer dependencies`

| Layer | Role | Depends On | Example |
|---|---|---|---|
| **Presentation** | Compose screens, ViewModels, navigation | Domain only | `SearchViewModel`, `SearchScreen` |
| **Domain** | Use cases, interfaces, models | Nothing | `SearchUseCase`, `Repository` interface |
| **Data** | Repo impls, data sources, mappers | Nothing (boundary) | `SearchRepositoryImpl`, `ApiDataSource` |

<details>
<summary>💻 Code Example</summary>

```kotlin
// Presentation
class SearchViewModel(val useCase: SearchUseCase) { }

// Domain (pure Kotlin, testable standalone)
interface SearchRepository
class SearchUseCase(val repo: SearchRepository)

// Data
class SearchRepositoryImpl : SearchRepository
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Dependency enforcement at module level

**Gradle module structure:**
```
:shared:domain/
  src/main/kotlin/
    SearchRepository (interface)
    SearchUseCase

:shared:data/
  build.gradle.kts: depends on :shared:domain
  src/main/kotlin/
    SearchRepositoryImpl

:android:app/
  build.gradle.kts: depends on :shared:domain (NOT :shared:data!)
  src/main/kotlin/
    SearchViewModel (injected SearchUseCase)
```

**Module dependency rules in build.gradle.kts:**
```kotlin
// :shared:domain (innermost, no dependencies)
dependencies {
    // No Android, no app dependencies
}

// :shared:data
dependencies {
    implementation(project(":shared:domain"))
    // Data layer implementation details (Room, Retrofit)
}

// :android:app (presentation)
dependencies {
    implementation(project(":shared:domain"))  // Only public contracts
    // NOT :shared:data (hidden behind interface)
}
```

**Compiler enforcement:** If you import `SearchRepositoryImpl` in ViewModel, IDE marks red (no transitive dependency). Prevents accidental coupling.

### What it reuses & relies on

- **Gradle module system** — separate compilation units, dependency graph
- **Interface/implementation pattern** — Data layer hidden behind Domain interfaces
- **Testability** — Domain layer testable without Android, Hilt, or database
- **Package-private** — Scala/Kotlin can use package-private to hide impl classes from outside module

### Why this design was chosen

**Problems it solves:**
- **Tight coupling:** Without layers, UI directly accesses database → UI changes break data layer
- **Testability:** Without Domain isolation, every test needs mocks for DB, Android framework
- **Business logic reuse:** Domain layer independent → logic shareable across platforms (Android, iOS, backend)

**Why 3 layers specifically:**
- Domain = business logic (core of app, most valuable)
- Data = storage/network (implementation detail, often changed)
- Presentation = UI framework (Android/Compose specific)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Domain has no Android" | Domain has no transitive Android deps; if you try to import Android class in Domain, build fails (module not on classpath) |
| "Depend inward only" | Presentation → Domain (unidirectional). Data also depends on Domain. No cycles allowed (DAG, not graph). |
| "Domain is testable" | Because Domain module has zero Android deps, unit tests run on local JVM (not instrumented tests on emulator) |
| "Use interfaces for coupling" | Data.SearchRepository (interface in Domain) implemented by Data.SearchRepositoryImpl. Presentation never imports Impl. |

### Gotchas at depth

- **Transitive dependencies leak:** If Data depends on Retrofit, and Presentation depends on Data, then Presentation has Retrofit available. Can import accidentally (no protection unless split further).
- **Module count overhead:** Many small modules = slower builds (Gradle has overhead per module). Some projects collapse Data+Domain into single module to reduce complexity.
- **Cross-module sealed classes:** Sealed class in Domain with subtypes in Data works but odd. Usually sealed classes stay in single layer.
- **Circular dependencies:** If Presentation → Data and Data → Presentation (rare bug), build fails with Gradle cycle detection. Forces you to fix architecture.

</details>

### KMP: expect/actual

> **TL;DR:** `expect` in commonMain declares API; `actual` in androidMain/iosMain provides implementation. Compiler validates 1:1 matching at link time. Use for platform-specific APIs only; prefer KMP libraries first.

`expect` declares API · `actual` implements · `Compile-time matched` · `Link time validation` · `One per platform`

<details>
<summary>💻 Code Example</summary>

```kotlin
// commonMain/Platform.kt
expect fun getPlatformName(): String

// androidMain/Platform.kt
actual fun getPlatformName(): String = "Android"

// iosMain/Platform.kt
actual fun getPlatformName(): String = "iOS"
```

</details>

**Best practice hierarchy:**
1. Prefer KMP-compatible library (e.g., `kotlinx.datetime`)
2. Abstract behind interface + dependency injection
3. Use `expect`/`actual` only for unavoidable APIs (e.g., platform clipboard)

<details>
<summary>🔩 Under the Hood</summary>

### Compiler resolution & linkage

**Compilation phases:**
```
Phase 1: commonMain compilation
  - expect fun getPlatformName(): String  (declaration, placeholder)
  - Compiler notes: "expects actual in each platform"

Phase 2: androidMain/iosMain compilation
  - actual fun getPlatformName(): String = "Android"  (implementation)
  - Compiler matches: "actual matches expect signature"

Phase 3: Linking (merge IR)
  - Intermediate Representation (IR) for common + actual merged
  - expect → replaced with actual's IR
  - Final binary contains only actual implementation
```

**Compilation error example:**
```kotlin
// ❌ Mismatch: expect vs actual signature differs
// commonMain
expect fun getPlatformName(): String

// androidMain
actual fun getPlatformName(): Int = 1  // Wrong return type!

// Error: Expected return type String, found Int
```

### What it reuses & relies on

- **Kotlin IR (Intermediate Representation)** — compiler's platform-agnostic IR format
- **Multiplatform metadata** — Gradle tracks which files are expect/actual
- **Linker** — final IR merge determines which actual is linked for each platform
- **Compiler plugins** — Kotlin compiler has KMP support built-in

### Why this design was chosen

**Alternative 1: Runtime reflection**
```kotlin
// No, bad for KMP
fun getPlatform() = Class.forName("com.app.PlatformImpl").getConstructor().newInstance()
```
- Slow, bloated runtime
- Fails on ahead-of-time platforms (Native, WASM)

**expect/actual approach:**
- Compile-time resolution (no runtime cost)
- Works on all Kotlin targets (JVM, Native, JS, WASM)
- Compiler enforces 1:1 matching

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "expect is interface, actual is impl" | Slightly wrong: expect/actual are functions (not interface/impl). Compiler validates they match, then replaces expect with actual in IR. |
| "Works across platforms" | Compiler builds separate binaries (Android APK, iOS framework); each links its own actual. Common code compiled once, shared. |
| "One actual per platform" | If you have androidMain but not iosMain for an expect, build fails (missing actual). Must provide for every platform used. |
| "expect/actual is inheritance" | No: they're parallel function definitions. Not method override (no polymorphism); compile-time substitution. |

### Gotchas at depth

- **Generic expect/actual:** `expect fun <T> getValue(): T` with `actual fun <T> getValue(): T = ...` works, but type erasure can surprise (T might be Int, String, etc.)
- **Expect class with members:** `expect class Config { expect val name: String }` requires each actual to provide actual properties (verbose).
- **No private actual:** If actual is private or internal, it won't match public expect. Visibility must align.
- **Expect in common, but no platform uses it:** Dead code. Gradle doesn't warn (rare but confusing if forget to provide actual).

</details>

### KMM Project Structure

|Module|Role|
|---|---|
|**`shared/`**|`commonMain` (shared logic), `androidMain` (Android actuals), `iosMain` (iOS actuals)|
|**`androidApp/`**|Android app, depends on `shared`, Jetpack Compose|
|**`iosApp/`**|Xcode project, consumes `shared` as framework (SPM or CocoaPods)|

### Sharing ViewModels in KMP

> **TL;DR:** `androidx.lifecycle:lifecycle-viewmodel` is KMP-stable (2.7.0+). Define ViewModels in commonMain. iOS: SKIE exposes StateFlow as Swift AsyncSequence. DI: Koin (Hilt Android-only).

`lifecycle-viewmodel KMP-stable` · `SKIE for iOS` · `StateFlow → AsyncSequence` · `Koin DI` · `commonMain ViewModels`

<details>
<summary>💻 Code Example</summary>

```kotlin
// commonMain/SearchViewModel.kt
class SearchViewModel(val repo: SearchRepository) : ViewModel() {
    val state: StateFlow<SearchState> = MutableStateFlow(SearchState())
    fun search(query: String) { /* */ }
}

// androidMain — works as-is
// iosMain — SKIE wraps StateFlow
```

</details>

**iOS interop (SKIE):**
<details>
<summary>💻 Code Example</summary>

```swift
// iOS automatically gets:
let viewModel = SearchViewModel(repo: repo)
for await state in viewModel.state.asAsyncSequence() {
    // state is SearchState (Swift native type, thanks to SKIE)
}
```

</details>

**DI:** Use Koin in commonMain; Hilt doesn't support commonMain (Android-only annotations).

<details>
<summary>🔩 Under the Hood</summary>

### lifecycle-viewmodel KMP architecture

**Gradle dependency:**
```kotlin
// commonMain
dependencies {
    implementation("androidx.lifecycle:lifecycle-viewmodel:2.7.0")  // Multiplatform!
}
```

**What's included:**
```kotlin
// Multiplatform (all platforms):
public expect class ViewModel : Closeable { }
public abstract class ViewModelProvider.Factory { }

// androidMain (Android-specific):
actual class ViewModel : Closeable {
    // Android lifecycle integration: onCleared() call
}

// iosMain:
actual class ViewModel : Closeable {
    // iOS lifecycle integration: deinit
}
```

### SKIE: StateFlow → AsyncSequence

**Problem:** Swift doesn't understand Kotlin Flow API.
```swift
// Without SKIE:
let flow: StateFlow = viewModel.state  // ❌ What is StateFlow? No Swift equivalent
```

**Solution: SKIE (Scope Functions Integration Engine)**
```
SKIE compiler plugin → intercepts Kotlin-to-Swift bridging
StateFlow<T> → generates Swift extension: asyncSequence() : AsyncSequence<T>
Collector/emission mechanism → translated to Swift async iteration
```

**Result:**
```swift
// With SKIE:
for await state in viewModel.state.asAsyncSequence() {
    // Native Swift async/await semantics!
}
```

### Koin DI in commonMain

```kotlin
// commonMain
val appModule = module {
    single<SearchRepository> { SearchRepositoryImpl(get()) }
    factory { SearchViewModel(get()) }
}

// iOS App Delegate
KoinKt.startKoin(config: KoinAppConfig(modules: [appModule]))
```

**Why not Hilt?**
- Hilt uses Android-specific annotations (@HiltViewModel, @AndroidEntryPoint)
- Not available in commonMain (compilation would fail on iOS)
- Koin is pure Kotlin + iOS-compatible

### What it reuses & relies on

- **Closeable interface** — ViewModel.onCleared() invoked when lifecycle ends
- **Kotlin memory model** — viewmodel state lives in heap (JVM), native memory (iOS)
- **SKIE compiler plugin** — Kotlin Native bridging (generates Swift extensions)
- **StateFlow** — already KMP-compatible (part of kotlinx.coroutines)

### Why this design was chosen

**Motivation:**
- Business logic often 60-80% identical across platforms
- ViewModels hold this logic (use cases, state management)
- Sharing ViewModel = share without re-implementing

**Before 2026:**
- ViewModel was Android-only (lifecycle-viewmodel had no KMP)
- Forced code duplication or complicated workarounds

**After 2026:**
- ViewModel is KMP-stable
- iOS can use same ViewModel class as Android
- SKIE makes StateFlow feel native in Swift

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "ViewModels in commonMain" | ViewModel definition is in common code, but ViewModel lifecycle management is platform-specific (Android/iOS) |
| "SKIE wraps StateFlow" | SKIE plugin generates Swift extension; StateFlow<T> becomes async iterable in Swift (not runtime conversion, compile-time codegen) |
| "Koin for DI" | Koin is runtime reflection-based DI (slower than Hilt codegen), but pure Kotlin (no Android deps) |
| "ViewModel survives rotation" | Android: lifecycle tied to Activity retention. iOS: tied to view controller lifetime (managed separately via SKIE). |

### Gotchas at depth

- **ViewModel memory:** If ViewModel holds large state (bitmap, list), it survives Android rotation (good!) but might keep iOS memory alive unexpectedly (use WeakReference carefully).
- **Dispatcher inheritance:** ViewModel in commonMain uses Dispatchers.Main. iOS doesn't have "Main dispatcher" natively; SKIE maps it to main queue (thread 0).
- **SKIE limitations:** Complex Kotlin generics, sealed classes, platform-specific types (List<T> works, but nullable generics tricky).
- **Lifecycle mismatch:** ViewModel.onCleared() on Android = Activity destroyed. iOS = view controller deinit. Timing differs (Android can restore, iOS usually doesn't).

</details>

### CocoaPods in KMP

Packages `shared` as CocoaPods pod for Xcode. `cocoapods {}` in `shared/build.gradle.kts`. Alternative: **SPM** gaining traction.

---

