# 🔥 LAST-MINUTE ANDROID INTERVIEW CHEAT SHEET

---

## 📑 Quick Navigation (Collapsible TOC)

<details>
<summary>Click to expand all 44 sections</summary>

### Core Fundamentals
1. [Data Structures & Big O](#1-data-structures--big-o-the-under-the-hood-section)
2. [Kotlin Language Deep Dive](#2-kotlin-language-deep-dive-start-simple-go-deeper)
3. [Concurrency & Kotlin Coroutines](#3-concurrency--kotlin-coroutines)

### Architecture & Design
4. [Architecture & Clean Principles](#4-architecture--clean-principles)
5. [Dependency Injection (DI)](#5-dependency-injection-di)
6. [Memory & Performance](#6-memory--performance)

### Android Components & Patterns
7. [Android Components & Lifecycles](#7-android-components--lifecycles)
8. [Testing Essentials (Staff Level)](#8-testing-essentials-staff-level)
9. [Live Coding Survival (25-Minute Strategy)](#9-live-coding-survival-25-minute-strategy)

### System & Build
10. [System & Feature Design (For Bolt)](#10-system--feature-design-for-bolt)
11. [Gradle & Build Tooling](#11-gradle--build-tooling)

### Advanced Topics (12-44)
- 12. Design Patterns & Strategic Questions
- 13. Networking & API Design
- 14. Interview Strategy
- 15. Platform Changes & Security (API 34+, 35+, 36+)
- 16. Jetpack Compose Advanced Patterns
- 17. Room Database Advanced Patterns
- 18. Permissions & Scoped Storage
- 19. Broadcast Receivers & Intent Filters
- 20. Services, JobScheduler, WorkManager (Deep)
- ... (and 24+ more sections)

**Scan time:** All titles visible in <10 seconds ⚡
**To find a section:** Use browser search (Cmd+F / Ctrl+F) to jump to section number

</details>

---

<details open>
<summary>⚡ Quick Scan — All 44 Topics (click to collapse)</summary>

| # | Topic | TL;DR |
|---|---|---|
| 1 | Data Structures & Big O (The "Under the Hood" Section) | (Coming soon...) |
| 2 | Kotlin Language Deep Dive (Start Simple, Go Deeper) | Flow operators transform/combine streams. Each choice reflects a design decision: serial vs parallel, buffer vs... |
| 3 | Concurrency & Kotlin Coroutines | `collectAsStateWithLifecycle` collects only when lifecycle ≥ STARTED (usually ON_RESUME). Stops automatically in background, preventing wasted... |
| 4 | Architecture & Clean Principles | `androidx.lifecycle:lifecycle-viewmodel` is KMP-stable (2.7.0+). Define ViewModels in commonMain. iOS: SKIE exposes StateFlow as Swift AsyncSequence.... |
| 5 | Dependency Injection (DI) | Hand-written AppContainer with constructor injection. No codegen overhead, fully transparent. Scales to ~50 classes comfortably;... |
| 6 | Memory & Performance | Recomposition = re-run composable when inputs change. Composition tree caches state via `remember`. Compiler skips... |
| 7 | Android Components & Lifecycles | SavedStateHandle (ViewModel-integrated) survives process death. onSaveInstanceState() survives config change only. Use SavedStateHandle for state, onDestroy()... |
| 8 | Testing Essentials (Staff Level) | Test Double replaces real dependency. Fakes are real logic (in-memory DB). Mocks verify interactions (was... |
| 9 | Live Coding Survival (25-Minute Strategy) | (Coming soon...) |
| 10 | System & Feature Design (For Bolt) | Design entities with indices on query columns. Use foreign keys with CASCADE for referential integrity.... |
| 11 | Gradle & Build Tooling | Dependency conflicts occur when transitive deps want different versions. Gradle defaults to *highest version*. Fix... |
| 12 | Strategic "Reverse" Questions | (Coming soon...) |
| 13 | BONUS: Platform Changes & Security (2026) | (Coming soon...) |
| 14 | Interview Strategy & Communication Tips | Ask questions that show you're thinking about trade-offs and culture fit. For technical companies: deep... |
| 15 | Debugging & Common Bugs | Crash: find exception in logcat, read stack trace bottom-up, jump to line, reproduce (always? intermittent?).... |
| 16 | Jetpack Compose Advanced Patterns | Snapshot system captures state at recomposition. Immutable data prevents unnecessary recompositions (Stability = Compose can... |
| 17 | Room Database Advanced Patterns | `@Transaction` wraps multiple queries in SQLite transaction (all succeed or all fail). Use for multi-step... |
| 18 | Permissions & Scoped Storage | Can't access shared `/sdcard/DCIM` directly. Use app-specific dirs (no permission) OR MediaStore + permission. |
| 19 | Fragments & Navigation | `navigate()` adds to back stack (default). `popUpTo()` pops previous entries. `popBackStack()` returns false if no... |
| 20 | Camera & Media Integration | Create `ExoPlayer` → set `MediaItem` (URL or local file) → `prepare()` → `play()`. Always `release()`... |
| 21 | Push Notifications & FCM | On app startup, get current token via `FirebaseMessaging.getInstance().token`. Sync with backend. Listen for `onNewToken()` refreshes. |
| 22 | Common Interview Gotchas | Orientation/locale/font scale change = Activity destroyed + recreated by default. **Solution:** Save in `SavedStateHandle` (auto-persists)... |
| 23 | Accessibility (a11y) & Localization (i18n) | Create `res/values-<locale>/strings.xml` for each language (e.g., `values-es`, `values-fr`). Framework auto-selects based on device locale. For... |
| 24 | Analytics & Crash Reporting | Call `FirebaseCrashlytics.getInstance().recordException(exception)` to log crashes. Use `.setCustomKey()` for context, `.setUserId()` for user identification. Crashes auto-reported... |
| 25 | Code Organization & Architecture | Write ADR (Architecture Decision Records) for major choices. Add KDoc with `@param`, `@throws`, `@return` for... |
| 26 | RecyclerView Optimization | Extend `DiffUtil.ItemCallback<T>` with `areItemsTheSame()` + `areContentsTheSame()`. Use `ListAdapter.submitList()` to compute diff and update only changed... |
| 27 | Custom Views & Canvas Drawing | Override `onMeasure()` (set size) → `onLayout()` (position) → `onDraw()` (draw). Pre-allocate Paint in member variable—never... |
| 28 | Animations & Transitions | `animateDpAsState()` observes state, animates to target value. Use `spring()`, `tween()`, or `keyframes()` specs. For multiple... |
| 29 | Battery Optimization & Doze Mode | Use `adb shell dumpsys batterystats` to profile drain. Check for partial wakelocks (held >1 sec... |
| 30 | SSL/TLS & Network Security | Define per-domain security policies in `network_security_config.xml`. Set certificate trust anchors, disable cleartext. Reference in AndroidManifest. |
| 31 | Instrumentation Tests & UI Testing | Use `ActivityScenarioRule` to launch activity. `onView(withId())` to find views. `perform(click())` for actions. `check(matches())` for assertions. |
| 32 | ProGuard/R8 Obfuscation Gotchas | R8 obfuscates & shrinks code for release. Enable `minifyEnabled true` + `shrinkResources true`. Use `-keep`... |
| 33 | RxJava vs. Coroutines Comparison | RxJava = stream abstraction, threading explicit (observeOn/subscribeOn), built-in backpressure. Coroutines = sequential async code, Dispatchers,... |
| 34 | Biometric Authentication & In-App Billing | Initialize `BillingClient` → `queryProductDetailsAsync()` to list products → `launchBillingFlow()` to start purchase. Handle `BillingResult` for... |
| 35 | Data Binding & View Binding Best Practices | Use `<data>` block in layout XML to bind variables + event handlers. Automatic UI updates... |
| 36 | Feature Flags & A/B Testing | Hash userId + testName to consistently assign variant. Log to analytics. Compare metrics between control... |
| 37 | Weak References & Memory Management | `WeakHashMap<K, V>` removes entry when key is unreferenced. Useful for caches tied to object lifetime... |
| 38 | App Shortcuts & Widgets | Extend `AppWidgetProvider`, override `onUpdate()`, use `RemoteViews` to build UI. Register receiver in manifest with `APPWIDGET_UPDATE`... |
| 39 | App Bundle vs. APK Distribution | Create dynamic feature modules, request download via `SplitInstallManager.startInstall()`. Google Play splits APK by device config... |
| 40 | Testing Strategies by Scenario | Launch activity with `ActivityScenarioRule`. Perform user flows (login → profile → edit). Assert UI state... |
| 41 | Lint Warnings to Watch | MissingPermission, UnreachableCode, MissingSuperCall = errors (fix immediately). RecyclerView handlers, NotFragmentAttached = warnings (fix most cases).... |
| 42 | Version Compatibility & Graceful Degradation | Don't assume all API N+ devices have feature X. Use `PackageManager.hasSystemFeature()` to verify feature exists. |
| 43 | Common Interview Red Flags (What NOT to Do) | GlobalScope = memory leak. Mutable objects exposed = state bugs. Blocking calls = ANR. Hardcoded... |
| 44 | Last-Minute Interview Prep (Night Before) | 5 questions interviewers ALWAYS ask. Prepare 1-2 min answers. Think out loud. Show reasoning. |

</details>


---

## 📁 Browse by Category

| Folder | Topics |
|---|---|
| [🔧 Android Core](android-core/) | [Android Components & Lifecycles](android-core/components-lifecycles.md), [Permissions & Scoped Storage](android-core/permissions-storage.md), + 5 more |
| [🏗️ Architecture](architecture/) | [Architecture & Clean Principles](architecture/architecture-patterns.md), [Dependency Injection (DI)](architecture/dependency-injection.md), + 1 more |
| [🔨 Build & Testing](build-testing/) | [Gradle & Build Tooling](build-testing/gradle-build.md), [Testing Essentials (Staff Level)](build-testing/testing-essentials.md), + 3 more |
| [🌐 Data & Networking](data-networking/) | [Networking & API Design](data-networking/networking-api.md), [Room Database Advanced Patterns](data-networking/room-database.md), + 5 more |
| [💡 Interview Strategy](interview-strategy/) | [System & Feature Design](interview-strategy/system-design.md), [Live Coding Survival](interview-strategy/live-coding.md), + 9 more |
| [🚀 Kotlin](kotlin/) | [Data Structures & Big O](kotlin/data-structures.md), [Kotlin Language Deep Dive](kotlin/kotlin-language.md), + 1 more |
| [⚡ Performance](performance/) | [Memory & Performance](performance/memory-performance.md), [Battery Optimization & Doze](performance/battery-optimization.md), + 1 more |
| [🎨 UI & Graphics](ui/) | [Jetpack Compose Advanced Patterns](ui/compose-advanced.md), [RecyclerView Optimization](ui/recyclerview.md), + 4 more |

