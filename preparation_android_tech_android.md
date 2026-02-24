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

## 1. Data Structures & Big O (The "Under the Hood" Section)

### ArrayList vs. LinkedList

|Feature|ArrayList|LinkedList|
|---|---|---|
|**Backing**|Dynamic array|Doubly-linked nodes|
|**Access**|O(1) random access|O(n) traversal|
|**Insert (end)**|O(1) amortized|O(1)|
|**Insert (middle)**|O(n) shift elements|O(1) if at node, O(n) to find|
|**Memory**|Contiguous, cache-friendly|Per-node overhead, scattered|
|**When to use**|95% of cases. Read-heavy, index-based|Frequent insert/remove at head/middle with iterator|

**ArrayList resize:** When capacity is exceeded, it allocates a **new array ~1.5x** the current size and copies all elements — amortized O(1) but worst-case O(n) for that single insertion. **Why 1.5x?** Sweet spot: reduces reallocation frequency (exponential growth) vs. memory waste. Cost is spread: one O(n) spike per ~log(n) insertions.

**Memory reality:** LinkedList has **24-40 bytes per node** overhead (object header + next/prev refs). For 1000 integers: ArrayList ≈ 4KB; LinkedList ≈ 40KB. Cache efficiency: ArrayList accesses contiguous memory (L1 cache hit); LinkedList scatters (L3 cache miss). **Practical impact:** ArrayList often faster even for inserts due to modern CPU speeds.

### HashMap Internals (Deep Dive)

**Buckets & Hashing:** A HashMap is an array of "buckets"; the bucket index is `key.hashCode() & (capacity - 1)` (bitwise AND, equivalent to modulo for power-of-2 sizes). Capacity is **always a power of 2** (1, 2, 4, 8...) for this trick to work.

**Collisions & Treeification:** When two keys hash to the same bucket, they form a **linked list**. In Java 8+/Kotlin JVM, when a bucket exceeds **8 entries**, it converts to a **red-black tree**. Why 8? A threshold study found it balances: linked list overhead for small counts vs. tree rebalancing overhead. Nodes store `hash`, `key`, `value`, `next` (~40 bytes).

**Load Factor & Resize:** Default load factor = **0.75**. Triggers resize at 75% capacity (e.g., 12 entries in 16-bucket map). Why 0.75? Empirical trade-off: <0.75 = wasted space; >0.75 = higher collision rate. Resize: capacity **doubles** (e.g., 16 → 32), all entries **rehashed** (O(n)). Worst case: many adds push load beyond 0.75 repeatedly.

**Complexity Guarantees:**
- **Average O(1):** Assumes good hash distribution. Most keys in different buckets.
- **Worst O(n):** Bad hashing (many keys → same bucket) or deliberate collision attack (DoS). After treeification, degrades to **O(log n)** instead.
- **String hashing:** Java caches `.hashCode()` after first call. Custom objects: override `hashCode()` and `equals()` together, always.

### Big O Quick-Table

|Operation|Array|HashMap|LinkedList|
|---|---|---|---|
|**Access**|O(1)|O(1) avg|O(n)|
|**Search**|O(n)|O(1) avg|O(n)|
|**Insert**|O(n)|O(1) avg|O(1) at head|
|**Delete**|O(n)|O(1) avg|O(1) at node|

---

## 2. Kotlin Language Deep Dive (Start Simple, Go Deeper)

---

### PART A: Data Classes & Destructuring

#### **The Basics (What it does)**

<details>
<summary>💻 Code Example</summary>

```kotlin
data class User(val id: Int, val name: String, val email: String)

val user = User(1, "Alice", "alice@ex.com")
println(user)  // User(id=1, name=Alice, email=alice@ex.com)
println(user.copy(name = "Bob"))  // Creates new copy with changed field

// Destructuring
val (id, name, email) = user
println("$id: $name")
```

</details>

#### **How to use it (Patterns)**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Auto-generated functions
val user1 = User(1, "Alice", "a@ex.com")
val user2 = User(1, "Alice", "a@ex.com")
println(user1 == user2)  // true (uses equals())

// Copying & updates
val updatedUser = user1.copy(name = "Bob", email = "b@ex.com")

// Collections benefit
val users = listOf(user1, user2)
users.distinct()  // Uses equals() & hashCode()

// Map to entities
val userMap = users.associateBy { it.id }  // Map<Int, User>
```

</details>

<details>
<summary><b>DEEP DIVE: How Data Classes Work Under the Hood</b></summary>

**Compiler magic:** Kotlin compiler **generates** these functions for data classes:

```kotlin
// What you write:
data class User(val id: Int, val name: String)

// Compiler generates:
class User(val id: Int, val name: String) {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true  // Same object?
        if (other !is User) return false  // Type check
        if (id != other.id) return false
        if (name != other.name) return false
        return true
    }

    override fun hashCode(): Int {
        var result = id.hashCode()  // Start with first field
        result = 31 * result + name.hashCode()  // Combine with others
        return result
    }

    override fun toString(): String =
        "User(id=$id, name=$name)"

    fun copy(id: Int = this.id, name: String = this.name): User =
        User(id, name)  // New instance with defaults

    operator fun component1(): Int = id  // For destructuring
    operator fun component2(): String = name
}
```

**Destructuring works via `componentN()` functions:**
```kotlin
val (id, name) = user
// Decompiles to:
val id = user.component1()
val name = user.component2()
```

**Key insight:** Data classes reuse standard object patterns. They're **syntactic sugar**, not new runtime concepts.

**Bytecode check:**
```bash
# Compile & decompile
kotlinc User.kt -d User.class
javap -c User.class  # Shows equals() is ordinary method
```

**Performance reality:**
- `equals()` is O(n) field comparisons (not reference comparison)
- `hashCode()` combines hashes (collision-safe)
- `copy()` always allocates new object (no structural sharing)

**Trade-off:** Convenience vs. allocation. Every `copy()` = new object. For 1000 users in list, `.distinct()` calls `equals()` O(n²) times worst-case.

</details>

---

### PART B: Extension Functions & Receiver

#### **The Basics (What it does)**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Add function to String without subclassing
fun String.isValidEmail(): Boolean = this.contains("@")

val email = "alice@ex.com"
println(email.isValidEmail())  // true (looks like String method!)

// Generic extension
fun <T> List<T>.second(): T = this[1]
listOf(1, 2, 3).second()  // 2
```

</details>

#### **How to use it (Patterns)**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Builder pattern via extensions
fun <T> buildList(block: MutableList<T>.() -> Unit): List<T> {
    val list = mutableListOf<T>()
    list.block()  // this = list
    return list
}

val numbers = buildList<Int> {
    add(1)
    add(2)
    add(3)
}

// Scope functions using receivers
user.apply { name = "Bob"; email = "b@ex.com" }  // Modify in-place
    .also { println(it) }  // Side effect
    .run { calculateScore() }  // Transform

// DSL building
html {
    body {
        div(id = "main") {
            h1 { +"Hello" }
            p { +"World" }
        }
    }
}
```

</details>

<details>
<summary><b>DEEP DIVE: Receivers & How Extension Functions Compile</b></summary>

**What you write:**
```kotlin
fun String.isValidEmail(): Boolean = this.contains("@")
```

**What compiler generates:**
```java
public static final boolean isValidEmail(String $this$isValidEmail) {
    return $this$isValidEmail.contains("@");
}
```

**The receiver (`this`) becomes first parameter!** Extension functions are **NOT actual methods**—they're **static functions with implicit first arg**.

**Receiver in scopes:**
```kotlin
// receiver = this = User object
user.apply {
    name = "Bob"  // this.name = "Bob"
    email = "b@ex.com"  // this.email = ...
}

// Decompiles to:
User $receiver = user;
$receiver.setName("Bob");  // Actual method call
$receiver.setEmail("b@ex.com");
return $receiver;
```

**DSL through receivers:**
```kotlin
// You write:
html {
    body { p { +"Hello" } }
}

// Receiver chain:
// html block: receiver = HTML object
// body block: receiver = BODY object (nested inside HTML)
// p block: receiver = P object (nested inside BODY)

// Decompiles to:
HTML html = new HTML();
BODY body = new BODY();
html.body(body);

P p = new P();
p.text("Hello");  // +"Hello" calls invoke on String receiver
body.p(p);
```

**Key insight:** Extensions are syntactic sugar over static methods. Allows **fluent chaining** and **DSL building** without inheritance.

**Performance:** No overhead—compiled to regular static calls. JIT inline them.

**Limitations:**
- No `private` access to receiver's private fields (compiled as outside class)
- Dispatch is **static** (not virtual)—no polymorphism

```kotlin
// ❌ Won't override
open class Animal
fun Animal.sound() = "generic"
class Dog : Animal()
fun Dog.sound() = "woof"

val dog: Animal = Dog()
dog.sound()  // Prints "generic" (static dispatch, not "woof")

// ✅ Virtual dispatch with open functions
open class Animal { open fun sound() = "generic" }
class Dog : Animal() { override fun sound() = "woof" }
dog.sound()  // "woof" (virtual dispatch)
```

</details>

---

### PART C: Inline Functions & Reified Generics

#### **The Basics (What it does)**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Regular function
fun <T> filter(list: List<T>, predicate: (T) -> Boolean): List<T> {
    return list.filter(predicate)
}

val numbers = listOf(1, 2, 3, 4)
val evens = filter(numbers) { it % 2 == 0 }

// ❌ Can't check generic type at runtime
// ❌ Lambda creates object allocation

// Inline function with reified
inline fun <reified T> parseJson(json: String): T {
    return when (T::class) {  // Can check T!
        User::class -> parseUserJson(json) as T
        Product::class -> parseProductJson(json) as T
        else -> throw IllegalArgumentException()
    }
}

val user: User = parseJson("""{"id":1,"name":"Alice"}""")  // Works!
```

</details>

#### **How to use it (Patterns)**

<details>
<summary>💻 Code Example</summary>

```kotlin
// Type-safe casts with reified
inline fun <reified T> Any.asOrNull(): T? = this as? T

val obj: Any = "Hello"
val str: String? = obj.asOrNull()  // Works: "Hello"
val int: Int? = obj.asOrNull()     // Works: null (not Int)

// No lambda allocation overhead
inline fun repeat(times: Int, block: () -> Unit) {
    for (i in 0 until times) {
        block()
    }
}
// block() calls are **inlined** (no lambda object created)

// With noinline (don't inline this lambda)
inline fun foo(crossinline callback: () -> Unit, noinline other: () -> Unit) {
    callback()  // Inlined
    other()     // Not inlined (stored in object)
}
```

</details>

<details>
<summary><b>DEEP DIVE: Inline & Reified Compilation Magic</b></summary>

**What you write:**
```kotlin
inline fun <reified T> parseJson(json: String): T {
    return when (T::class) {
        User::class -> parseUserJson(json) as T
        else -> throw IllegalArgumentException()
    }
}

val user: User = parseJson("""...""")
```

**What compiler generates (simplified):**
```java
// Function body COPIED into call site
User user;
String json = "...";
Class<?> $klass = User.class;  // Type argument materialized!
if ($klass.equals(User.class)) {
    user = (User) parseUserJson(json);
} else {
    throw new IllegalArgumentException();
}
```

**Key: Type argument reified at call site!** Compiler inserts `User.class` directly.

**Why only inline can be reified:**
- Generic type erasure: `List<String>` becomes `List` at runtime (JVM limitation)
- **Inline** = code copied → can use actual type
- **Non-inline** = separate function → can't access caller's type info

```kotlin
// ❌ Error: Can't be reified
fun <reified T> notInline(json: String): T {  // ERROR: reified needs inline
    // ...
}

// ✅ Works
inline fun <reified T> isInline(json: String): T {
    // Compiler copies body here; T is known
}
```

**Lambda allocation vs inline:**
```kotlin
// Regular function
fun processItems(items: List<Int>, action: (Int) -> Unit) {
    for (item in items) action(item)
}

val lambda = object : Function1<Int, Unit> {  // Object allocated on heap
    override fun invoke(x: Int) {
        println(x)
    }
}
processItems(numbers, lambda)

// Inline function
inline fun processItems(items: List<Int>, action: (Int) -> Unit) {
    for (item in items) {
        println(item)  // Code inlined here, NO object created!
    }
}
processItems(numbers) { println(it) }
```

**Bytecode comparison:**
```bash
# Regular: processItems calls invoke() on Function1 object
# Inline: processItems loop contains println directly (no lambda object)
```

**`crossinline` keyword (for nested coroutines):**
```kotlin
// ❌ Error: Can't use suspend in inlined lambda
inline fun launchAsync(block: suspend () -> Unit) {
    GlobalScope.launch { block() }  // Error: block not inlined (in lambda context)
}

// ✅ Fixed: Mark crossinline
inline fun launchAsync(crossinline block: suspend () -> Unit) {
    GlobalScope.launch { block() }  // block is inlined but prevents direct return
}
```

**Trade-off table:**

| Inline | Benefit | Cost |
|--------|---------|------|
| ✅ | Reified generics | Code bloat (inlined everywhere) |
| ✅ | No lambda allocation | Not suitable for recursive functions |
| ✅ | Return from lambda | Larger bytecode |
| ❌ | Can't be `private` | Can't use in Java |

**When to use:**
- Small functions (1-3 lines)
- Reified needed
- High-call-frequency (allocation matters)

**Avoid:**
- Large functions (code bloat)
- Library APIs (consumers pay cost)
- Recursive functions (infinite expansion)

</details>

---

### PART D: Coroutine Internals — How `suspend` Works (CPS Deep Dive)

> **TL;DR:** `suspend` functions compile to state machines via Continuation-Passing Style (CPS). The compiler transforms suspension points into labeled states, allowing one thread to manage 100K+ coroutines.

`suspend keyword` · `Continuation<T>` callback · `State machine` · `No OS threads` · `Yields, not blocks`

<details>
<summary>💻 Code Example</summary>

```kotlin
suspend fun getUser(id: Int): User {
    val cached = cache.get(id)
    if (cached != null) return cached
    val user = api.fetch(id)  // Suspension point
    return user
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Compiler transformation (CPS)

**What you write:**
```kotlin
suspend fun getUser(id: Int): User {
    val cached = cache.get(id)         // State 0
    if (cached != null) return cached
    val user = api.fetch(id)           // Suspension point → State 1
    cache.put(id, user)
    return user
}
```

**What compiler generates:**
```kotlin
fun getUser(id: Int, cont: Continuation<User>): Any {
    when (cont.label) {
        0 -> {  // State 0: check cache
            if (cached != null) { cont.resume(cached); return COROUTINE_SUSPENDED }
            else { cont.label = 1; return api.fetch(id, cont) }
        }
        1 -> {  // State 1: resume after fetch
            val user = (cont as MyContinuation).result()
            cache.put(id, user)
            return user
        }
    }
}
```

### What it reuses & relies on

- **Continuation<T>** callback interface (JVM standard, coroutines runtime)
- **CoroutineDispatcher** (Dispatcher.Main, Default, IO) — schedules resumed coroutines on thread pool
- **Suspending function protocol** — returns `COROUTINE_SUSPENDED` sentinel to indicate yielding
- **No stack frames stored** — locals become object fields (ContinuationImpl subclass)

### Why this design was chosen

**Alternative 1:** Thread per coroutine (like platform threads)
- Simpler model but 1 thread ≈ 1 MB stack → max 100K impossible (OOM at 1K)
- OS context switches expensive (microseconds each)

**CPS state machine approach:**
- Coroutine state lives in heap object (few KB) → 100K+ fit in RAM
- No OS thread context switch needed → switch is function call (~nanoseconds)
- JVM JIT can inline state transitions → minimal overhead

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| `suspend` pauses execution | Compiler inserts `label` field; each state is a branch in `when` |
| "Coroutines are lightweight" | Suspended coroutine = object holding locals + label; no OS resource held |
| `Dispatchers.Main` runs on UI thread | Dispatcher is thread pool; coroutine resumes on available thread (not bound to original) |
| `launch { }` starts a coroutine | Compiler creates `SafeContinuation` wrapper; runtime enqueues on dispatcher's queue |

### Gotchas at depth

- **No automatic stack trace in debugger:** Stack is broken across states (state 0 stack, state 1 stack separate). Debugger shows only current state. (Mitigated in IDE but confusing in logs.)
- **Locals are fields:** If coroutine suspends at same point twice with different locals, race condition possible if not careful. (Coroutine scope prevents this in practice.)
- **Cross-platform differences:** Native/Wasm have different CPS strategies. Kotlin/JS uses callbacks directly.

</details>

### PART E: sealed class vs sealed interface

> **TL;DR:** `sealed class` = shared state + single parent; `sealed interface` = type union + multi-inheritance. Start with interface (more flexible).

`sealed class` for shared state · `sealed interface` for type unions · Mutually exclusive subtypes · Exhaustive when

<details>
<summary>💻 Code Example</summary>

```kotlin
// Interface: type union (no shared state)
sealed interface UiState {
    data object Loading : UiState
    data class Success(val data: String) : UiState
    data class Error(val msg: String) : UiState
}

// Class: shared state + parent
sealed class ApiResponse<T>(val statusCode: Int) {
    class Success<T>(val data: T, statusCode: Int) : ApiResponse<T>(statusCode)
}
```

</details>

| Feature | `sealed class` | `sealed interface` |
|---|---|---|
| **Inheritance** | Single parent only | Multiple interfaces + one class |
| **State** | Constructor params, shared fields | No state, only methods |
| **Equals/hashCode** | Auto-generated in data subclasses | Manual or data class subtypes |
| **When to use** | Subtypes share common data | Type unions, multi-inheritance needed |

<details>
<summary>🔩 Under the Hood</summary>

### Compiler handling

**Sealed class:**
```kotlin
sealed class Result<T>(val ts: Long) {
    class Success<T>(val value: T, ts: Long = System.currentTimeMillis()) : Result<T>(ts)
}

// Compiler generates:
// - Result constructor calls stored in Result.kt bytecode (linkage metadata)
// - Subclass check: Result.class.getPermittedSubclasses() (Java 15+)
// - Only subclasses in same file/sealed hierarchy allowed
```

**Sealed interface:**
```kotlin
sealed interface Loadable
data class Item(val id: Int) : Loadable
class CustomItem(val id: Int) : Loadable

// Compiler generates:
// - Same permitted subclasses metadata
// - No state sharing (interface has no fields)
// - Subtypes can extend other classes simultaneously
```

### What it reuses & relies on

- **Java sealed types (Java 15+)** — compiled as `PermittedSubclasses` attribute
- **Data classes** — used for subclass implementations (auto-generate equals/hashCode/copy)
- **Single Inheritance Hierarchy** — sealed interface doesn't change single parent rule for classes, only adds interface implementation

### Why this design was chosen

**Sealed class:**
- Enforce exhaustive matching without error-prone inheritance
- Share common constructor/fields across variants (Result<T> with timestamp)
- Clear ownership: one family tree

**Sealed interface (Kotlin 1.4+):**
- More flexible: allow type A to be both `Loadable` AND `Parcelable`
- Decouple type union from class hierarchy
- Better for multi-concern types (UI state that's also serializable)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| `sealed` prevents external subclasses | Only subclasses in same file/module allowed (compiler enforces via PermittedSubclasses) |
| `when(state)` is exhaustive | Compiler tracks permitted subclasses; missing branch = compilation error |
| Sealed classes hold data | Sealed interface subtypes can implement other interfaces (e.g., `Parcelable`); more composable |
| Sealed interface is like abstract interface | No difference at runtime (both erased); difference is in what compiler enforces statically |

### Gotchas at depth

- **Inheritance + interface mix:** `sealed interface X` + `data class Y : X, Parcelable` works, but if `Parcelable` has conflicting methods, must implement both
- **toString/equals:** With sealed class, use data class subtypes for auto-generation. If mixing data + regular classes, equals() becomes manual
- **Multi-module sealed:** If sealed type is in module A, subclass in module B, compiler in B may not know it's sealed (depends on configuration)

</details>

### PART F: inline class (Value Class)

> **TL;DR:** `@JvmInline value class` = compile-time type-safe wrapper, erased at runtime. Zero allocation when passed directly; boxed only when stored in containers or interface returns.

`Type-safe IDs` · `No object allocation` · `Erased at runtime` · `Boxing in some contexts`

<details>
<summary>💻 Code Example</summary>

```kotlin
@JvmInline value class UserId(val value: Int)
@JvmInline value class Email(val value: String)

fun sendEmail(userId: UserId, email: Email) { /*...*/ }
sendEmail(UserId(123), Email("test@ex.com"))  // Type-safe, zero allocation
```

</details>

**When to use:** Wrapper types for primitives/strings passed frequently (IDs, emails, URLs). Skip if rarely used (negligible savings).

<details>
<summary>🔩 Under the Hood</summary>

### Compilation & erasure

**What you write:**
```kotlin
@JvmInline value class UserId(val value: Int)

fun sendEmail(userId: UserId, email: String) { }
val id: UserId = UserId(123)
sendEmail(id, "test@ex.com")
```

**What compiler generates:**
```java
// Erased: UserId doesn't exist at runtime
public static void sendEmail(int userId, String email) { }

// Call site:
int id = 123;  // No object created
sendEmail(id, "test@ex.com");
```

### Boxing behavior — When allocation occurs

```kotlin
@JvmInline value class UserId(val value: Int)

val id: UserId = UserId(123)              // ✅ No allocation
val boxed: Any = id as Any                // ❌ BOX! Wrapper created
val nullable: UserId? = id                // ❌ BOX! Nullable requires object
val inList: List<UserId> = listOf(id)     // ❌ BOX! Container = wrapper
interface Identifiable { fun id(): UserId }  // ❌ BOX! Interface boundary
```

**Compiler generates (for nullable/container):**
```java
// When UserId is nullable or in container:
public static final class UserId {  // Object wrapper created
    private final int value;
    public UserId(int v) { this.value = v; }
}
```

### What it reuses & relies on

- **JVM type erasure** — generics erased at runtime, inline classes leverage this
- **Value-based classes** (Java, JEP 169) — compiler recognizes immutable patterns
- **Escape analysis** (JIT) — optimizer can prove object escapes and eliminate allocation
- **Kotlin metadata** — `@JvmInline` annotation tells compiler to inline in JVM code

### Why this design was chosen

**Alternative: Regular wrapper class**
```kotlin
data class UserId(val value: Int)  // Every use allocates object
```
- Prevents parameter mix-ups (same benefit)
- But allocation cost: every call allocates wrapper → garbage pressure

**Inline class approach:**
- Type-safe at compile time (catches mistakes)
- Runtime cost = zero (erased to primitive)
- Tradeoff: Boxing in 4 specific contexts (documented above)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| Inline class is type-safe ID wrapper | Erased to underlying type at runtime; no object exists at JVM level |
| "Zero allocation" | Allocation free ONLY in direct parameter passing; boxed in containers/nullability |
| `UserId?` creates a wrapper | Nullable forces boxing (primitive can't be null at JVM level) |
| Works like an `Int` but type-safe | Compiler emits `Int` at bytecode level; IDE + type checker prevent mixing |

### Gotchas at depth

- **Boxing unpredictable in IDE:** IDE may show "no allocation" but conditional code paths might box unexpectedly (escape analysis visibility)
- **Equality comparisons:** `UserId(1) == UserId(1)` works, but comparing boxed instances uses identity not value (gotcha if persisting in collections)
- **Reflection:** Can't instantiate via reflection (class doesn't exist at runtime); use factory functions
- **Multi-platform:** Inline classes work on JVM; on Native/JS behavior differs (not always erased)

</details>

### PART G: Flow Operators — When to Use

> **TL;DR:** Flow operators transform/combine streams. Each choice reflects a design decision: serial vs parallel, buffer vs backpressure, cancellation vs completion.

`flatMapConcat` serial · `flatMapMerge` parallel · `flatMapLatest` cancels · `debounce` + `throttle` rate-limit

| Operator | Decision | When | Example |
|---|---|---|---|
| **`flatMapConcat`** | Sequential, waits for each | Depends on order | User ID → profile → posts |
| **`flatMapMerge(N)`** | N parallel, emits as ready | Independent, limited concurrency | Download 4 images in parallel |
| **`flatMapLatest`** | Cancel old on new input | Search/autocomplete | New query cancels prev search |
| **`buffer(N)`** | Producer ahead, doesn't suspend | Fast producer, slow consumer | Network (fast) → UI (slow) |
| **`conflate()`** | Drop intermediate, keep latest | Only final state matters | Position flow → render |
| **`debounce(ms)`** | Wait after silence, emit latest | Search input (wait for user stop) | Wait 300ms → emit query |
| **`throttle(ms)`** | Emit max once per interval | Prevent spam | Click flow (1 per 500ms) |
| **`distinctUntilChanged()`** | Skip if same as previous | Avoid redundant work | User ID unchanged → skip fetch |

<details>
<summary>🔩 Under the Hood</summary>

### How each operator manipulates the stream

**`flatMapConcat` (sequential):**
```kotlin
// Pseudocode: waits for inner Flow to complete
outer.flatMapConcat { x -> inner(x) }

// Emission order: guaranteed ordered
// Backpressure: if inner is slow, outer suspends (waits)
```

**`flatMapMerge(concurrency=4)` (parallel with limit):**
```kotlin
// Pseudocode: runs up to 4 inner Flows simultaneously
outer.flatMapMerge(4) { x -> inner(x) }

// Emission order: as they complete (not guaranteed order)
// Backpressure: collects results, can buffer if consumer slow
```

**`flatMapLatest` (cancellation):**
```kotlin
// Pseudocode: cancels previous inner Flow on new outer value
outer.flatMapLatest { x -> inner(x) }

// When outer emits again:
// - Previous inner() coroutine is cancelled (Job.cancel())
// - New inner() starts
// Use case: search query changes → old search API call cancelled
```

**`debounce(ms)` + `throttle(ms)` (rate limiting):**
```kotlin
// debounce: waits for gap, emits latest
searchQuery.debounce(300).collect { query ->
    // Called only 300ms after user stops typing
}

// throttle: samples at fixed interval
clickFlow.throttle(500).collect { click ->
    // Called at most once per 500ms
}

// Compiler generates: Timer-based coroutine + delay() calls
```

### What it reuses & relies on

- **Coroutine scope** — each operator runs in collector's scope (lifetime tied to collect())
- **CoroutineContext** — dispatcher inherited from collector (Main/Default/IO)
- **Job hierarchy** — cancellation propagates down (child coroutines cancelled when parent cancelled)
- **Channel/buffer** — internal buffering for backpressure (FlowCollector implements buffered channel protocol)

### Why these designs were chosen

**Serial (`flatMapConcat`) vs Parallel (`flatMapMerge`):**
- Serial guarantees order; parallel maximizes throughput
- Parallel has concurrency limit (default depends on CPU count) to prevent resource exhaustion

**Cancellation (`flatMapLatest`) vs completion (`flatMapConcat`):**
- Cancellation is expensive (cancellation token, exception unwinding) but necessary for UI (search queries)
- Completion is cheap (just wait) but blocks producer

**Rate limiting (`debounce` vs `throttle`):**
- `debounce`: reactive (wait for silence) → ideal for input events (search, typing)
- `throttle`: periodic (fixed interval) → ideal for high-frequency events (scroll, mouse move)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| `flatMapLatest` cancels old search | Compiler inserts `currentJob?.cancel()` before launching new one; cancellation token propagates down |
| `debounce(300)` waits for silence | Uses Timer coroutine + delay(300); each new item resets timer |
| `conflate()` keeps latest | Internal buffer with size=1; new items overwrite pending item |
| `buffer(N)` decouples producer/consumer | Channel(capacity=N); producer emits into channel, collector drains independently |

### Gotchas at depth

- **`flatMapLatest` doesn't re-emit on cancel:** If search is cancelled mid-emission, no error emitted (unless explicitly handled in `catch { }`)
- **`debounce` with 0ms:** Still suspends once (delay(0) = yield to scheduler); not "no delay"
- **`buffer` overflow:** If capacity exceeded, behavior depends on BufferOverflow (SUSPEND, DROP_OLDEST, DROP_LATEST)
- **Dispatcher matters:** `debounce` uses default scheduler (can cause delays if Dispatcher.Main blocked); consider explicit dispatcher

</details>

**Practical decision tree:**
1. **Multiple independent values?** → `flatMapMerge(4)` (N parallel)
2. **Each depends on previous?** → `flatMapConcat` (sequential)
3. **Cancel on new input?** → `flatMapLatest` (search, autocomplete)
4. **Only latest matters?** → `conflate()` (UI rendering)
5. **Prevent rapid-fire?** → `debounce(300)` or `throttle(500)`

**Example: Search autocomplete (interview pattern):**
<details>
<summary>💻 Code Example</summary>

```kotlin
val searchQuery = MutableStateFlow("")
val results: Flow<List<Item>> = searchQuery
    .debounce(300)  // Wait for user to stop typing
    .distinctUntilChanged()  // Skip if unchanged
    .flatMapLatest { query ->
        if (query.isEmpty()) flowOf(emptyList())
        else api.search(query)
            .onStart { emit(emptyList()) }  // Loading state
    }
    .catch { emit(emptyList()) }  // Error → empty
```

</details>

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

## 5. Dependency Injection (DI)

### Hilt vs Dagger vs Koin

> **TL;DR:** Hilt = Android standard (codegen). Dagger = legacy (complex). Koin = KMP-friendly (runtime reflection). For 2026: Hilt if Android-only, Koin if KMP, kotlin-inject if lightweight.

`Hilt` standard · `Dagger` legacy · `Koin` KMP · `Codegen vs runtime` · `Compile-safety vs flexibility`

| Feature | Hilt | Dagger | Koin |
|---|---|---|---|
| **Setup** | `@HiltAndroidApp` + annotations | Manual Dagger components | DSL block |
| **Code generation** | KSP (compile-time) | KSP (compile-time) | Runtime reflection |
| **Android lifecycle scopes** | ✅ Built-in | ❌ Manual | ✅ androidContext |
| **KMP support** | ❌ Android only | ❌ JVM only | ✅ Full KMP |
| **Compile-safety** | ✅ Missing bindings = error | ✅ Missing bindings = error | ⚠️ Runtime error (call verify()) |
| **Performance** | Fast (generated code) | Fast (generated code) | Moderate (reflection) |

**Emerging options:** Metro (compile-time KMP), kotlin-inject (lightweight KSP-based).

<details>
<summary>💻 Code Example</summary>

```kotlin
// Hilt (standard for Android)
@HiltAndroidApp
class App : Application()

@AndroidEntryPoint
class MainActivity : AppCompatActivity()

// Koin (KMP projects)
startKoin {
    modules(appModule)
}

val viewModel: SearchViewModel by viewModel()
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Hilt: KSP codegen pipeline

**Compilation phases:**
```
1. Annotation processing: @HiltAndroidApp, @AndroidEntryPoint, @Module scanned
2. KSP plugin: Generates Dagger components + injection factories
3. Generated files: HiltComponents.java (component interfaces), ViewModel_Factory, etc.
4. Linking: build combines generated code with compiled sources
```

**Generated code (simplified):**
```java
// Input:
@HiltAndroidApp
class MyApp : Application()

// Generated:
class Hilt_MyApp extends MyApp {
    private GeneratedComponent component;

    public void onCreate() {
        super.onCreate();
        component = DaggerGeneratedComponent.builder().app(this).build();
    }
}
```

### Dagger: Manual component graph

**Explicit dependency graph:**
```kotlin
@Component(modules = [NetworkModule::class])
interface AppComponent {
    fun inject(activity: MainActivity)
}

// Build explicitly:
val component = DaggerAppComponent.create()
component.inject(mainActivity)
```

**Problem:** Verbose. Every component, module, scope must be wired by hand.

### Koin: Runtime reflection

**Module definition:**
```kotlin
val appModule = module {
    single { OkHttpClient() }  // Single instance
    single { Retrofit.Builder().client(get()).build() }  // get() = resolve OkHttpClient
    factory { UserRepository(get()) }  // New instance each time
}

startKoin { modules(appModule) }
```

**At runtime:**
- Koin scans module, builds object graph via reflection
- `get()` = look up binding by type + qualifier
- Lazy initialization: bindings created on first request

**Gotcha: no compile-time safety**
```kotlin
factory { UserRepository(get()) }  // ❌ If OkHttpClient not registered, error happens at runtime (first use)
// Mitigation: koin.verify() at app start to catch early
```

### What each reuses

**Hilt:**
- Dagger library (Hilt is wrapper, generates Dagger components)
- KSP (compiler plugin interface)
- Android lifecycle components (for scoped bindings)

**Dagger:**
- JSR 330 (javax.inject standard interfaces)
- Compile-time APT (code generation)

**Koin:**
- Kotlin reflection API (runtime type inspection)
- Coroutine scope integration (for lifecycle-aware singletons)

### Why these designs were chosen

**Hilt = Dagger simplified:**
- Dagger powerful but boilerplate-heavy
- Hilt pre-configures Android components (reducing decisions)
- Standard Android recommendation (Google, Google Play plugins)

**Dagger = explicit graph:**
- Before Java 5 annotations → components were wiring code
- Still used in legacy/complex projects with many dynamic bindings

**Koin = developer friction reduction:**
- DSL more readable than annotation chains
- Reflection cost acceptable for most apps
- KMP support (only option for commonMain)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| Hilt uses KSP | Hilt plugin + KSP = generates Dagger components at compile time (no runtime cost) |
| Koin resolves types via `get()` | Koin uses Kotlin reflection to look up bindings by type + qualifier at runtime |
| "Hilt scopes" = Android components | Hilt maps @ViewModelScoped to ViewModelComponent, which Dagger manages (tied to ViewModel lifecycle) |
| Dagger is "manual" | Explicit: you write components, modules, @Provides functions. Hilt generates these. |

### Gotchas at depth

- **Hilt + Dagger conflict:** If project already uses Dagger, adding Hilt can cause double-generation (duplicate bindings). Requires migration.
- **Koin verify() false sense of safety:** `verify()` finds unused bindings but not type mismatches (Kotlin reflection doesn't catch `get<String>` when String not bound).
- **Android plugin requirement:** Hilt requires `com.google.dagger:hilt-android-gradle-plugin`. Forget it = cryptic "Hilt not found" errors.
- **Metro/kotlin-inject immaturity:** Emerging alternatives (2025+) but not battle-tested like Hilt (use if starting fresh KMP).

</details>

### Hilt Component Hierarchy

> **TL;DR:** Component = Dagger component scoped to Android lifetime (Application, Activity, Fragment, ViewModel). Hierarchy determines when bindings are created/destroyed.

`SingletonComponent` app-life · `ViewModelComponent` screen-life · `ActivityComponent` activity-life · `Scoped binding` · `Lifetime management`

| Component | Scope Annotation | Lifetime | Use For |
|---|---|---|---|
| `SingletonComponent` | `@Singleton` | Application | API clients, databases, preferences |
| `ActivityRetainedComponent` | `@ActivityRetainedScoped` | Survives config change | Shared ViewModel state |
| `ViewModelComponent` | `@ViewModelScoped` | ViewModel lifetime | Repository, use cases tied to screen |
| `ActivityComponent` | `@ActivityScoped` | Activity lifetime | Activity-specific (rare) |
| `FragmentComponent` | `@FragmentScoped` | Fragment lifetime | Fragment-specific (rare) |

<details>
<summary>💻 Code Example</summary>

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object ApiModule {
    @Provides
    @Singleton
    fun provideApiService(): ApiService = Retrofit.Builder().build()
}

@Module
@InstallIn(ViewModelComponent::class)
object RepositoryModule {
    @Provides
    fun provideUserRepo(api: ApiService): UserRepository = UserRepositoryImpl(api)
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Dagger component graph & scoping

**Component hierarchy (Dagger):**
```
SingletonComponent (root)
  ├── ActivityRetainedComponent (survives rotation)
  ├── ViewModelComponent (per-ViewModel)
  └── ActivityComponent (per-Activity)
       └── FragmentComponent (per-Fragment)
```

**Scope enforcement:**
```kotlin
@Singleton  // Only in SingletonComponent
fun provideDb(): Database = Database()

@ViewModelScoped  // Only in ViewModelComponent + children (ActivityComponent, FragmentComponent)
fun provideRepo(db: Database): UserRepository = UserRepositoryImpl(db)

// ❌ Error: ViewModelScoped binding can't be used in SingletonComponent
// (scope lifetime mismatch: ViewModel lives shorter than Singleton)
```

**Implicit scoping:** If function has no @Scope, it's **unscoped** (new instance each injection).

### Lifetime management

**SingletonComponent:**
- Created once at app start (in HiltAndroidApp.onCreate())
- Destroyed when app killed
- All @Singleton bindings persist for app lifetime

**ViewModelComponent:**
- Created when ViewModel created (by Hilt)
- Destroyed when ViewModel cleared (onCleared())
- All @ViewModelScoped bindings scoped to that ViewModel

**FragmentComponent:**
- Created when Fragment created
- Destroyed when Fragment destroyed
- All @FragmentScoped bindings scoped to that Fragment

### What it reuses & relies on

- **ViewModel#onCleared()** — Hilt clears ViewModelComponent when ViewModel cleared
- **Activity lifecycle** — Hilt clears ActivityComponent on Activity destruction
- **Fragment lifecycle** — Hilt clears FragmentComponent on Fragment destruction
- **Dagger scoped provider** — generates SingletonHolder if @Singleton (thread-safe double-check locking)

### Why this hierarchy

**Problem:** If all bindings were Singleton, they'd persist even after Activity destroyed (memory leak).

**Solution:** Hierarchy allows scoped lifetimes:
- Short-lived (Fragment) bindings created per-fragment, destroyed with fragment
- Long-lived (Singleton) bindings created once, shared across all activities

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use @Singleton for expensive objects" | @Singleton = Dagger double-checked locking provider (thread-safe, one instance in memory) |
| "ViewModelScoped tied to ViewModel" | Hilt's ViewModelComponent linked to ViewModel.onCleared() callback (auto-cleanup when ViewModel cleared) |
| "Can't use ViewModelScoped in Singleton" | Scope mismatch: Singleton lives longer than ViewModel. If Singleton held ViewModel-scoped instance, leak after ViewModel cleared. |
| "Fragment bindings are unscoped" | If no @FragmentScoped on binding, each injection call gets new instance (no caching) |

### Gotchas at depth

- **ActivityRetainedComponent confusion:** Doesn't survive Fragment transactions (only config changes). Easy to misuse for "keep-alive" logic.
- **Scope lifetime leaks:** If Singleton binding holds reference to Activity-scoped binding, Activity can't GC (common bug).
- **No parent scope injection:** Child component can't inject from parent (design choice). Must explicitly pass via constructor.
- **Unscoped overhead:** If binding is unscoped, each inject() call constructs new instance (no caching). Can be performance issue if constructor expensive.

</details>

### Hilt Modules: @Provides vs @Binds

> **TL;DR:** `@Provides` = factory function (custom logic). `@Binds` = simple wrapper (impl to interface). Use Binds when no logic needed (less generated code).

`@Provides` factory · `@Binds` wrapper · `Abstract modules` · `Code generation` · `When each`

<details>
<summary>💻 Code Example</summary>

```kotlin
// @Binds: delegation (no custom logic)
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    @Singleton
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
}

// @Provides: factory (custom logic)
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideRetrofit(httpClient: OkHttpClient): Retrofit =
        Retrofit.Builder().client(httpClient).build()
}
```

</details>

| Pattern | Use | Generated Code Size |
|---|---|---|
| `@Binds` | Impl → Interface, no logic | Small (delegation only) |
| `@Provides` | Factory, custom initialization | Larger (logic included) |

**Rule of thumb:** Binds for repository/simple implementations, Provides for complex factories (Retrofit, database builders).

<details>
<summary>🔩 Under the Hood</summary>

### Generated factory classes

**What you write:**
```kotlin
@Binds
@Singleton
abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
```

**Generated code (simplified):**
```java
public class RepositoryModule_BindUserRepositoryFactory implements Factory<UserRepository> {
    private final UserRepositoryImpl impl;

    public RepositoryModule_BindUserRepositoryFactory(UserRepositoryImpl impl) {
        this.impl = impl;
    }

    public UserRepository get() {
        return impl;  // Simple wrapper
    }
}
```

**What you write:**
```kotlin
@Provides
@Singleton
fun provideRetrofit(httpClient: OkHttpClient): Retrofit =
    Retrofit.Builder().client(httpClient).build()
```

**Generated code (simplified):**
```java
public class NetworkModule_ProvideRetrofitFactory implements Factory<Retrofit> {
    private final OkHttpClient httpClient;

    public NetworkModule_ProvideRetrofitFactory(OkHttpClient httpClient) {
        this.httpClient = httpClient;
    }

    public Retrofit get() {
        return NetworkModule.provideRetrofit(httpClient);  // Calls your function
    }
}
```

### Binding key resolution

**How Dagger matches dependencies:**
```kotlin
fun provideRetrofit(httpClient: OkHttpClient): Retrofit
// Key = (Retrofit, no qualifier)
// When injecting Retrofit, Dagger looks up this key

@Provides
@Named("baseUrl")
fun provideBaseUrl(): String = "https://..."
// Key = (String, qualifier="baseUrl")
// When injecting @Named("baseUrl") String, Dagger looks up this specific key
```

**Binding precedence:**
1. Scoped binding (@Singleton, @ViewModelScoped, etc.)
2. Unscoped binding
3. If ambiguous → compilation error

### Module installation

**@InstallIn:**
```kotlin
@Module
@InstallIn(ViewModelComponent::class)  // This module's bindings available in ViewModelComponent
object RepositoryModule {
    @Provides
    fun provideUserRepository(): UserRepository = UserRepositoryImpl()
}

// Dagger generates:
class DaggerViewModelComponent implements ViewModelComponent {
    // Installs RepositoryModule's bindings
    private final RepositoryModule repositoryModule = new RepositoryModule();
}
```

### What it reuses & relies on

- **Dagger annotation processing** — @Provides/@Binds triggers factory generation
- **KSP** — generates factory classes at compile time
- **Java generics** — Factory<T> is parameterized interface

### Why @Binds vs @Provides

**@Binds optimization:**
- Smaller generated code (just delegation)
- Compiler can inline better (less function indirection)
- Cleaner intent (user just wrapping impl in interface)

**@Provides necessity:**
- Custom logic (can't just delegate)
- Multiple instances (e.g., @Named qualifiers)
- Complex initialization

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use @Binds for simple wrapping" | @Binds generates minimal factory code; @Provides includes your function logic in factory |
| "Qualifiers distinguish same types" | @Named, @Qualifier are binding keys; Dagger matches String + @Named("url") separately from plain String |
| "@Provides receives dependencies" | Function parameters are injected by Dagger (provideRetrofit(httpClient) → httpClient auto-injected) |
| "Abstract modules with @Binds" | @Binds requires abstract function (no implementation); Dagger generates impl (factory). @Provides requires concrete object. |

### Gotchas at depth

- **Binding shadowing:** If two modules provide same type without qualifier, build fails (ambiguous). Qualifiers (@Named, custom) required to distinguish.
- **Circular dependencies:** If RepositoryA depends on RepositoryB and vice versa (rare), Dagger detects and errors. Use lazy injection (Provider<T> instead of T) to break cycle.
- **Missing @Singleton on Provides:** If @Provides fun createDb() doesn't have @Singleton, new Database created every injection (often unintended).
- **Module duplication:** If @Module installed twice (rare), bindings duplicated (cryptic error). Ensure @InstallIn components don't overlap.

</details>

**Entry Points** = inject into non-injectable classes (Application, custom services). Rare in modern Compose apps.

<details>
<summary>💻 Code Example</summary>

```kotlin
@EntryPoint
@InstallIn(SingletonComponent::class)
interface AnalyticsEntryPoint {
    fun analytics(): Analytics
}

// Use when Hilt can't auto-inject (e.g., Application onCreate)
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        val entryPoint = EntryPoints.get(this, AnalyticsEntryPoint::class.java)
        entryPoint.analytics().init()
    }
}
```

</details>

**Scope selection:**
- **Singleton:** Expensive, app-wide (API, database)
- **ViewModelScoped:** Per-screen (repository, use case)
- **ActivityScoped/FragmentScoped:** Rare; only if truly activity/fragment-specific

### Manual DI — Constructor Injection without Framework

> **TL;DR:** Hand-written AppContainer with constructor injection. No codegen overhead, fully transparent. Scales to ~50 classes comfortably; beyond that, framework (Hilt/Koin) helps. Best for KMP shared code.

`Constructor injection` · `AppContainer` · `Zero magic` · `Fully KMP` · `Simple, scales ~50 classes`

<details>
<summary>💻 Code Example</summary>

```kotlin
// commonMain
interface UserRepository { suspend fun getUser(id: Int): User }
class UserRepositoryImpl(val api: ApiService) : UserRepository

// Shared AppContainer
class AppContainer(val api: ApiService) {
    val userRepository: UserRepository = UserRepositoryImpl(api)
    val userUseCase = GetUserUseCase(userRepository)
    val viewModelFactory = SearchViewModelFactory(userUseCase)
}

// androidApp
val container = AppContainer(OkHttpApiService())
val viewModel = container.viewModelFactory.create()
```

</details>

| Approach | Setup | Overhead | KMP | Scales |
|---|---|---|---|---|
| **Manual DI** | Hand-written | None | ✅ | ~50 classes |
| **Hilt** | Annotations | KSP codegen | ❌ Android-only | 1000+ |
| **Koin** | DSL | Runtime reflection | ✅ | 500+ |

<details>
<summary>🔩 Under the Hood</summary>

### Object graph construction

**Graph at runtime:**
```
AppContainer
├── ApiService (OkHttpApiService)
├── UserRepository (UserRepositoryImpl <- ApiService)
├── GetUserUseCase (GetUserUseCase <- UserRepository)
└── ViewModelFactory (SearchViewModelFactory <- GetUserUseCase)

// When requesting viewModel:
container.viewModelFactory.create()
  → SearchViewModelFactory(GetUserUseCase(...))
    → GetUserUseCase(UserRepositoryImpl(ApiService))
```

**Manual vs Framework:**
```kotlin
// Manual: explicit construction order
val container = AppContainer(
    api = createApi(),  // Step 1
    repo = UserRepositoryImpl(api),  // Step 2
    useCase = GetUserUseCase(repo),  // Step 3
    viewModel = SearchViewModel(useCase)  // Step 4
)

// Hilt: implicit (codegen handles order)
class SearchViewModel @Inject constructor(useCase: GetUserUseCase)  // Dagger figures out GetUserUseCase deps
```

### Constructor injection pattern

**Principle:** Dependencies passed via constructor (no setters, no service locator).

**Example:**
```kotlin
class UserRepositoryImpl(
    private val api: ApiService,  // Constructor injection
    private val cache: UserCache  // All deps passed in
) : UserRepository { }

// Usage:
val repo = UserRepositoryImpl(
    api = OkHttpApiService(),
    cache = InMemoryUserCache()
)
```

**Benefits:**
- All dependencies visible in constructor (inspectable)
- Testable (pass mocks in constructor)
- Immutable (no runtime changes to deps)

**Drawback:** If dependency tree is deep (50+ classes), manual wiring becomes tedious.

### Lazy initialization pattern (for circular deps)

```kotlin
class AContainer {
    val serviceA = ServiceA(lazy { serviceB })  // Lazy<ServiceB>
    val serviceB = ServiceB(lazy { serviceA })
}

// At runtime:
// serviceA gets lazy reference to serviceB
// Only resolved when accessed (lazy.value)
// Avoids circular construction
```

### What it reuses & relies on

- **Kotlin delegation** — can use delegation patterns for optional deps
- **Lazy<T>** — enables lazy initialization and circular dep breaking
- **Visibility modifiers** — package-private constructor can enforce DI (no public ctors)
- **Interfaces** — enables swapping implementations (test doubles, production)

### Why this design chosen

**Motivation:**
- No framework overhead → works on all Kotlin targets (JVM, Native, JS, WASM)
- Fully transparent (no code generation) → easy to debug
- KMP support (frameworks lag)

**Scalability tradeoff:**
- <20 classes: Manual DI is simpler than Hilt boilerplate
- 20-50 classes: Manual DI acceptable but boilerplate noticeable
- >50 classes: Framework (Hilt/Koin) worth investment (auto-wiring saves ~30% boilerplate)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Constructor injection = pass deps in" | Constructor param order matters (not really); dependencies are just function arguments (no magic) |
| "AppContainer is app graph" | AppContainer is hand-written factory; instantiating AppContainer walks entire dependency tree (all objects created eagerly) |
| "Manual DI works on KMP" | No Android-specific annotations; object construction is pure Kotlin (works on all targets) |
| "Pass mocks in constructor for testing" | Tests can pass different implementation in constructor (e.g., FakeUserRepository). No reflection or service locator needed. |

### Gotchas at depth

- **Eager initialization:** Manual container creates all objects when instantiated (not lazy). If AppContainer has 100 classes, all created upfront (can be slow). Mitigation: use Lazy<T> or factory functions.
- **Missing dep error:** If you forget to add a dependency, constructor call fails at runtime with ParameterMismatchException (caught early if running tests, but not by compiler).
- **Circular deps without Lazy:** If ServiceA needs ServiceB and vice versa, constructor fails (StackOverflow). Must use Lazy<T> or factory functions to break cycle.
- **No validation:** Unlike Hilt/Koin, no "verify all bindings" check. If you wire incorrectly, only found when code path executed.

</details>

**When manual DI makes sense:**
- Small modules/libraries (<30 classes)
- KMP shared code (no Hilt support)
- Onboarding (zero framework learning curve)
- Debugging (explicit construction order)

**When framework needed:**
- >50 classes (boilerplate burden too high)
- Complex scoping rules (Android lifecycle tiers)
- Large teams (consistency enforcement)

---

## 6. Memory & Performance

### 3 Common Memory Leaks (With Detection)

> **TL;DR:** Memory leak = object retained when should be garbage collected. Usually: Activity retained after back navigation. Top causes: wrong coroutine scope, lambda capturing context, unregistered listeners.

`GlobalScope` × Activity · `Callback captures context` · `Unregistered listeners` · `LeakCanary detection` · `GC root chain`

| Leak | Cause | Fix |
|---|---|---|
| **GlobalScope + Activity** | GlobalScope outlives Activity | Use viewModelScope, lifecycleScope |
| **Compose remember captures context** | Lambda captures `this@Activity` | Use rememberUpdatedState, pass data only |
| **Unregistered listeners** | Framework holds strong ref | Unregister in onStop(), use repeatOnLifecycle |

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ Leak: GlobalScope outlives Activity
GlobalScope.launch {
    val data = loadData(activity)  // activity ref held
    updateUI(data)  // Called after Activity destroyed!
}

// ✅ Fix: viewModelScope tied to Activity lifetime
viewModelScope.launch {
    val data = loadData()  // Activity ref not needed
    updateUI(data)  // Safe: scope cleared on ViewModel cleared
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### GC root graph traversal

**Leak mechanism (simplified):**
```
GC Root (static field)
  ↓ (strong reference)
GlobalScope.launch (Job)
  ↓ (closure capture)
lambda { updateUI(activity) }
  ↓ (implicit this)
Activity (trapped!)
  ↓ (references)
Fragment, View, ViewModel
    (all trapped, can't GC)

Result: Activity + all children retained indefinitely
```

**Memory Profiler inspection:**
```
Retained Objects: Activity
  └─ Fragment (still referenced by Activity)
     └─ ViewModel (still referenced by Fragment)
        └─ GlobalScope job (still scheduled)
           └─ Closure (captured Activity)
```

### LeakCanary detection

**What it does:**
1. On suspected leak (Activity destroyed but ref still held):
2. Force GC, dump heap to .hprof file
3. Parse heap: find shortest path from GC root to suspected object
4. Print chain: "App → GlobalScope job → closure → Activity"

**Root causes LeakCanary finds:**
- Static fields (never eligible for GC)
- Thread objects (threads live until thread exits)
- Thread-local storage (if thread pool reused, TLS persists)
- Service callbacks (if service not stopped)

### Compose `remember` with context capture

**Problem:**
```kotlin
@Composable
fun MyScreen(activity: Activity) {  // Shouldn't need activity here!
    val callback = remember {
        { Toast.makeText(activity, "Clicked", Toast.LENGTH_SHORT).show() }  // Captures activity
    }
    Button(onClick = callback) { Text("Click") }
}

// Recomposition lifecycle:
// 1. Composable called with activity ref
// 2. remember block creates callback (captures activity)
// 3. Callback stored in Composition (in-memory tree)
// 4. If Composition held after Activity destroyed, activity trapped
```

**Solution: rememberUpdatedState**
```kotlin
@Composable
fun MyScreen() {
    val context = LocalContext.current  // Compose context, safe
    val message = rememberUpdatedState("Clicked")  // Updated on recomposition, no capture
    val callback = remember {
        { Toast.makeText(context, message.value, Toast.LENGTH_SHORT).show() }  // No closure over mutable state
    }
}
```

### Listener registration pattern

**Old (error-prone):**
```kotlin
override fun onStart() {
    super.onStart()
    context.registerReceiver(receiver, filter)  // ❌ Easy to forget unregister
}

override fun onDestroy() {
    super.onDestroy()
    // ❌ If onPause called before onDestroy, receiver still registered (onPause → onStop → onDestroy)
    context.unregisterReceiver(receiver)
}
```

**New (safe):**
```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {  // Automatically managed
        context.registerReceiver(receiver, filter)  // Registered at onStart
        // Unregistered at onStop (not onDestroy — safer)
    }
}
```

### What it reuses & relies on

- **GC root** — thread stacks, static fields, JNI references (where GC traversal starts)
- **Reachability** — object can be GC'd if unreachable from any GC root
- **Strong/weak references** — weak refs don't prevent GC (used for caches)
- **Lifecycle awareness** — lifecycleScope automatically cancelled when lifecycle destroyed

### Why these leaks happen

**GlobalScope:**
- Intentionally long-lived (global app duration)
- Designed for fire-and-forget (bad for Activity-scoped work)
- No automatic cleanup (must manually cancel Job)

**Closure capture:**
- Lambdas implicitly capture `this` (convenience, but risk)
- Stored in remember cache (persists across recompositions)
- If composable cached after Activity destroyed, leak

**Listeners:**
- Framework holds strong ref (by design)
- onDestroy not guaranteed in all lifecycle paths (especially rotation)
- Must unregister in onStop (called before onDestroy reliably)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "GlobalScope is bad for Activity" | GlobalScope.launch creates Job that outlives Activity. Closure captures Activity ref. Job stored in global registry (never cleared). |
| "Use viewModelScope instead" | viewModelScope = CoroutineScope(Job + Dispatchers.Main). Job cancelled in ViewModel.onCleared() → Activity GC-eligible. |
| "Remember captures context" | Remember stores closure in Composition tree (in-memory). If Composition retained after Activity destroyed, closure retained → activity retained. |
| "Listeners leak if not unregistered" | Framework stores listener in list. If Activity destroyed but listener still in list, Activity can't GC (strong ref from listener to Activity). |

### Gotchas at depth

- **Rotation = onDestroy/onCreate:** On config change, Activity destroyed + recreated. If GlobalScope job still holding ref to old Activity, new Activity created but old Activity trapped (two activities in memory).
- **Listener weak refs:** Some frameworks use WeakReference for listeners (safe), but not all. Always unregister manually unless docs guarantee weak ref.
- **rememberUpdatedState overhead:** rememberUpdatedState creates wrapper object. For frequently-changing state, use composition tree to pass values instead.
- **TLS in coroutines:** If coroutine launches on thread pool that's reused (Dispatchers.Default), thread-local variables might leak if not cleaned up.

</details>

### GC Root — How Objects are Kept Alive

> **TL;DR:** GC Root = starting point for reachability traversal. Thread stacks, static fields, JNI refs are always roots. Anything reachable from a root stays alive.

`GC Root` always alive · `Thread stacks` · `Static fields` · `JNI references` · `Reachability chains`

**Root types (never collected):**
- **Thread stacks:** Local variables in running threads
- **Static fields:** Class-level vars (single per app)
- **JNI references:** C++ refs to Java objects
- **Monitor objects:** Locks held in synchronized blocks
- **Interned strings:** String pool

**Objects trapped (reachable from root):**
<details>
<summary>💻 Code Example</summary>

```
GC Root (thread stack)
  ↓ Local var: GlobalScope job (strong ref)
  ↓ Closure captures: Activity
    ↓ Field: Fragment
      ↓ Field: View
        ↓ (all trapped — can't GC)
```

</details>

**Detection workflow:**

| Tool | What it does | Use when |
|---|---|---|
| **LeakCanary** | Auto-detects Activity leaks, dumps heap, finds GC root chain | Suspect leak in Activity back nav |
| **Memory Profiler** | Manual heap dump, object count, retained size | Investigating specific object |
| **adb shell dumpsys meminfo** | System memory stats (not object-level) | Checking overall memory pressure |

<details>
<summary>🔩 Under the Hood</summary>

### JVM Generational GC vs ART

**JVM Generational GC (Android API <28, legacy):**
```
Heap divided into:
  - Young Gen (70%): Objects aged <1s, collected frequently (fast)
  - Old Gen (30%): Long-lived objects, collected rarely (slow)

Allocation → Young Gen
  ↓ (if survives 1-2 young gen collections)
  ↓ (promoted to Old Gen)
Happens: O(1) marking, but full GC stalls

Leak impact:
  - Young gen leak (e.g., Activity in cache): cleared quickly (minor GC)
  - Old gen leak (e.g., static field): not cleared until full GC (rare)
```

**ART (Art Runtime, Android API 28+):**
```
Generational concurrent mark sweep:
  - Young collection: concurrent (doesn't stop threads)
  - Old collection: less frequent, can be concurrent

Heap stats:
  - More efficient GC (less pause time)
  - Leak detection same (object reachability = key)

Leak impact:
  - Same retention logic
  - But pause times shorter (better UX)
```

### Heap dump format (.hprof)

**Binary format parsed by LeakCanary:**
```
[Object instances]
  - Instance ID
  - Class pointer
  - Field values (field offsets, types)

[GC roots]
  - Thread stack roots
  - Static field roots
  - JNI refs

[References between objects]
  - Object A → Object B (field reference)
  - Object A → Array Object B[i] (array element)
```

**Shortest path algorithm:**
```
BFS from suspected object → find shortest chain to any GC root
  Activity (under test) → Fragment → ViewModel → Job → Activity (cycle)
  Print: "Leak found. GC root chain: Job(GlobalScope) → Activity"
```

### Strong vs Weak Reference Queues

**Strong reference:**
```kotlin
var ref: Activity = activity
// Activity trapped (reachable from local var)
// GC can't collect even if Activity.destroy() called
```

**Weak reference (doesn't prevent GC):**
```kotlin
val weakRef = WeakReference(activity)
// activity eligible for GC even if weakRef still exists
// After GC: weakRef.get() returns null
```

**Reference queue (for cleanup):**
```kotlin
val refQueue = ReferenceQueue<Activity>()
val weakRef = WeakReference(activity, refQueue)

// After GC collects activity:
val ref = refQueue.poll()  // Returns weakRef
// Notification that activity was collected
```

**Soft reference (cached objects):**
```kotlin
val softRef = SoftReference(bitmap)
// Collected only if memory pressure critical (LRU cache)
// Survives normal GC collections
```

### What it reuses & relies on

- **Concurrent mark-sweep algorithm** — walks reachability graph, marks live objects
- **Write barriers** — track object reference changes for concurrent GC
- **Card marking** — divide heap into "cards," track which old objects reference young objects
- **Thread park/resume** — STW (Stop-The-World) collections pause all threads briefly

### Why these designs were chosen

**Generational approach:**
- Observation: Most objects die young (temporary allocations)
- Collect young gen frequently (fast, small)
- Collect old gen rarely (expensive, large)
- Result: Lower average pause time

**ART over Dalvik:**
- Dalvik: JIT compilation (slow startup, unpredictable)
- ART: AOT + JIT hybrid (fast startup, predictable)
- Both use same generational GC concepts

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "GC Root determines if object stays alive" | GC traverses from roots (static/stack), marks reachable objects, sweeps unmarked. Unreachable from root = eligible for collection. |
| "WeakReference doesn't prevent GC" | WeakReference bypasses reachability check (not followed during GC traversal). Weak refs survive even after object GC'd. |
| "Heap dump shows all objects" | .hprof file is snapshot at point-in-time. Includes all object instances + field values + GC roots + reference graph. |
| "LeakCanary detects retained Activity" | After Activity.destroy(), LeakCanary polls Activity objects. If still in heap after GC, finds shortest chain to GC root (usually GlobalScope job). |

### Gotchas at depth

- **False positives in LeakCanary:** Some frameworks intentionally cache Activity (e.g., for resources). LeakCanary flags as leak, but actually safe if bounded. Can suppress via `@SuppressLint("DiscouragedPrivateApi")` or custom matchers.
- **Heap dump size:** Large app heaps (300+ MB) create huge .hprof files. Analyzing on slow machine can take minutes.
- **WeakReference timing:** After GC collects object, WeakReference.get() returns null **immediately next call**. Small window between collection and notification.
- **Static field leaks:** If static field holds Activity, leak is permanent (static never GC'd). Only way to fix: null out static field explicitly, or clear in app shutdown.

</details>

### Compose Recomposition — Smart Re-execution

> **TL;DR:** Recomposition = re-run composable when inputs change. Composition tree caches state via `remember`. Compiler skips unchanged branches (strong skipping). Use stable types to enable skipping.

`Recomposition` only affected nodes · `Composition tree` in memory · `Strong skipping` compiler analysis · `Stable types` enable optimization

<details>
<summary>💻 Code Example</summary>

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableIntStateOf(0) }  // Persisted in Composition
    Button(onClick = { count++ }) { Text("$count") }
}
// Parent recomposes → Counter re-executes
// but remember block returns cached mutableIntStateOf(0) (same object)
// count value preserved across recompositions
```

</details>

| Optimization | What it does | Enables |
|---|---|---|
| **`remember`** | Cache object in Composition tree, keyed by position | State persistence across recompositions |
| **`derivedStateOf`** | Only trigger recomp if result value changes, not intermediate | Filter/transform without cascading |
| **Strong skipping** | Skip composable if all params stable | Child skip parent recomposition |
| **State hoisting** | Move state up, pass as params + lambdas down | Composable reusability + testing |

<details>
<summary>🔩 Under the Hood</summary>

### Composition slot table

**In-memory tree structure:**
```
Composition (in-memory tree)
├── Node: Counter @Composable
│   ├── Slot 0: mutableIntStateOf(5)  // remember value, keyed by position
│   ├── Node: Button
│   │   ├── onClick = { count++ }
│   │   └── Node: Text
│   │       └── Slot 0: "5"
```

**Recomposition process:**
```
1. State change: count = 6
2. Composition tree notified: Counter needs recomposition
3. Counter re-executes
4. remember block: looks up Slot 0 in tree
   - Key = (composable id, position, type)
   - Found in tree: returns cached MutableState<Int> (same object!)
5. count is still same MutableState object, but value changed to 6
6. Button and Text re-execute (because they're inside Counter)
7. Compiler checks: Button's params changed? Text's params changed?
   - If yes: recompose
   - If no: skip (strong skipping)
```

### Smart recomposition algorithm

**Dependency tracking:**
```kotlin
@Composable
fun SearchResults(query: String, items: List<Item>) {
    val filteredItems = derivedStateOf { items.filter { it.name.contains(query) } }
    // Depends on: query, items
    // Produces: filteredItems (state)

    LazyColumn {
        items(filteredItems.value) { item ->  // Only recompose if filteredItems changed
            ResultItem(item)  // Skip if item identity unchanged
        }
    }
}

// If items reordered but filteredItems same: LazyColumn skips
// If query changed but no matches: filteredItems same, LazyColumn skips
```

**Without derivedStateOf (inefficient):**
```kotlin
val filteredItems = items.filter { it.name.contains(query) }  // New list every recomposition!
// Every parent recomposition → new list instance → LazyColumn sees new param → full recompose (cascade)
```

### Strong skipping compiler pass

**Compiler analysis (Kotlin 2.0.20+):**
```
@Composable
fun Child(name: String, count: Int) {  // Params: all stable types
    Text(name)
    Text(count.toString())
}

// Compiler marks: skippable=true
// Why? name is String (stable), count is Int (stable)
// If parent recomposes but passes same name + count → skip Child entirely
```

**Stability inference:**
```kotlin
// Stable: data classes with all stable fields
data class Item(val id: Int, val name: String)  // Both fields stable

// Unstable: mutable interface
List<String>  // Mutable, compiler can't guarantee it's immutable

// Unstable: generic without bounds
class Container<T>  // T could be mutable type

// Solution: use immutable library
ImmutableList<String>  // From kotlinx-collections-immutable, marked stable
```

**Check compiler metrics:**
```bash
./gradlew debugComposeCompilerMetrics
# Output: app/build/compose_compiler_metrics/ComposableMetrics.txt
# Shows: composable name, skippable=true/false, stability
```

### State hoisting pattern

**Stateful (un-reusable):**
```kotlin
@Composable
fun CounterScreen() {  // State internal
    var count by remember { mutableIntStateOf(0) }
    Button(onClick = { count++ }) { Text("$count") }
}
// Can't reuse, can't test, can't preview with different count values
```

**Stateless (reusable):**
```kotlin
@Composable
fun CounterScreen(count: Int, onCountChange: (Int) -> Unit) {  // State external
    Button(onClick = { onCountChange(count + 1) }) { Text("$count") }
}
// Reusable, testable, previewable
```

### What it reuses & relies on

- **Composition tree** — in-memory Compose IR (not Kotlin AST, but runtime structure)
- **Compiler plugin** — analyzes code, generates skipping logic, infers stability
- **Kotlin reflection** — stability inference uses type information
- **State management** — MutableState<T> tracks observers, notifies on change

### Why this design was chosen

**Problem (naive recomposition):**
- Every state change → recompose entire tree
- Result: O(n) expensive recompositions

**Solution (smart recomposition):**
- Only affected subtrees recompose (O(1) if dependency tree shallow)
- Compiler analysis finds skippable branches (no manual annotation)
- State hoisting decouples state from UI (enables testing, previewing)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "remember persists state" | remember stores MutableState<T> in Composition tree slot (keyed by position). Recomposition retrieves same slot → same object → value persisted. |
| "derivedStateOf prevents cascading" | derivedStateOf creates separate state, only notifies dependents if value changes (not intermediate values). Breaks dependency chain. |
| "Strong skipping = skip child" | Compiler generates skipping code: `if (params changed) recompose(); else skip()`. Analyzer marks skippable if all params stable. |
| "Stable types enable skipping" | Compiler trusts stable types won't change unexpectedly. List<T> unstable (mutable), ImmutableList<T> stable (immutable). |

### Gotchas at depth

- **Position-based keys:** remember uses composable position as key (not content). If remember moves (different position in tree), gets different slot → state lost. Rare but confusing.
- **Stability overrides:** Can mark class @Stable or @Immutable to override compiler inference (sometimes needed for external libraries marked unstable).
- **derivedStateOf overhead:** Creates new State object, hoists computation (slightly expensive). Don't over-use for every small computed value.
- **Composition tree size:** remember allocates slots in tree. 1000 remember calls = 1000 slots = memory overhead. Not a problem for typical screens, but huge list with remember per item is wasteful (use factory + scope).

</details>

### State Hoisting

**What:** Move state **up** to caller; state down as params, events up as lambdas. **When:** Reusable, testable, previewable composables. **Pattern:** `StatefulScreen()` → `StatelessScreen(state, onEvent)`. **Rule:** Hoist to **lowest common ancestor** needing the state.

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

## 8. Testing Essentials (Staff Level)

### Coroutine Testing

> **TL;DR:** `runTest` with virtual clock auto-skips delays (no waiting). `StandardTestDispatcher` queues work. Use `Dispatchers.setMain()` for Main dispatcher. Turbine for Flow testing.

`runTest` virtual time · `StandardTestDispatcher` queued · `advanceUntilIdle` control · `Dispatchers.setMain` · `Turbine` flow testing

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test
fun loadUser_withDelay() = runTest {  // Virtual clock active
    val viewModel = UserViewModel(fakeRepo)
    viewModel.load()

    advanceUntilIdle()  // Skip all delays instantly (virtual time)

    assertEquals(UiState.Success(user), viewModel.state.value)
}
```

</details>

| Tool | Purpose | When |
|---|---|---|
| **`runTest`** | Test builder; auto-skips delays | All coroutine tests |
| **`StandardTestDispatcher`** | Queues work; manual `advanceUntilIdle()` | Tests needing delay control |
| **`UnconfinedTestDispatcher`** | Eager execution; immediate | Collecting without delay |
| **`Dispatchers.setMain()`** | Replace Main in @Before | Main dispatcher tests |
| **`Turbine`** | `flow.test { awaitItem() }` | Flow/StateFlow testing |

<details>
<summary>🔩 Under the Hood</summary>

### Virtual clock & delay skipping

**Normal delay (without runTest):**
```kotlin
// Real time: Thread.sleep() blocks actual OS thread
delay(1000)  // Blocks for 1 second
```

**Virtual clock (inside runTest):**
```kotlin
@Test
fun test() = runTest {  // Virtual clock activated
    val startTime = currentTime
    delay(1000)  // Virtual: no actual wait, clock advances 1000ms
    advanceUntilIdle()  // Skip to next delayed operation
    val endTime = currentTime  // Instant later (in virtual time)
    // Test completes in milliseconds, not seconds!
}
```

**TestCoroutineScheduler internals:**
```kotlin
class TestCoroutineScheduler {
    private var virtualTime = 0L  // Virtual clock
    private val delayedTasks = PriorityQueue<Task>()  // Delay queue

    fun delay(ms: Long) {
        val task = Task(virtualTime + ms, block)
        delayedTasks.add(task)
        // No actual sleep; task queued at future virtual time
    }

    fun advanceUntilIdle() {
        while (delayedTasks.isNotEmpty()) {
            val nextTask = delayedTasks.poll()
            virtualTime = nextTask.time  // Jump to task's scheduled time
            nextTask.execute()
        }
    }
}
```

### StandardTestDispatcher vs UnconfinedTestDispatcher

**StandardTestDispatcher (recommended):**
```kotlin
@Test
fun test() = runTest {  // Uses StandardTestDispatcher by default
    val flow = flowOf(1, 2, 3)
    flow.collect { value ->
        // Collector runs queued, awaiting advanceUntilIdle()
    }
    advanceUntilIdle()  // Now collector executes
}
```

**UnconfinedTestDispatcher (eager):**
```kotlin
@Test
fun test() = runTest(UnconfinedTestDispatcher()) {
    val flow = flowOf(1, 2, 3)
    flow.collect { value ->
        // Collector executes immediately (not queued)
        println(value)
    }
    // No advanceUntilIdle() needed
}
```

### Dispatchers.setMain() pattern

```kotlin
@Before
fun setupMainDispatcher() {
    Dispatchers.setMain(StandardTestDispatcher())
}

@After
fun resetMainDispatcher() {
    Dispatchers.resetMain()  // Must reset to avoid leaking test state
}

@Test
fun test() = runTest {
    val viewModel = ViewModelThatUsesMain()  // Uses replaced Main dispatcher
    viewModel.updateUI()  // Safe: runs on virtual clock
}
```

### Turbine for Flow testing

```kotlin
@Test
fun searchFlow_emitsResults() = runTest {
    val searchFlow = searchViewModel.results
    searchFlow.test {
        searchViewModel.search("query")

        // Collect emissions in sequence
        assertEquals(Loading, awaitItem())
        assertEquals(Success(results), awaitItem())

        // Ensure no more emissions
        expectNoEvents()
    }
}
```

### What it reuses & relies on

- **TestCoroutineScheduler** — virtual clock implementation
- **Dispatchers** — can be replaced for testing
- **Job lifecycle** — cancellation works same in tests
- **Turbine library** — Flow testing DSL (kotlinx-coroutines-test dependency)

### Why this design was chosen

**Problem (real delays in tests):**
- Delaying 1000ms in test = 1000ms real wait (slow test suite)
- Flaky timeouts if CI slower than dev machine

**Virtual clock solution:**
- Skip delays in virtual time (tests run in milliseconds)
- Deterministic: same sequence always produces same result
- Testable: control time, test timeout scenarios

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "runTest auto-skips delays" | Virtual clock (TestCoroutineScheduler) jumps simulation time; no actual OS waits |
| "advanceUntilIdle() executes pending work" | Scheduler processes all queued tasks in virtual time order until idle |
| "StandardTestDispatcher queues work" | Tasks don't execute immediately; queued until advanceUntilIdle() called |
| "Must call resetMain() after test" | Dispatchers.setMain() global (affects all tests if not reset). Must restore to avoid test interference. |

### Gotchas at depth

- **Multiple advanceUntilIdle() calls:** Multiple calls execute queued work in batches. First call runs all work scheduled in initial time. Second call runs work scheduled by first batch, etc.
- **Unconfined + blocking:** UnconfinedTestDispatcher executes immediately but blocks if coroutine tries to switch dispatchers (unlike real Main which queues).
- **Flow collection timing:** If test doesn't await all items, collector left hanging. Turbine.expectNoEvents() validates nothing pending (or timeout).
- **setMain + AndroidDispatchers conflict:** AndroidDispatchers.Main (Jetpack) may not recognize test replacement. Explicitly use test dispatcher in ViewModel for testing.

</details>

### Compose Testing

> **TL;DR:** Use `createComposeRule()` to test Compose UI on JVM. Find nodes by text/tag. Robolectric 4.16+ lets Compose tests run without emulator. Verify with assertions; simulate interactions with `performClick()`.

`createComposeRule()` · `onNodeWithText()` or `onNodeWithTag()` · Robolectric JVM rendering · `assertIsDisplayed()` · `performClick()`

|Tool|Purpose|
|---|---|
|**`createComposeRule()`**|Compose test environment|
|**`onNodeWithText("X")`**|Find by text|
|**`onNodeWithTag("X")`**|Find by `Modifier.testTag()`|
|**`assertIsDisplayed()`**|Verify visibility|
|**`performClick()`**|Simulate tap|
|**Robolectric 4.16**|Compose on **JVM** — no emulator|
|**Screenshot testing**|`com.android.compose.screenshot` or Roborazzi|

<details>
<summary>💻 Code Example</summary>

```kotlin
@get:Rule
val composeRule = createComposeRule()

@Test
fun button_click_updates_text() {
    composeRule.setContent { MyButton() }
    composeRule.onNodeWithTag("my_button").performClick()
    composeRule.onNodeWithText("Clicked!").assertIsDisplayed()
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Compose Test Environment

**What createComposeRule() does:**
```kotlin
@get:Rule
val composeRule = createComposeRule()
// Internally:
// 1. Creates Composition with test clock (same virtual time as coroutine tests)
// 2. Renders Compose tree into test FrameLayout (Robolectric)
// 3. Provides SemanticsTree for node selection
// 4. Binds Dispatchers.Main to test dispatcher (no real Main thread)
```

### Robolectric 4.16+ Integration

**Why JVM rendering works:**
- Robolectric shadows Android framework (no emulator needed)
- Paints Compose UI to bitmap in memory
- Semantics tree extracted from composition (not from real Surface)
- Performance: 100x faster than emulator (no IPC, no GPU)

**Under the hood:**
```kotlin
// Test rendering flow:
composeRule.setContent { MyComposable() }
// → Composition created with TestCoroutineScheduler
// → Robolectric Shadow* classes intercept Canvas/Paint calls
// → Semantics collected from Recomposable
// → Node tree available for queries
```

### Node Selection via Semantics

**Finder strategy:**
```kotlin
// onNodeWithText() internally:
fun onNodeWithText(text: String): SemanticsNodeInteraction {
    val matcher = { semantics: SemanticsNode ->
        semantics.config.getOrNull(SemanticsProperties.Text)?.contains(text) == true
    }
    return onNode(matcher)  // Linear scan of SemanticsTree
}

// onNodeWithTag() uses testTag modifier:
Modifier.testTag("my_button")  // Adds to semantics.config[TestTag]
// Then finds by matcher
```

**Performance consideration:** Finding nodes is O(n) tree scan. Use specific matchers (tag > text > role).

### Performance & Timing

**Virtual time applies:**
```kotlin
@Test
fun animation_completes() = runTest {  // Shares scheduler with Compose
    composeRule.setContent { AnimatedButton() }
    composeRule.clock.advanceTimeByFrame()  // Skips animation frames
    composeRule.onNode(...).assertExists()
}
```

### What it reuses & relies on

- **Semantics** — accessibility tree used for node selection (same as TalkBack)
- **Robolectric** — Android framework shadowing
- **TestCoroutineScheduler** — virtual time for animations, delays
- **Composition** — internal Compose state management

### Why this design was chosen

**Problem:** Compose is declarative, not inspectable like View XML.
- View tests could read hierarchy via Espresso
- Compose tree exists only during recomposition (functional)

**Solution: Semantics tree.**
- Expose metadata (text, contentDescription, roles) without exposing internal state
- Stable across recompositions
- Works on JVM (Robolectric shadows it)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Find nodes by text/tag" | Semantics tree is O(n) linear scan; tag matching is O(1) in semantics.config |
| "createComposeRule() renders to screen" | Robolectric shadows Canvas; renders to bitmap in memory, no actual display |
| "Clock controls animations" | TestCoroutineScheduler advanced via composeRule.clock; animations calculated in virtual time |
| "performClick() simulates tap" | Injects SemanticsAction.OnClick into node; triggers lambda without real touch event |

### Gotchas at depth

- **Node not found → silent wait:** `onNode().performClick()` waits (default 1s) if not found, then throws. No fast-fail. Use `waitUntilExists()` if async rendering.
- **Text matching is substring:** `onNodeWithText("Click")` matches "Click Me" and "Clickable". Use `useUnmergedTree = true` to search unmerged nodes only.
- **Recomposition timing:** `setContent()` queues recomposition. Call `composeRule.waitForIdle()` before assertions if state updates are delayed.
- **Modifier.testTag persists:** Don't use in production code. Use dev-only `BuildConfig.DEBUG` check if accidentally added.

</details>

### Test Doubles: Fakes, Mocks, Stubs (Hierarchy)

> **TL;DR:** Test Double replaces real dependency. Fakes are real logic (in-memory DB). Mocks verify interactions (was X called?). Stubs return hardcoded values. Use Fakes by default (fast, deterministic). Mock only for verification or when faking impractical.

Fake (real impl, simplified) · Mock (verify interactions) · Stub (hardcoded returns)

| Test Double | Definition | When | Example |
|---|---|---|---|
| **Fake** | Real impl, simplified | Test logic/integration | In-memory Repository |
| **Mock** | Verifies interactions | Verify side effects | Verify analytics logged |
| **Stub** | Hardcoded return | One-off test data | `every { repo.get() } returns user` |

<details>
<summary>💻 Code Example</summary>

```kotlin
// Fake (preferred)
class FakeUserRepository : UserRepository {
    override suspend fun getUser(id: Int) = User(id, "Test")
}

// Mock (verify call)
val repo = mockk<UserRepository>()
coVerify { repo.saveUser(any()) }

// Stub (minimal setup)
every { repo.getUser() } returns fakeUser
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Fake: Real Implementation Simplified

**What it does:**
```kotlin
// Real repository (Retrofit + Room):
class UserRepository(
    val api: UserApi,
    val db: UserDao
) {
    suspend fun getUser(id: Int): User {
        val cached = db.getUser(id)  // Try cache
        if (cached != null) return cached
        val user = api.fetchUser(id)  // Network call
        db.insertUser(user)  // Save to DB
        return user
    }
}

// Fake repository (in-memory):
class FakeUserRepository : UserRepository {
    private val cache = mutableMapOf<Int, User>()

    override suspend fun getUser(id: Int): User {
        val user = cache[id] ?: throw NotFoundException()
        return user
    }

    // Test-only: manually populate
    fun addUser(user: User) { cache[user.id] = user }
}

// Test:
val repo = FakeUserRepository()
repo.addUser(User(1, "Alice"))
val user = repo.getUser(1)  // ✅ Returns immediately
// No actual DB I/O or network
```

**Why Fakes work:**
- Implement the same interface (UserRepository)
- Provide predictable behavior (no network variability)
- Keep test logic readable (no framework boilerplate)
- Fast (in-memory operations ~1μs vs API call ~100ms)

### Mock: Interaction Verification

**MockK internals:**
```kotlin
val repo = mockk<UserRepository>()  // Generates proxy at runtime

// MockK creates:
// 1. JVM Proxy implements UserRepository
// 2. Every method call logged to call history
// 3. Returns default values (null, 0, empty collections)

repo.saveUser(user)  // Logged: [Call(saveUser, [User(...)])]

coVerify { repo.saveUser(any()) }  // Scans history
// → Finds matching call
// → Passes test
```

**Why MockK uses reflection/bytecode generation:**
```kotlin
// Without framework (manual mock):
class ManualMockRepository : UserRepository {
    var saveUserCalls = mutableListOf<User>()
    override suspend fun saveUser(user: User) {
        saveUserCalls.add(user)
    }
}
// Tedious: manual tracking for every method

// MockK does it automatically via proxy
```

**When to use Mocks:**
```kotlin
// Use case: Verify analytics logged
val analytics = mockk<Analytics>()
viewModel.trackEvent("button_clicked")
verify { analytics.log(Event("button_clicked")) }

// Why not Fake here?
// - Analytics is fire-and-forget (no return value to test)
// - We care that it WAS CALLED, not what it does
// - Faking it (tracking in-memory list) is reinventing mock
```

### Stub: Hardcoded Return Values

**When to use Stubs:**
```kotlin
@Test
fun test() {
    val userApi = mockk<UserApi>()

    // Stub: hardcoded return for specific call
    every { userApi.getUser(1) } returns User(1, "Alice")
    every { userApi.getUser(2) } returns User(2, "Bob")

    // Any other ID returns null (MockK default)
    val result = userApi.getUser(999)  // null
}
```

**Stubs in production code (not tests):**
```kotlin
// When actual implementation not yet written
class UserApi {
    fun getUser(id: Int): User = stub()  // TODO: implement
}
// Compilation error: forces implementation
```

### Preference Order: Fake → Stub/Mock

**Hierarchy (best to worst):**

1. **Fake** — Full logic, fast, deterministic
   ```kotlin
   val repo = FakeUserRepository()  // Use this
   ```

2. **Stub** (within Mock) — Minimal setup, OK for simple cases
   ```kotlin
   val repo = mockk<UserRepository>()
   every { repo.getUser(1) } returns user  // OK
   ```

3. **Mock (verification)** — Use only for side effects
   ```kotlin
   val analytics = mockk<Analytics>()
   viewModel.track()
   verify { analytics.log(...) }  // OK only here
   ```

**Why this order:**
- Fakes test actual logic (closest to prod)
- Stubs test with minimal setup
- Mocks test behavior, not logic (loosest coupling)

### Real Example: When Faking is Impractical

```kotlin
// Real: Database with Room, constraints, triggers
val roomDb: MyDatabase = mockk()  // Too complex to fake

// Solution: Stub the queries
every { roomDb.userDao().getUser(1) } returns User(1, "Test")

// Alternative: In-memory Room database
@get:Rule
val inMemoryDb = room.inMemoryDatabaseBuilder(
    MyDatabase::class.java
).build()  // Real Room, real DB engine, in RAM

@Test
fun test() {
    inMemoryDb.userDao().insertUser(user)
    val result = inMemoryDb.userDao().getUser(user.id)
    assertEquals(user, result)  // Tests actual SQL
}
```

### What it reuses & relies on

- **Interfaces** — Fakes/Mocks must implement same contract
- **Proxy pattern** — MockK uses JVM Proxy or bytecode generation
- **Reflection** — MockK inspects method signatures at runtime
- **Dependency Injection** — Fakes injected same way as real impl

### Why this design was chosen

**Problem:** How to test without side effects?
- Real database: slow, shared state between tests
- Real API: flaky network, external dependencies
- Real file system: leftover test files, cleanup complexity

**Solution: Test Doubles.**
- Fake: Trade accuracy for speed (tests logic, not I/O)
- Mock: Trade completeness for verification (tests contracts, not impl)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Fakes are simple implementations" | Fakes implement full interface; test tests actual logic (if() branches, loops, null checks) |
| "Mocks verify that a function was called" | MockK uses Proxy or CGLIB to intercept calls; maintains call history; `verify()` scans history |
| "Stubs return hardcoded values" | Stubs configured via `every {...} returns ...` DSL; any unconfigured method returns MockK default (null, 0, empty) |
| "Use Fakes by default" | Fakes are closest to production (test real logic); slower to set up (write Fake class) but faster to run (in-memory) |

### Gotchas at depth

- **Fake gets out of sync:** Real impl changes, Fake not updated. Tests pass, prod fails. Use golden tests or contract tests to catch.
- **Mock verification order:** `verify(ordering = Ordering.SEQUENCE)` checks call order. Unordered by default—can pass even if calls happen in different order than expected.
- **every {...} returns runs immediately:** `every { expensive() } returns value` doesn't delay. If you need lazy computation, use `every { expensive() } answers { computeValue() }`.
- **Stub + Mock mix:** Using both (stub return + verify call) couples test to impl. Better: Fake (checks logic) + Mock verification (only for logging/analytics).

</details>

### Fake Repository Pattern (for ViewModel testing):

<details>
<summary>💻 Code Example</summary>

```kotlin
class FakeUserRepository : UserRepository {
    private var shouldFail = false
    private var failureMessage = ""

    fun setShouldFail(msg: String) { shouldFail = true; failureMessage = msg }
    fun reset() { shouldFail = false }

    override suspend fun getUser(id: Int): User {
        if (shouldFail) throw Exception(failureMessage)
        return User(id, "Test User")
    }
}

@Test
fun loadUser_onSuccess() = runTest {
    val repo = FakeUserRepository()
    val viewModel = UserViewModel(repo)
    viewModel.load()

    advanceUntilIdle()  // Let coroutine finish
    assertEquals(UiState.Success(User(1, "Test User")), viewModel.state.value)
}

@Test
fun loadUser_onError() = runTest {
    val repo = FakeUserRepository()
    repo.setShouldFail("Network error")
    val viewModel = UserViewModel(repo)
    viewModel.load()

    advanceUntilIdle()
    assertEquals(UiState.Error("Network error"), viewModel.state.value)
}
```

</details>

**Say:** "I use Fakes for unit tests (state/integration), Mocks for interaction verification (logging, tracking). Fakes are default—simpler, faster, KMP-compatible."

---

## 9. Live Coding Survival (25-Minute Strategy)

### The Checklist (Timer Starts)

1. **Clarify** (1 min) — inputs, outputs, edge cases. "Should I handle errors?"
2. **State approach** (1 min) — "ViewModel + StateFlow + Repository"
3. **Skeleton first** (3 min) — data class, ViewModel stub, Composable collecting state
4. **Fill logic** (remaining) — happy path first, error handling last. **Talk while coding.**

### ViewModel + StateFlow + Repository (Full Pattern with Error Handling)

**Quick skeleton (5 lines — happy path):**
<details>
<summary>💻 Code Example</summary>

```kotlin
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow(UiState())
    val state = _state.asStateFlow()
    fun load() { viewModelScope.launch { _state.update { it.copy(user = repo.getUser()) } } }
}
data class UiState(val user: User? = null, val error: String? = null)
```

</details>

**Production version (with errors + loading):**
<details>
<summary>💻 Code Example</summary>

```kotlin
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow<UiState>(UiState.Loading)
    val state = _state.asStateFlow()

    fun load() {
        viewModelScope.launch {
            try {
                val user = repo.getUser()
                _state.value = UiState.Success(user)
            } catch (e: Exception) {
                _state.value = UiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

sealed interface UiState {
    data object Loading : UiState
    data class Success(val user: User) : UiState
    data class Error(val message: String) : UiState
}
```

</details>

**Why sealed interface over data class:** Exhaustive when, prevents invalid states (can't have both user and error), clearer intent.

**Common live-code gotchas:**
1. **Forget `viewModelScope`** → GlobalScope (memory leak)
2. **Not handling errors** → crashes during demo
3. **Accessing `.value` in UI** → doesn't recompose. Use `collectAsStateWithLifecycle()` instead.
4. **State naming:** Suffix with `ViewModel` (UserViewModel), `UiState` or `UiModel` for state class.

**Quick error handling pattern (2 min to write):**
<details>
<summary>💻 Code Example</summary>

```kotlin
_state.update {
    try {
        it.copy(items = repo.getItems(), isLoading = false)
    } catch (e: Exception) {
        it.copy(error = e.message, isLoading = false)
    }
}
```

</details>

### Modularization — If They Ask

**Benefits:** (1) **Faster builds** — unchanged modules skip recompilation. (2) **Enforced boundaries** — no cross-module internal access.

**Pattern:** `:feature:home`, `:feature:profile`, `:core:network`, `:core:data`, `:core:ui`. Convention plugins in `build-logic/`.

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

## 11. Gradle & Build Tooling

### Kotlin DSL vs Groovy

> **TL;DR:** Kotlin DSL (`.kts`) = type-safe, IDE support, modern. Groovy (`.gradle`) = dynamic, legacy. Use Kotlin DSL for new projects (AGP 9+ default). Groovy works but not recommended.

`Kotlin DSL` type-safe · `Groovy` dynamic · `IDE autocomplete` · `Convention plugins` · `AGP 9+ default`

<details>
<summary>💻 Code Example</summary>

```kotlin
// Kotlin DSL (build.gradle.kts) - Type-safe
android {
    compileSdk = 35
    defaultConfig { applicationId = "com.example.app" }
}
dependencies {
    implementation(libs.androidx.core)  // Type-safe reference
}

// Groovy (build.gradle) - Dynamic
android {
    compileSdkVersion 35
    defaultConfig { applicationId "com.example.app" }
}
dependencies {
    implementation libs.androidx.core  // String-based, autocomplete weak
}
```

</details>

| Feature | Kotlin DSL | Groovy |
|---|---|---|
| **IDE autocomplete** | ✅ Full | ⚠️ Limited |
| **Type checking** | ✅ Compile-time | ❌ Runtime errors |
| **Syntax errors** | ✅ Caught by IDE | ❌ Found at gradle sync |
| **2026 default** | **Yes** | Supported only |
| **Performance** | Slightly faster (compiled) | Slightly slower (interpreted) |

<details>
<summary>🔩 Under the Hood</summary>

### Gradle configuration model & DSL generation

**Kotlin DSL compilation:**
```
build.gradle.kts
  ↓ (Kotlin compiler at sync)
  ↓ Type-checks against Project API
  ↓ Generates build.gradle.kts.jar (compiled Kotlin bytecode)
  ↓ Gradle loads JAR, executes configuration
  Result: Type errors caught before gradle runs
```

**Groovy interpretation:**
```
build.gradle
  ↓ (Gradle reads as DSL text)
  ↓ Method resolution at runtime (dynamic dispatch)
  ↓ If method not found: error during sync
  Result: Errors found later, harder to debug
```

### Lazy vs Eager task configuration

**Eager (Groovy, old pattern):**
```groovy
tasks.create("myTask") {
    doLast {
        println "Task running"
    }
}

// Problem: Task created immediately, even if not used
// Large build.gradle = many unused tasks created upfront
```

**Lazy (Kotlin DSL, recommended):**
```kotlin
tasks.register("myTask") {  // register() instead of create()
    doLast {
        println "Task running"
    }
}

// Benefit: Task created only if referenced/used
// Faster configuration phase (skips unused tasks)
```

**Configuration phase optimization:**
```
Gradle configuration phase:
  1. Read all build.gradle files
  2. Register tasks (but don't execute yet)
  3. Build task graph
  4. Execute tasks

Eager tasks: All created in step 2 (slower config phase)
Lazy tasks: Only registered if actually used (faster config phase)
```

### Convention plugins (Kotlin DSL requirement)

**Pattern:**
```kotlin
// plugins/build-logic/src/main/kotlin/MyConvention.gradle.kts
plugins {
    id("com.android.library")
}

android {
    compileSdk = 35
    defaultConfig {
        minSdk = 24
    }
}

// App's build.gradle.kts:
plugins {
    id("com.example.my-convention")  // Reusable configuration
}

// Benefit: Share build config across modules (DRY)
```

**Requires Kotlin DSL:** Convention plugins must be `.kts` (Groovy plugins deprecated).

### What it reuses & relies on

- **Kotlin compiler** — type-checks `.kts` at sync time
- **Gradle Plugin API** — Project, Task, Extension interfaces
- **Groovy interpreter** — Groovy `.gradle` evaluated at runtime
- **Build model** — task graph, configuration vs execution phases

### Why this design was chosen

**Kotlin DSL benefits:**
- Type-safe: IDE prevents mistakes
- Faster configuration: lazy registration
- Convention plugins possible (modern build architecture)

**Groovy legacy:**
- Pre-Kotlin era (simpler dynamic syntax seemed appealing)
- No compile-time checks (worked fine until projects got large)
- Now superceded by Kotlin DSL (static typing + tooling)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Kotlin DSL has better IDE support" | `.kts` compiled by Kotlin compiler; type errors caught at sync. `.gradle` interpreted at runtime. |
| "Use register() instead of create()" | register() = lazy (only creates if used). create() = eager (creates immediately). Faster config phase with lazy. |
| "Convention plugins are .kts" | Convention plugins (reusable build logic) require Kotlin DSL. Groovy plugins being deprecated. |
| "Kotlin DSL is default" | AGP 9+ defaults to `.kts` for all generated files. Groovy still works but not recommended for new code. |

### Gotchas at depth

- **Type safety can be overly strict:** Sometimes you want dynamic behavior (Groovy lets you). Kotlin DSL requires more explicit types.
- **Kotlin DSL sync slower first time:** Compilation adds overhead. Subsequent syncs faster (caching). Groovy syncs always fast (no compilation).
- **Mixed .gradle + .kts:** Both can coexist but confusing. Pick one (ideally all `.kts`). IDE autocomplete weak if mixed.
- **AGP version compatibility:** Older AGP may not support all Kotlin DSL features. Keep AGP updated for best compatibility.

</details>

### Version Catalogs

> **TL;DR:** `gradle/libs.versions.toml` centralizes all versions and dependencies. Single source of truth. Gradle generates type-safe `libs.*` accessors. AGP 9+ default.

`TOML format` · `Centralized versions` · `Type-safe accessors` · `No string magic` · `Easy updates`

<details>
<summary>💻 Code Example</summary>

```toml
# gradle/libs.versions.toml
[versions]
kotlin = "2.0.0"
androidx-core = "1.13.1"

[libraries]
androidx-core = { module = "androidx.core:core", version.ref = "androidx-core" }
kotlinx-serialization = "org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.3"

[bundles]
androidx = ["androidx-core"]

[plugins]
android-application = { id = "com.android.application", version = "8.2.0" }
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
// build.gradle.kts - type-safe usage
dependencies {
    implementation(libs.androidx.core)          // Single lib
    implementation(libs.bundles.androidx)       // Bundle
}

plugins {
    id(libs.plugins.android.application)
}
```

</details>

| Pattern | Example | Benefit |
|---|---|---|
| **Single version** | `[versions]` + `version.ref` | Update once, used everywhere |
| **Type-safe ref** | `libs.androidx.core` | IDE autocomplete, no strings |
| **Bundles** | `libs.bundles.androidx` | Group related deps |
| **Plugins** | `libs.plugins.android.application` | Reusable plugin versions |

<details>
<summary>🔩 Under the Hood</summary>

### TOML parsing & generated accessors

**What Gradle does:**
```
gradle/libs.versions.toml (TOML file)
  ↓ (Gradle reads at sync)
  ↓ Parser: [versions], [libraries], [plugins], [bundles]
  ↓ Generates: build/.gradle/generated/gradle/libs/Libs.kt
  ↓ Exposes: libs.androidx.core, libs.bundles.androidx, etc.
```

**Generated accessors (pseudocode):**
```kotlin
// Generated in build/.gradle/generated/gradle/libs/Libs.kt
object Libs {
    object Androidx {
        val core = "androidx.core:core:1.13.1"
    }
    object Bundles {
        val androidx = listOf(Libs.Androidx.core)
    }
}

// So you write:
dependencies {
    implementation(libs.androidx.core)  // IDE sees this, autocompletes
}
```

**Naming transformation:**
```
TOML: androidx-core
→ Property: androidx.core (dash to nested property)

TOML: [plugins] android-application
→ Property: libs.plugins.android.application

Naming convention makes hierarchical structure accessible
```

### Why centralized versions matter

**Before Version Catalogs (scattered):**
```kotlin
// build.gradle.kts (app module)
dependencies {
    implementation("androidx.core:core:1.13.1")
}

// build.gradle.kts (lib-a module)
dependencies {
    implementation("androidx.core:core:1.12.0")  // Different version!
}

// Problem: Two modules use different versions (potential conflicts)
```

**After Version Catalogs (centralized):**
```toml
[versions]
androidx-core = "1.13.1"
```
All modules reference same version. No conflicts.

### Type-safe accessors vs strings

**String approach (error-prone):**
```kotlin
dependencies {
    implementation("androidx.core:core:1.13.1")  // Typo: "androidx.cor" → unnoticed until runtime
    implementation("androidx.core:core:1.12.0")  // What version? Have to scroll up
}
```

**Type-safe accessors (safe):**
```kotlin
dependencies {
    implementation(libs.androidx.core)  // IDE catches typo immediately (androidx.cor doesn't exist)
    // Version is in TOML, single update point
}
```

### What it reuses & relies on

- **TOML parser** — Gradle includes TOML support natively
- **Kotlin code generation** — generates accessor .kt files at sync
- **Gradle plugin API** — Extension model to define libs object
- **Classpath** — accessors added to buildscript classpath automatically

### Why this design was chosen

**Problem:** 20+ dependencies across modules, versions scattered everywhere.

**Solution:** Single TOML file as source of truth. Gradle generates type-safe code.

**Benefits:**
- One place to update versions (no copy-paste)
- Type-safe access (IDE prevents typos)
- DRY (don't repeat versions)
- Bundles for common groups (androidx, testing, etc.)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Version Catalogs centralize versions" | TOML file parsed by Gradle; generates `.kt` accessor file with type-safe properties |
| "Use libs.androidx.core" | libs object created by code generation; androidx.core maps to TOML [libraries] entry |
| "Dash converts to nested property" | androidx-core in TOML → androidx.core property (dash = hierarchy separator) |
| "Sync regenerates accessors" | Every sync re-parses TOML, regenerates accessor file (`.gradle/generated/`). Changes immediate. |

### Gotchas at depth

- **TOML syntax strict:** Invalid TOML = sync fails cryptically. Validate TOML (use IDE plugin or online validator).
- **Accessor generation delay:** If sync didn't regenerate, IDE might not see updated libs. Clean build (Ctrl+Shift+S) forces regen.
- **Version constraints not reflected:** Version Catalogs don't enforce "use max version" automatically. Still need gradle resolution strategy if conflicts occur.
- **Mixed manual + TOML:** If some deps in TOML and others hardcoded, defeats purpose. Migrate all or none (avoid confusion).

</details>

### Build Types vs. Product Flavors

> **TL;DR:** Build Types = *how* to build (debug/release, minify, signing). Product Flavors = *what* to build (free/premium, dev/prod, regions). Flavors × Build Types = all variants (e.g., `freeDebug`, `premiumRelease`).

Build Type (debug/release) · Flavor (free/premium) · Variant (dimension) · `applicationIdSuffix` · `buildConfigField`

|Concept|Build Types|Product Flavors|
|---|---|---|
|**Purpose**|**How** to build|**What** to build|
|**Examples**|`debug`/`release`|`free`/`premium`, `dev`/`prod`|
|**Controls**|minify, debuggable, signing, JVM args|appId suffix, resources, endpoints, feature flags|
|**Combine**|`freeDebug`, `premiumRelease`||

**Build Types deep dive:**
<details>
<summary>💻 Code Example</summary>

```kotlin
buildTypes {
    debug {
        debuggable = true
        minifyEnabled = false
        signingConfig = signingConfigs.getByName("debug")
    }
    release {
        debuggable = false
        minifyEnabled = true
        signingConfig = signingConfigs.getByName("release")
        proguardFiles("proguard-rules.pro")
    }
    // Custom type for internal testing
    staging {
        initWith(release)
        debuggable = true
        minifyEnabled = false
        applicationIdSuffix = ".staging"
    }
}
```

</details>

**Product flavors for multi-variant apps:**
<details>
<summary>💻 Code Example</summary>

```kotlin
flavorDimensions = listOf("tier", "region")
productFlavors {
    create("free") { dimension = "tier"; applicationIdSuffix = ".free" }
    create("premium") { dimension = "tier" }
    create("us") { dimension = "region" }
    create("eu") { dimension = "region"; buildConfigField("String", "API_URL", "\"https://api-eu.example.com\"") }
}
// Variants: freeDebug, freeUsDebug, premiumEuRelease, etc.
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Build Type vs Flavor Distinction

**Build Type:**
- Controls compilation & packaging (how you build)
- Single selection per build (either debug OR release)
- Applied to final APK/AAB

**Product Flavor:**
- Controls app variant (what you ship)
- Multiple dimensions allow combinations (tier × region)
- Each combination = unique app (different appId, resources, code paths)

**Example: Free + Debug vs Premium + Release**
```kotlin
// Free Debug: dev build, logging, no minify, free API endpoint
// Premium Release: prod build, minified, signing, premium API endpoint
```

### Dimension Combinations (Variant Explosion)

**With 2 dimensions:**
```
tier: [free, premium]      (2 options)
region: [us, eu]           (2 options)
build types: [debug, release] (2 options)
Total variants = 2 × 2 × 2 = 8 variants
```

**Variants generated:**
- freeUsDebug
- freeUsRelease
- freeEuDebug
- freeEuRelease
- premiumUsDebug
- premiumUsRelease
- premiumEuDebug
- premiumEuRelease

**Problem:** Too many dimensions = variant explosion (slow build). Keep dimensions ≤2.

### buildConfigField & Resource Selection

**buildConfigField (compile-time constant):**
```kotlin
buildConfigField("String", "API_URL", "\"https://api-free.example.com\"")
// Generates: BuildConfig.API_URL = "https://api-free.example.com"
// Used: API calls fetch from BuildConfig.API_URL
```

**Resource selection (src/free/resources/values/strings.xml):**
```xml
<!-- src/free/resources/values/strings.xml -->
<string name="app_name">MyApp (Free)</string>

<!-- src/premium/resources/values/strings.xml -->
<string name="app_name">MyApp (Premium)</string>
```
Gradle merges: free variant uses free/strings.xml, premium uses premium/strings.xml.

### What it reuses & relies on

- **Gradle variant generation** — combinations of flavorDimensions × buildTypes
- **Source set merging** — src/main + src/flavor/ + src/buildType/ combined
- **Resource overlay** — later sources override earlier (flavor > main)
- **BuildConfig code generation** — Gradle creates fields from buildConfigField calls

### Why this design was chosen

**Problem:** Multi-app strategy without duplicating codebase.
- One codebase = 1 app
- Flavors = multiple apps from 1 codebase (share core logic, vary appearance/config)

**Example:** Google Play allows multiple APKs per app (free vs premium). Build system needed to support this at scale.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Build Types control debug vs release" | Debug = debuggable flag ON, minify OFF. Release = minify ON via R8/ProGuard, signing configured. |
| "Product Flavors differentiate apps" | Gradle creates variant per dimension combo; merges src/main + src/flavor + src/buildType source sets. |
| "buildConfigField sets constants" | Gradle generates BuildConfig.java with static fields; constants inlined by compiler (no reflection). |
| "Appending .free suffix" | applicationIdSuffix appended to base appId (com.example.app + ".free" = com.example.app.free). Allows multiple installs. |

### Gotchas at depth

- **Flavor dimension required:** Flavors must declare dimension. If missing, gradle error. Use same dimension names across modules for consistency.
- **Source set priority:** src/freeDebug > src/free > src/debug > src/main. Debug specifics override flavor specifics (careful!).
- **Resource duplication:** If free and premium need different layouts, must create src/free/res/layout/main.xml (whole file, not just changes).
- **Variant explosion:** 3 dimensions × 2 flavors each = 8 variants. Gradle build time scales with variant count. Use source set filtering if possible.

</details>

### Dependency Resolution & Conflicts

> **TL;DR:** Dependency conflicts occur when transitive deps want different versions. Gradle defaults to *highest version*. Fix via: force strategy, BOM (preferred), or exclude transitive. BOM is safest (Google Firebase, AndroidX patterns use it).

Transitive dependencies · Highest version strategy · `force()` · `exclude()` · BOM (Bill of Materials)

**Problem:** Two transitive deps want different versions of the same lib.
<details>
<summary>💻 Code Example</summary>

```
app → lib-a (wants okhttp 4.10) → lib-b (wants okhttp 4.9)
// Gradle picks 4.10 (highest version, default strategy)
```

</details>

**Resolution Strategies:**
1. **Force version (not recommended):** Overrides all versions
<details>
<summary>💻 Code Example</summary>

   ```kotlin
   configurations.all {
       resolutionStrategy {
           force("com.squareup.okhttp3:okhttp:4.10.0")
       }
   }
   ```

</details>

2. **Exclude transitive (risky):** Remove conflicts manually
<details>
<summary>💻 Code Example</summary>

   ```kotlin
   implementation("lib-a") { exclude("com.squareup.okhttp3") }
   ```

</details>

3. **Bill of Materials - BOM (RECOMMENDED):** Single source of truth
<details>
<summary>💻 Code Example</summary>

   ```kotlin
   implementation(platform("com.google.firebase:firebase-bom:33.0.0"))
   implementation("com.google.firebase:firebase-analytics")  // Version from BOM
   implementation("com.google.firebase:firebase-messaging")  // Same version
   ```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Gradle Dependency Graph Resolution

**Dependency graph construction:**
```
app/build.gradle.kts declares:
  implementation("okhttp:4.11.0")
  implementation("retrofit2:2.9.0")

retrofit2:2.9.0 transitively depends on:
  okhttp:4.9.0

Gradle builds graph:
  app
    ├── okhttp:4.11.0 (direct)
    └── retrofit2:2.9.0
         └── okhttp:4.9.0 (transitive)

Conflict detected: okhttp:4.11.0 vs okhttp:4.9.0
Resolution strategy: highest version → okhttp:4.11.0 wins
```

**Resolution Strategy Options:**
1. **Highest version (default):** okhttp:4.11.0 selected
2. **Fail on conflict:** Error if mismatch found (rare)
3. **Custom strategy:** User-defined rules

### Bill of Materials (BOM) Mechanism

**What BOM provides:**
```toml
<!-- firebase-bom:33.0.0 declares (internally) -->
[library_versions]
firebase-analytics = "21.6.1"
firebase-messaging = "23.4.1"
okhttp = "4.11.0"  <!-- BOM also manages transitive deps! -->
```

**How it works:**
```kotlin
// Step 1: Declare BOM (not a library, no code)
implementation(platform("com.google.firebase:firebase-bom:33.0.0"))

// Step 2: Gradle loads BOM constraints
// All firebase libs will use versions declared in BOM

// Step 3: Gradle resolves lib versions from BOM
implementation("com.google.firebase:firebase-analytics")
// → Gradle looks up "firebase-analytics" in BOM → 21.6.1
```

**BOM vs direct version declaration:**
```kotlin
// Without BOM (manual):
implementation("com.google.firebase:firebase-analytics:21.6.1")
implementation("com.google.firebase:firebase-messaging:23.4.1")
// Multiple places to update if version changes

// With BOM (centralized):
implementation(platform("com.google.firebase:firebase-bom:33.0.0"))
implementation("com.google.firebase:firebase-analytics")  // No version
implementation("com.google.firebase:firebase-messaging")  // No version
// One place to update (BOM version)
```

### Transitive Dependency Exclusion (Dangerous)

**When you exclude:**
```kotlin
implementation("okhttp:4.11.0")
implementation("retrofit2:2.9.0") {
    exclude("okhttp")  // Remove okhttp from retrofit2's deps
}
// Result: Only okhttp:4.11.0 used
// Risk: retrofit2 tested with okhttp:4.9.0; may break with 4.11.0
```

**Problems with exclusion:**
- Retrofit assumes okhttp 4.9 APIs exist (may be removed in 4.11)
- No guarantee of compatibility
- Hard to debug ("library X mysteriously crashes with version Y")

**Better:** Use BOM that was tested together.

### Force Strategy (Last Resort)

```kotlin
configurations.all {
    resolutionStrategy {
        force("com.squareup.okhttp3:okhttp:4.10.0")
    }
}
```

**What happens:**
- Gradle force-selects okhttp:4.10.0 regardless of declared versions
- No conflict resolution needed
- Risk: Untested combination (like exclusion)

**Use only if:**
- BOM not available
- Multiple independent transitive deps want incompatible versions
- You've tested the forced version

### What it reuses & relies on

- **Gradle dependency resolution algorithm** — DAG (directed acyclic graph) traversal
- **Version constraints** — declared in build.gradle.kts or BOM
- **Transitive dependency closure** — recursively resolved
- **Maven Central/Google Maven** — where libs fetched from

### Why this design was chosen

**Problem:** Complex projects have 100+ transitive deps; versions scatter everywhere.

**Solution:** BOM pattern (Maven standard).
- Single version file (BOM) tested together
- All libs in same BOM guaranteed compatible
- One update point for large sets of libs

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Gradle picks highest version" | Gradle builds DAG of deps; conflict resolver selects max version (Semver-based). Configurable. |
| "BOM enforces versions" | BOM constraints applied during graph resolution. Gradle looks up libs in BOM instead of declared versions. |
| "Exclude removes conflicts" | exclusion() removes edges in DAG. Risk: untested version combos may break. |
| "Force overrides everything" | resolutionStrategy.force() applies global rule; all paths to lib get forced version regardless. |

### Gotchas at depth

- **BOM ordering matters:** `platform()` must come before dependent libs (affects version selection order).
- **Transitive closure explosion:** 100 direct deps can pull 1000+ transitive. Slow resolution on first build. Gradle caches (second builds fast).
- **Version scheme mismatch:** Some libs use Semver (1.2.3), others don't (2021.01.01). Highest version may not mean "latest stable."
- **Conflicting BOMs:** Two BOMs declare different versions of same lib. Gradle error if not resolvable. Use exclusion or version overrides carefully.

</details>

### Task Execution & Caching

**Gradle tasks:** `./gradlew assemble` = compile + package. Skips unchanged sources (incremental build).

**ABI change:** If public API changes, all dependents recompile (ABI incompatibility).

**Custom task with caching:**
<details>
<summary>💻 Code Example</summary>

```kotlin
tasks.register("reportVersions") {
    doLast {
        println("Kotlin: ${kotlinVersion}, AGP: ${agpVersion}")
    }
}
./gradlew reportVersions  // Task runs
./gradlew reportVersions  // Task runs again (no outputs to cache)
```

</details>

**Parallel build:** `org.gradle.parallel=true` in gradle.properties. Faster on multi-core. Beware: some plugins not thread-safe.

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

## 14. Interview Strategy & Communication Tips

### Live Coding Best Practices

> **TL;DR:** Spend 70% on happy path, 20% on errors, 10% on polish. Clarify requirements first (1 min), sketch architecture (1 min), implement visible structure (18 min), then error handling (5 min). Talk constantly—interviewers want to hear reasoning.

Time-boxing · Happy path first · Visible architecture · Constant communication · Code quality signals

**Time Budget (25 min total):**

| Phase | Time | Goal | Key Action |
|---|---|---|---|
| **Clarify** | 0-1 min | Write down requirements | Ask about errors, edge cases, scope |
| **Sketch** | 1-2 min | Draw architecture on board | ViewModel + Repository + UI pattern |
| **Stub** | 2-5 min | Class structure only | Data classes, interfaces, minimal logic |
| **Happy path** | 5-20 min | Core feature working | Main flow, happy case, ignore errors |
| **Polish** | 20-25 min | Error handling, edge cases | Try-catch, validation, "nice to have" |

**Code Quality Signals (What Interviewers See):**

1. **Type safety** — sealed interfaces, specific exception types
2. **Naming** — `UserViewModel` not `VM`, `onUserLoaded` not `onSuccess`
3. **Immutability** — `data class`, `val`, immutable collections
4. **Error handling** — try-catch or Result type (not ignored)
5. **Testing-friendly** — injected dependencies, no hardcoded singletons

<details>
<summary>💻 Code Example</summary>

```kotlin
// Strong signal code:
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow<UiState>(UiState.Loading)
    val state = _state.asStateFlow()

    fun loadUser(id: Int) {
        viewModelScope.launch {
            try {
                val user = repo.getUser(id)
                _state.value = UiState.Success(user)
            } catch (e: IOException) {
                _state.value = UiState.Error("Network error")
            }
        }
    }
}

sealed interface UiState {
    data object Loading : UiState
    data class Success(val user: User) : UiState
    data class Error(val message: String) : UiState
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Why Time-Boxing Matters

**Problem (writing too much):**
```
Interview starts: 2 min questions
Candidate starts coding: spends 20 min on perfect architecture
Interviewer: "We're out of time. Show me it working."
Candidate: "Just need 5 more minutes..."
Result: Interview ends. Feature half-done. Interviewer unsure of ability.
```

**Solution (time-boxing):**
```
Interview starts: 1 min questions
Clarify: 1 min
Sketch: 1 min
Stub: 3 min (data classes, interface structure visible early)
Happy path: 15 min (Feature works, core logic visible)
Error handling: 4 min (Shows robustness)
Result: Interviewer sees working feature + signal of quality.
```

### "Talk While Coding" Psychology

**Why interviewers want you talking:**
- They can't see your thinking (silent coding = black box)
- Communication is 50% of senior engineer skill
- If you're stuck, talking helps them guide you

**Script to start:**
```
"I'll use a ViewModel to manage state, a Repository to abstract the API,
and expose a StateFlow so the UI automatically updates. The ViewModel
launches a coroutine on the IO dispatcher to fetch data without blocking
the main thread. I'll use a sealed interface for UiState to represent
Success/Loading/Error states exhaustively."
```

Communicates:
- Architecture (ViewModel + Repository)
- Concurrency (coroutines, dispatcher)
- Safety (sealed interface, exhaustive when)
- User experience (reactive updates)

### Common Live-Code Mistakes & How to Fix

**Mistake 1: Forgetting viewModelScope**
```kotlin
// ❌ BAD: GlobalScope outlives ViewModel
GlobalScope.launch {
    val user = api.getUser()
}

// ✅ GOOD: Cancelled when ViewModel destroyed
viewModelScope.launch {
    val user = api.getUser()
}
```
**Signal:** Shows understanding of lifecycle, memory safety.

**Mistake 2: Blocking on Main**
```kotlin
// ❌ BAD: withContext still runs on Main (blocks UI)
withContext(Dispatchers.Main) {
    val data = expensiveComputation()  // ANR if too slow
}

// ✅ GOOD: Computation on IO, then Main update
val data = withContext(Dispatchers.IO) {
    expensiveComputation()
}
updateUI(data)  // Implicit Main (in ViewModel)
```
**Signal:** Shows understanding of threading, performance.

**Mistake 3: No error handling**
```kotlin
// ❌ BAD: Happy path only
_state.value = repo.getUser()  // Crashes on error

// ✅ GOOD: Distinguishes error types
try {
    _state.value = repo.getUser()
} catch (e: IOException) {
    _state.value = UiState.Error("Network unavailable")
} catch (e: Exception) {
    _state.value = UiState.Error("Unexpected error")
}
```
**Signal:** Shows production readiness, defensive coding.

### What it reuses & relies on

- **ViewModel lifecycle** — scope tied to ViewModel
- **Coroutine dispatchers** — threading model
- **Sealed interfaces** — exhaustive pattern matching
- **Kotlin syntax** — data classes, extension functions

### Why this design was chosen

**Interview context:** Limited time, high stakes. Prioritize visible working code over perfect abstraction.

**Interviewers evaluate:**
1. Can you solve the problem? (working code)
2. Do you know Android patterns? (ViewModel + Repository)
3. Are you production-ready? (error handling)
4. Can you communicate? (talk while coding)

Spending 70% time on happy path maximizes the chance of showing #1 and #2.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Clarify requirements first" | Ambiguous requirements = wrong solution. Asking shows senior thinking. |
| "Sketch before coding" | Architecture design before implementation. Prevents rewriting mid-interview. |
| "Time-box each section" | Happy path is 15/25 min because core logic matters most. Error handling is polish. |
| "Talk while coding" | Communication = part of assessment. Interviewer guides if you explain thinking. |

### Gotchas at depth

- **Over-engineering for time:** Building perfect architecture takes 10 min. Then no time for logic. Stick to ViewModel + Repository (boring is good).
- **Asking permission too much:** "Is it OK if I...?" costs time. Ask once (requirements), then code confidently.
- **Fixing typos and syntax:** Spend 10 min on `data class` syntax. Ask interviewer: "Remind me the order?" (saves time, shows humility).
- **Running code:** If no IDE, don't try to test. Pseudocode + logic is fine. Testing is separate from live-code signal.

</details>

### System Design Interview Structure

> **TL;DR:** 5-step interview: (1) Clarify scope—ask about scale, offline, real-time, conflicts (2 min). (2) Sketch architecture—Room + Repository + ViewModel (3 min). (3) Deep dive critical paths—load failures, sync conflicts (7 min). (4) Trade-offs—why these decisions (2 min). (5) Invite follow-up (1 min).

Clarify scope · Sketch architecture · Deep critical paths · Trade-offs · Invite follow-up

**Problem Example:** "Design an offline-capable user profile screen with sync."

**Time Allocation (15 min typical system design):**

| Step | Time | Action | Goal |
|---|---|---|---|
| **Clarify** | 2 min | Ask 4 questions | Define constraints |
| **Architecture** | 3 min | Sketch boxes/arrows | Show structure understanding |
| **Deep dive** | 7 min | Explain critical paths | Show depth, problem-solving |
| **Trade-offs** | 2 min | Why these decisions | Show judgment |
| **Follow-up** | 1 min | Invite questions | Show confidence, readiness |

**Example Clarifying Questions:**

<details>
<summary>💻 Code Example</summary>

```
"Before I design, let me ask:
1. Scale: How many users? Millions → need pagination and sharding?
2. Offline: Completely offline-first, or fetch on open?
3. Real-time: Real-time sync, or eventual consistency OK?
4. Conflicts: Last-write-wins, or ask user to resolve?
5. Updates: Who can edit? Just user, or admins too?"
```

</details>

**Architecture Sketch (3 min—draw on board):**

<details>
<summary>💻 Code Example</summary>

```
UI Layer (Compose)
     ↓ (observes StateFlow)
ViewModel (loads data, manages state)
     ↓ (requests via suspend funs)
Repository (abstraction layer)
     ├─ API Layer (Retrofit + OkHttp)
     └─ Local DB (Room + Coroutines)

Sync Layer (separate):
  WorkManager → Work Queue in Room → Sync Service → API
```

</details>

**Deep Dive: Critical Paths (7 min—talk through each):**

<details>
<summary>💻 Code Example</summary>

```
Scenario 1: First load, no internet
  → Room empty, API fails
  → Show empty state + "Retrying..."
  → When network returns, auto-fetch + cache in Room

Scenario 2: Offline edit, then sync
  → User edits profile (Room updated immediately)
  → WorkManager queues sync task
  → Network returns → execute sync
  → Conflict? Last-write-wins (server timestamp > local)

Scenario 3: Real-time: Other user updates profile
  → Server notifies via WebSocket (or poll)
  → Room invalidated + refetch
  → UI observes Room → auto-updates
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Why This Structure Works

**For interviewer:**
- Clarify: Shows you think before designing (not jumping to code)
- Architecture: Shows understanding of layering
- Deep dive: Shows you think through edge cases
- Trade-offs: Shows judgment (context matters)
- Invite follow-up: Shows confidence (not defensive)

**For candidate:**
- Scope limits prevents over-design
- Architecture gives talking points
- Deep dives show depth
- Trade-offs prevent "best possible" debates
- Follow-up invites guidance if stuck

### Common System Design Mistakes

**Mistake 1: Over-scoping**
```
Candidate designs: "Pagination, infinite scroll, lazy load, image caching,
video streaming, P2P sync, mesh networking, distributed consensus..."
Interviewer: "We have 15 minutes..."
Candidate: "Oh. I'll simplify."
Result: Too late. Interview derailed.
```

**Better:** Scope consciously. "Let me focus on offline-first with Room.
If time, we can add pagination."

**Mistake 2: No critical paths**
```
"So it's Repository → Room + API."
Interviewer: "What if both fail?"
Candidate: "Hmm... I didn't think about that."
Result: Shows lack of depth.
```

**Better:** Pre-think failure modes. "When API fails, we show cached + retry.
When cache missing, show empty state + fetch in background."

**Mistake 3: Defending design without trade-offs**
```
Interviewer: "Why Room as SSOT?"
Candidate: "Because it's better."
Interviewer: "Better how?"
Candidate: "It just is..."
Result: Shows weak judgment.
```

**Better:** "Room as SSOT because: (1) persists across process death,
(2) single consistency point, (3) simpler than distributed cache.
Alternative would be in-memory cache, but then we'd lose data on crash."

### What it reuses & relies on

- **Architecture patterns** (layered, dependency inversion)
- **Android components** (ViewModel, Repository, Room, WorkManager)
- **Concurrency** (coroutines, threading)
- **Consistency models** (eventual consistency, last-write-wins)

### Why this design was chosen

**Interview context:** 15-30 min to evaluate system design thinking.

**Interviewer assesses:**
1. Can you scope problems? (Clarify)
2. Do you know Android patterns? (Architecture)
3. Can you think through edge cases? (Deep dive)
4. Do you have good judgment? (Trade-offs)
5. Are you coachable? (Invite follow-up)

This structure demonstrates all five.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Clarify scope first" | Ambiguous requirements = wrong design. Interviewer tests whether you ask before diving. |
| "Use Room as SSOT" | Single source of truth simplifies consistency. Room survives process death (unlike caches). |
| "Sync offline writes" | WorkManager persists sync work across reboots. Room + timestamps enable conflict resolution. |
| "Show critical paths" | Edge cases (failures) matter more than happy path. Depth = system design thinking. |

### Gotchas at depth

- **Analysis paralysis:** Too many clarifying questions (10+) wastes time. Ask 4-5, then design.
- **Infinite scaling:** "What if 1B users?" Keep it practical. Use Paging 3 + server-side pagina pagination. Don't redesign entire backend.
- **Technology debates:** "But why not Firebase?" Stick to your choice. Defend briefly, move on.
- **Whiteboarding mistakes:** Don't erase. Cross out, draw on top. Interviewer wants to see your thinking process.

</details>

### How to Answer Architecture Questions

> **TL;DR:** Answer formula: (1) "I would..." [solution] (2) "Because..." [reasoning/trade-off] (3) "Alternative..." [option B] (4) "Choose A because..." [rationale]. Structured answers signal seniority—shows you think in trade-offs, not dogma.

Answer formula · Trade-offs first · Alternatives · Context matters · No dogma

**Interview Question Formula:**

| Question | Your Formula | Why It Works |
|---|---|---|
| "How would you...?" | "I would **[solution]**. Reasoning: **[why]**. Alternative: **[B]**. Choose A because **[rationale]**." | Shows depth: not just right answer, but why |
| "What do you prefer?" | "Depends on context. **[Scenario A]** → **[solution A]**. **[Scenario B]** → **[solution B]**." | Avoids dogma. Shows judgment. |
| "What's the problem with...?" | "The problem is **[specific issue]**. **[Real example]**. Solution: **[fix]**." | Specific, not vague. Backed by example. |

**Real Interview Examples:**

<details>
<summary>💻 Code Example</summary>

```
Q: "How would you handle a slow API?"
A: "I'd cache in Room with TTL. First load: fetch from API → save to Room.
   Subsequent loads: check Room first (instant). If stale (>1 hour), fetch
   fresh in background. If network fails, show cached + 'stale' indicator.
   Reasoning: Fast UX + reliability. Alternative: in-memory cache, but
   would lose on process death. Choose Room because persists + ACID."

Q: "MVI vs MVVM—which do you prefer?"
A: "Depends on complexity. Simple screens (list view): MVVM is simpler.
   Complex screens (search + filter + sort simultaneously): MVI's reducer
   pattern ensures one consistent state path. My last project: MVVM with
   custom logic for complex screen—worked, but MVI would've been cleaner.

Q: "How do you test ViewModel with async?"
A: "I inject a fake Repository returning known values. Use runTest builder
   (virtual clock). Assert state transitions: Loading → Success. Network
   error: Loading → Error. Why: Deterministic (no actual network), fast,
   covers error paths."
```

</details>

**Red Flags (What NOT to Say):**

- ❌ "Room is always better than..." (no always—depends on scale)
- ❌ "I never use GlobalScope" (yes you do, know when it's OK)
- ❌ "The best approach is..." (context matters—what's best for whom?)
- ❌ "Everyone should..." (no dogma in interviews)

### Reverse Questions to Ask

> **TL;DR:** Ask questions that show you're thinking about trade-offs and culture fit. For technical companies: deep technical questions (modularization, offline strategy). For product companies: growth/shipping questions. For team: "biggest challenge" signals you want to solve real problems, not just pass time.

Signal competence · Tailor to company · Cultural fit · Technical depth · Show interest

**Question Taxonomy:**

| Company Type | Why They Care | Your Question | Signal |
|---|---|---|---|
| **Technical** (Bolt, Blinkist) | Code quality, systems | "Modularization at scale? Convention plugins?" | You care about engineering |
| **Product-driven** (Babbel, N26) | Speed, market | "Feature velocity vs. tech debt?" | You understand business |
| **Early-stage** | Survival | "Biggest technical challenge?" | You want to impact |
| **Large** (Google, Meta) | Process, scale | "How do you handle X at scale?" | You think systems |

**Strong Technical Reverse Questions:**

<details>
<summary>💻 Code Example</summary>

```
"How do you handle modularization and Gradle build times at scale?
 Do you use convention plugins or manual configurations?"

"What's your current offline-first strategy? Do you handle sync
 conflicts, or do you rebuild from server on reconnect?"

"What's the biggest performance bottleneck on Android right now?
 Startup, rendering, or network? How do you measure it?"

"How do you test critical paths? Unit tests + integration tests +
 UI tests? Manual QA? Flakiness strategy?"
```

</details>

**Strong Cultural Reverse Questions:**

<details>
<summary>💻 Code Example</summary>

```
"What does success look like in the first 3 months?"

"What's the biggest technical challenge the team faces right now?"

"How does the team approach on-call? Is there a rotation? What's
 the escalation process?"

"How do you balance shipping fast with maintaining code quality?
 Any horror stories from moving too fast?"
```

</details>

**Red Flags (Don't Ask):**
- ❌ "What's the salary?" (save for recruiter or offer stage)
- ❌ "How many vacation days?" (not the time)
- ❌ "Will I work from home?" (OK to ask, but frame professionally)
- ❌ "Do you have ping-pong tables?" (signals you care about perks, not work)

**Strong Closer (Last 2 min):**
<details>
<summary>💻 Code Example</summary>

```
"This sounds like an exciting challenge. The offline-first + sync
 strategy is exactly the kind of problem I want to solve. I'm ready
 to roll up my sleeves and contribute."
```

</details>
Shows enthusiasm + confidence + willingness to work hard.

## 12. Strategic "Reverse" Questions

### For Bolt (Technical)

1. "What's your biggest **performance bottleneck** on Android — startup, rendering, or network? How do you measure it?"
2. "How does your team handle **modularization and build times** — convention plugins, monorepo?"

### For Babbel (Culture/Process)

1. "What's the biggest **challenge and win in KMP adoption** — how much logic do you share today?"
2. "How do Android and iOS teams **collaborate on shared KMP modules** — shared ownership or platform maintainers?"

---

## 13. Networking & API Design

### RESTful API Best Practices for Android

> **TL;DR:** Design APIs resource-oriented (`/users/123`), not RPC-style (`/getUser?id=123`). Use DTOs to map API responses, separate from domain models. Stateless + idempotent design enables safe retries.

REST principles · DTO ↔ Domain mapping · Stateless · Idempotent · Safe retries

**HTTP Method Contract:**

| Method | Safe to Retry | Idempotent | Use Case |
|---|---|---|---|
| **GET** | ✅ Yes | ✅ Yes | Fetch data (no side effects) |
| **PUT** | ✅ Yes | ✅ Yes | Update entire resource (replace) |
| **DELETE** | ✅ Yes | ✅ Yes | Remove resource (same result) |
| **POST** | ❌ No | ❌ No | Create (may duplicate) |
| **PATCH** | ❌ No | ❌ No | Partial update (depends on order) |

**Response shape for Android:**
<details>
<summary>💻 Code Example</summary>

```kotlin
// API response (server)
data class ApiResponse<T>(
    val success: Boolean,
    val data: T?,
    val error: String?
)

// DTO (maps API shape)
data class UserDto(val id: Int, val name: String)

// Domain model (app logic)
data class User(val id: Int, val name: String)

// Mapper (DTO → Domain)
fun UserDto.toDomain() = User(id, name)
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Stateless Design (Why It Matters)

**Stateful design (problematic):**
```
Client A: POST /users/{id}/follow → Server stores "A is following id"
Client A loses connection
Client A: Are you following? → Server: "checking my memory..." → ERROR
// Server state lost
```

**Stateless design (safe):**
```
Client A: POST /users/{id}/follow
  Request includes: user_id, token, timestamp
  Server: "User A wants to follow id. Token valid? Timestamp recent? → Update DB"
Client A reconnects: Same POST → Idempotent (already followed, no duplicate)
```

### DTO ↔ Domain Separation

**Why separate layers:**
```
API evolves: adds "createdAt" field
// Old code (tightly coupled):
data class User(val id: Int, val name: String, val createdAt: String)
// Must update EVERYWHERE

// Decoupled code:
data class UserDto(val id: Int, val name: String, val createdAt: String)  // Evolves
data class User(val id: Int, val name: String)  // Stable
// Domain logic unchanged
```

### Idempotency & Safe Retries

**Problem without idempotency:**
```
POST /transfer (transfer $100)
  ↓ (network timeout)
  ↓ Retry POST (same request)
  ↓ Server: "Transfer $100 again" → $200 transferred (ERROR!)
```

**Solution with idempotency:**
```
PUT /users/123 (replace user data)
  ↓ (network timeout)
  ↓ Retry PUT (same request)
  ↓ Server: "Replace user data" → Same result (SAFE!)

// Or: Idempotency key
POST /transfer with header: Idempotency-Key: abc123
  ↓ Server stores: "abc123 → transferred $100"
  ↓ Retry with same key: Server: "Already processed" → No duplicate
```

### What it reuses & relies on

- **HTTP standards** (RFC 7231) — method semantics
- **JSON serialization** (Gson, kotlinx.serialization)
- **Database transactions** — ensure idempotent updates are atomic

### Why this design was chosen

**Problem:** APIs change. Servers go down. Clients retry. Need safe, predictable behavior.

**Solution: REST principles**
- Stateless: clients carry all context (easier scaling)
- Idempotent: safe to retry (no duplicates)
- DTO/Domain split: decouples API from logic

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use /users/123 not /getUser?id=123" | REST = resource-oriented (nouns), not RPC (verbs). /users/{id} = resource path. |
| "PUT is idempotent, POST isn't" | PUT: same request = same result (replace). POST: same request = multiple results (create duplicate). |
| "Separate DTOs from domain" | DTO maps API schema. Domain model independent. API evolves; domain logic stable. |
| "Stateless design" | Server doesn't store client context. Client sends all data per request. Enables horizontal scaling. |

### Gotchas at depth

- **DELETE idempotency:** DELETE /users/123 twice. First: resource deleted. Second: resource already gone → 404. Still idempotent (same intended result). Handle 404 gracefully.
- **PATCH not idempotent:** PATCH /users/123 {"age": "+1"} → Increments age. Retry: age incremented again. Use PUT instead (replace whole resource).
- **DTO field order:** JSON deserialization order shouldn't matter (Gson handles it). But Parcelable/Serializable order-dependent. Use Gson, not Parcelable for network.
- **API versioning:** URL versioning (/v1/users vs /v2/users) or header versioning. Both have tradeoffs. Header cleaner (single endpoint), URL explicit (separate endpoints).

</details>

### Error Handling in Networking

> **TL;DR:** Use sealed interface (`ApiResult`) to represent Success/Failure/NetworkError. Distinguish network errors (retry) from HTTP errors (don't retry 4xx). Repository handles mapping; ViewModel observes result type.

Sealed interface · Network vs HTTP error · Retry strategy · Repository responsibility · Type-safe

<details>
<summary>💻 Code Example</summary>

```kotlin
sealed interface ApiResult<out T> {
    data class Success<T>(val data: T) : ApiResult<T>
    data class Failure(val code: Int, val message: String) : ApiResult<Nothing>
    data class NetworkError(val cause: Throwable) : ApiResult<Nothing>
}

class UserRepository(private val api: UserApi) {
    suspend fun getUser(id: Int): ApiResult<User> = try {
        val response = api.getUser(id)
        if (response.success) {
            ApiResult.Success(response.data.toDomain())
        } else {
            ApiResult.Failure(400, response.error ?: "Unknown")
        }
    } catch (e: IOException) {
        ApiResult.NetworkError(e)  // Network error (retry candidate)
    } catch (e: HttpException) {
        val code = e.code()
        val retryable = code >= 500  // 5xx (server error)
        ApiResult.Failure(code, e.message())
    } catch (e: Exception) {
        ApiResult.Failure(500, "Unexpected error")
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Exception Types in Retrofit + OkHttp

**Network-level errors (IOException - RETRYABLE):**
```kotlin
// What causes it:
// - No internet connectivity
// - DNS lookup fails
// - Socket timeout
// - Connection refused

try {
    api.getUser(123)
} catch (e: IOException) {  // Network layer error
    // Safe to retry
    // Repository should implement exponential backoff
}
```

**HTTP-level errors (HttpException - CONTEXT DEPENDENT):**
```kotlin
// What causes it:
// - Server responded with error status (4xx, 5xx)
// - Response parsing failed

try {
    api.getUser(123)
} catch (e: HttpException) {
    when (e.code()) {
        400, 401, 403, 404 -> return Failure(e.code(), "Don't retry - client error")
        500, 502, 503, 504 -> return Failure(e.code(), "Retry - server error")
    }
}
```

### ApiResult Pattern vs Exceptions

**Exception-based (old style):**
```kotlin
suspend fun getUser(id: Int): User {  // Throws on error
    return api.getUser(id)
}

// Caller must handle:
try {
    val user = repo.getUser(123)
    updateUI(user)
} catch (e: IOException) {
    showRetry()
} catch (e: HttpException) {
    showError(e.message())
}
```

**ApiResult-based (safe, recommended):**
```kotlin
suspend fun getUser(id: Int): ApiResult<User> {
    return try {
        ApiResult.Success(api.getUser(id))
    } catch (e: IOException) {
        ApiResult.NetworkError(e)
    } catch (e: HttpException) {
        ApiResult.Failure(e.code(), e.message())
    }
}

// Caller pattern-matches:
when (val result = repo.getUser(123)) {
    is ApiResult.Success -> updateUI(result.data)
    is ApiResult.Failure -> showError(result.message)
    is ApiResult.NetworkError -> showRetry()
}
```

**Why ApiResult better:**
- Exhaustive when (compiler enforces all cases)
- No unchecked exceptions
- Clear success/error paths

### Repository Responsibility for Error Handling

**Repository decides:**
1. Which errors are retryable (network errors → yes, 4xx → no)
2. How many retries (exponential backoff)
3. When to delegate to cache (on network error, serve stale)
4. How to map errors (API error codes → user messages)

**ViewModel doesn't:**
- Retry logic (Repository handles)
- Network vs HTTP distinction (Repository handles)
- Specific error messages (Repository handles)

### What it reuses & relies on

- **sealed interface** — exhaustive pattern matching
- **Retrofit interceptors** — can transform exceptions
- **OkHttp client** — throws IOException on network errors
- **Kotlin coroutines** — exception propagation in suspend functions

### Why this design was chosen

**Problem:** Exceptions hide error type (network vs HTTP). Caller can't decide retry strategy.

**Solution: ApiResult ADT**
- Distinguish error types explicitly
- Repository owns retry logic
- ViewModel observes result (exhaustive when)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "IOException = network error" | IOException from socket layer (DNS, timeout, disconnect). Thrown by OkHttp before HTTP response. |
| "HttpException = server responded" | HttpException only thrown if response status not 2xx. HTTP layer, after socket. |
| "Retry on network error, not 4xx" | Network = likely transient (retry helps). 4xx = client error (fix request first, retrying won't help). |
| "ApiResult exhaustive" | sealed interface forces all cases in when. Compiler error if missing. |

### Gotchas at depth

- **Retrofit success status range:** By default, 2xx-3xx = success. 4xx, 5xx throw HttpException. Can configure with custom success predicate.
- **Exception chain:** Retrofit wraps exceptions. e.cause may contain underlying IOException. Always check the chain.
- **Timeout exceptions:** SocketTimeoutException extends IOException. Treat as network error (retry). But increase timeout if consistently hitting it.
- **Error body parsing:** response.errorBody() is a stream (consume once). Don't parse multiple times or errors become null.

</details>

### Retry Strategy (Exponential Backoff)

> **TL;DR:** Exponential backoff = wait 100ms, 200ms, 400ms between retries (doubles each time). Prevents thundering herd when server recovers. Retry only network errors & 5xx; never 4xx. Max 3 retries (diminishing returns).

Exponential backoff · Jitter · Retry budget · Circuit breaker · Idempotent operations only

<details>
<summary>💻 Code Example</summary>

```kotlin
suspend inline fun <T> retryWithBackoff(
    maxRetries: Int = 3,
    initialDelayMs: Long = 100,
    block: suspend () -> T
): T {
    var lastException: Exception? = null
    repeat(maxRetries) { attempt ->
        try {
            return block()
        } catch (e: IOException) {
            lastException = e
            if (attempt < maxRetries - 1) {
                val delay = initialDelayMs * (2.0.pow(attempt)).toLong()
                delay(delay)  // 100ms, 200ms, 400ms
            }
        }
    }
    throw lastException!!
}

// Usage: immediate, 100ms, 200ms
val user = retryWithBackoff { api.getUser(123) }
```

</details>

| Scenario | Retry? | Reason |
|---|---|---|
| **IOException (no internet)** | ✅ Yes | Network transient; may recover |
| **HttpException 500, 503** | ✅ Yes | Server error; likely transient |
| **HttpException 401, 403, 404** | ❌ No | Client error; retrying won't help |

<details>
<summary>🔩 Under the Hood</summary>

### Exponential Backoff Mechanics

**Why exponential (not linear):**
```
Scenario: Server overloaded, recovers in 1 second

Linear backoff (50ms, 100ms, 150ms):
  ↓ All 1000 clients retry at similar times
  ↓ Server recovers but gets hammered again
  ↓ Cascading failure (thunder herd)

Exponential backoff (100ms, 200ms, 400ms):
  ↓ Clients spread out retries (early ones wait less, late ones wait more)
  ↓ Server recovers gradually
  ↓ Load distributes naturally
```

**Formula:**
```kotlin
delay = initialDelayMs * (2^attempt)  // 100ms * 2^0, 2^1, 2^2
// Attempt 0: 100 * 1 = 100ms
// Attempt 1: 100 * 2 = 200ms
// Attempt 2: 100 * 4 = 400ms
// Attempt 3: 100 * 8 = 800ms (but limited by maxRetries = 3)
```

### Jitter (Optional Enhancement)

**Problem with pure exponential:**
```
Clients A, B, C all start at T=0
All hit server error
All retry at T=100ms (synchronized thundering herd again)
```

**Solution: Add random jitter**
```kotlin
val delay = initialDelayMs * (2.0.pow(attempt)).toLong()
val jitter = Random.nextLong(delay)  // Random 0..delay
delay(delay + jitter)  // Spread out retries
```

### HTTP Status Code Retry Decision

**2xx-3xx (Success):** Don't retry (succeeded!)

**4xx (Client Error - DON'T RETRY):**
- 400: Bad request (invalid JSON)
- 401: Unauthorized (invalid token)
- 403: Forbidden (permission denied)
- 404: Not found (resource doesn't exist)

**5xx (Server Error - RETRY):**
- 500: Internal server error (may be transient)
- 502: Bad gateway (load balancer issue)
- 503: Service unavailable (temporarily down)
- 504: Gateway timeout (server slow)

### What it reuses & relies on

- **Kotlin delay()** — suspends coroutine (non-blocking sleep)
- **Math.pow()** — exponential calculation
- **Coroutine scope** — cancellation propagates through retries

### Why this design was chosen

**Problem:** Naive retries overload recovering servers (thundering herd). Retrying 4xx wastes time.

**Solution: Exponential backoff + smart decisions**
- Exponential: spreads out retries
- Smart: only retry transient errors

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Exponential backoff spreads retries" | 2^attempt grows delays. Prevents synchronized retries from multiple clients. |
| "Don't retry 4xx" | 4xx = client error (invalid input, auth). Retrying same request won't fix it. |
| "Max 3 retries" | More retries have diminishing returns. After 3 failures (~700ms), likely unrecoverable. |
| "delay() doesn't block" | Coroutine suspension. Thread remains free for other work (not Thread.sleep blocking). |

### Gotchas at depth

- **Retry storms:** Many clients retrying simultaneously. Use jitter to randomize timing. Server should send 429 (rate limit) to back off clients.
- **Timeout during retry:** If socket timeout + retry backoff both happen, cumulative delays multiply. Set socket timeout < total retry window.
- **Only retry idempotent ops:** GET, PUT, DELETE safe to retry. POST may duplicate. Use Idempotency-Key header if retrying POST.
- **Jitter overhead:** Adding jitter helps, but small delays (100ms) may not need it. Larger retry delays (1s+) benefit from jitter more.

</details>

### Connection Pooling & Keep-Alive

> **TL;DR:** Reuse TCP connections (keep-alive) instead of opening new ones. OkHttp pools connections automatically. Keep 5 idle connections, TTL 5 min. Timeout: 30s for connect/read/write. Reduces latency by 100-500ms per request.

Connection pooling · Keep-alive · TCP reuse · Timeout tuning · Idle connection cleanup

<details>
<summary>💻 Code Example</summary>

```kotlin
val httpClient = OkHttpClient.Builder()
    .connectTimeout(30, TimeUnit.SECONDS)   // TCP handshake timeout
    .readTimeout(30, TimeUnit.SECONDS)      // Waiting for response data
    .writeTimeout(30, TimeUnit.SECONDS)     // Sending request timeout
    .connectionPool(
        ConnectionPool(
            maxIdleConnections = 5,         // Keep 5 idle connections
            keepAliveDuration = 5,          // 5 minute TTL
            TimeUnit.MINUTES
        )
    )
    .build()

val retrofit = Retrofit.Builder()
    .client(httpClient)
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()
```

</details>

| Config | Default | Tuning | When |
|---|---|---|---|
| **connectTimeout** | 10s | 30s | Slow network, distant servers |
| **readTimeout** | 10s | 30s | Slow response, large payload |
| **keepAlive** | 5 min | Increase | High-frequency requests |
| **maxIdle** | 5 | Increase | High concurrency |

<details>
<summary>🔩 Under the Hood</summary>

### TCP Connection Lifecycle (Keep-Alive vs New)

**Without keep-alive (new connection per request):**
```
Request 1:
  T=0ms: SYN (client → server)
  T=10ms: SYN-ACK (server → client)
  T=20ms: ACK (client → server) — connection established
  T=25ms: HTTP GET (send request)
  T=100ms: HTTP 200 (receive response)
  T=110ms: FIN (close connection)
  Total: ~110ms (includes TCP overhead)

Request 2 (to same host):
  T=110ms: SYN (new connection)
  T=120ms: SYN-ACK
  T=130ms: ACK
  ... repeat overhead
  Total: ~110ms again
```

**With keep-alive (reuse connection):**
```
Request 1:
  T=0ms-20ms: TCP handshake (3-way)
  T=25ms: HTTP GET
  T=100ms: HTTP 200
  Connection stays open

Request 2 (reuses same connection):
  T=110ms: HTTP GET (no handshake!)
  T=150ms: HTTP 200
  Total: ~40ms (no TCP overhead)
  Savings: ~70ms (64% faster!)
```

### Connection Pool Management

**How OkHttp manages:**
```kotlin
// Pool stores:
// - Idle connections: ready to reuse
// - Active connections: currently in use
// - Max idle: 5 connections (default)
// - Keep-alive: 5 minutes (default)

// When request comes in:
if (pool.hasIdleConnection) {
    connection = pool.getIdle()  // Reuse (instant)
} else if (pool.size < maxIdleConnections) {
    connection = new Connection()  // Create new (TCP handshake)
} else {
    // Wait or create new (depends on config)
}

// After response:
if (response.canReuseConnection()) {
    pool.put(connection)  // Return to pool
} else {
    connection.close()  // Close
}

// Background: pool.evict() removes idle > TTL
```

### Timeout Configuration

**connectTimeout (socket handshake):**
```kotlin
.connectTimeout(30, TimeUnit.SECONDS)
// If server doesn't respond to SYN-ACK in 30s, fail
// Typical: 10-30s (default 10s)
```

**readTimeout (waiting for response):**
```kotlin
.readTimeout(30, TimeUnit.SECONDS)
// If no data received for 30s, fail
// For large payloads (download), increase
// Typical: 10-30s (default 10s)
```

**writeTimeout (sending request):**
```kotlin
.writeTimeout(30, TimeUnit.SECONDS)
// If request not fully sent in 30s, fail
// Rarely needed (requests small)
// Typical: 10-30s (default 10s)
```

### Connection Pool Contention

**Problem: Too few idle connections**
```
5 concurrent requests, only 3 idle connections
→ 2 requests wait for idle connection
→ Latency spikes
```

**Solution: Increase pool size**
```kotlin
connectionPool(ConnectionPool(maxIdleConnections = 10, ...))
// Trade-off: more memory, better concurrency
```

### What it reuses & relies on

- **TCP keep-alive** (SO_KEEPALIVE socket option) — OS level keep-alive
- **HTTP persistent connections** (Connection: keep-alive header)
- **OkHttp interceptors** — can inspect pool stats

### Why this design was chosen

**Problem:** TCP handshake (3-way) adds 20-100ms latency per request. Wasteful if requests frequent.

**Solution: Connection pooling**
- Reuse TCP connections (amortize handshake)
- Keep-alive: idle connections stay open (short TTL)
- Reduces latency by 50-90% for high-frequency APIs

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Keep-alive reuses connections" | TCP connection stays open after response. Next request reuses same socket (no handshake). |
| "Connection pool holds idle connections" | OkHttp maintains pool of idle sockets. New request reuses from pool (if available) or creates new. |
| "Timeout prevents hanging" | connectTimeout catches hung handshakes. readTimeout catches slow servers. Both use SO_TIMEOUT socket option. |
| "Max idle = pool size" | More idle connections = faster reuse, but more memory. Trade-off based on concurrency (5 for most apps). |

### Gotchas at depth

- **Stale connection reuse:** Connection idle for 5 min might be closed by proxy/firewall. OkHttp retries automatically on stale connection error.
- **Proxy/firewall interference:** Some proxies reset idle connections sooner than 5 min. Reduce TTL if seeing connection resets.
- **Thread safety:** OkHttp pool is thread-safe (internal locks). Safe to share single client across threads.
- **Connection limits:** Server may limit connections per IP. If hitting server's limit, reduce maxIdleConnections to prevent exhausting server's file descriptors.

</details>

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

## 16. Jetpack Compose Advanced Patterns

### Modifiers & Custom Layout

> **TL;DR:** Modifier order matters — applied *right to left* (last = outermost). Use `composed {}` for stateful modifiers. `CustomLayout` for manual measurements (LayoutModifier internals).

Modifier chain · Composed modifier · CustomLayout · Measurement/Placement · Layout inspection

**Modifier order matters — left to right application:**
<details>
<summary>💻 Code Example</summary>

```kotlin
Box(
    Modifier
        .size(100.dp)           // First: set size
        .background(Color.Blue) // Then: color inside box
        .border(2.dp, Black)    // Then: border outside
        .padding(8.dp)          // Then: padding between border & content
)
// Order reversed = visual order (rightmost = outermost)
```

</details>

**Custom modifier:**
<details>
<summary>💻 Code Example</summary>

```kotlin
fun Modifier.shimmer() = composed {
    val infinite = rememberInfiniteTransition()
    val alpha by infinite.animateFloat(
        initialValue = 0.3f,
        targetValue = 0.9f,
        animationSpec = infiniteRepeatingSpec(
            animation = tween(1000),
            repeatMode = RepeatMode.Reverse
        )
    )
    alpha(alpha)
}

// Usage: Modifier.shimmer().background(Gray)
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Modifier Chain Execution (Right-to-Left)

**Visual order vs execution order:**
```kotlin
Box(
    Modifier
        .padding(8.dp)          // Applied 3rd
        .border(2.dp, Black)    // Applied 2nd
        .background(Color.Blue) // Applied 1st (outermost)
)

// Execution: padding → border → background
// Visual: background [outermost] → border → padding [innermost]
```

**Why reversed?**
- Each Modifier wraps the next
- padding(8) wraps border(2)
- border(2) wraps background()
- Result: background as outermost layer

**Real-world impact:**
```kotlin
// ❌ Wrong: padding inside background
Modifier
    .background(Color.Blue)
    .padding(8.dp)  // Padding outside box

// ✅ Right: padding outside background
Modifier
    .padding(8.dp)
    .background(Color.Blue)  // Padding wraps background
```

### Composed Modifier Pattern

**Without `composed`** (broken):
```kotlin
fun Modifier.badShimmer() = this.then(
    alpha(0.5f)  // Static value, no animation
)
```

**With `composed`** (correct):
```kotlin
fun Modifier.shimmer() = composed {  // Lambda creates new modifier per use
    val infinite = rememberInfiniteTransition()
    val alpha by infinite.animateFloat(...)
    alpha(alpha)  // Alpha animates
}
// Each use of .shimmer() gets its own animation state
```

**Why `composed` needed:**
- `remember {}` only works inside `@Composable`
- Direct modifier = non-composable (no `remember`)
- `composed {}` converts modifier DSL to composable context

### What it reuses & relies on

- **Modifier.then()** — chains modifiers
- **LayoutModifier interface** — measurement/placement
- **remember/rememberInfiniteTransition** — state management in composed modifiers
- **Recomposition system** — animating modifiers trigger recomposition

### Why this design was chosen

**Problem:** Modifiers need to layer (padding outside background).

**Solution:** Chain pattern (fluent API). Last modifier called = first applied (reverse).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Modifier order matters" | Chain is applied right-to-left; each modifier wraps previous (Decorator pattern) |
| "Use composed for animations" | `composed {}` creates new modifier instance per use; `remember` scoped to that instance |
| ".padding.background looks wrong" | Padding applied 2nd (after background); visually appears outside. Reverse order if want padding inside. |
| "Custom modifiers use LayoutModifier" | LayoutModifier.measure(constraints) → layout(w, h) → measure children, place them. |

### Gotchas at depth

- **Recomposition in composed:** If anything inside `composed {}` changes, entire modifier recomputed (may reset animations).
- **Multiple uses of same modifier:** Each use creates separate state (good for reusability, but watch for unintended duplication).
- **Drawing order:** Modifiers draw in applied order. Last modifier = drawn on top. Easy to hide content accidentally.

</details>

### Compose Effects: LaunchedEffect, DisposableEffect, SideEffect

> **TL;DR:** LaunchedEffect for async work (coroutines). DisposableEffect for listeners (with cleanup). SideEffect for side effects after recomposition. Choose based on lifecycle + cleanup needs.

`LaunchedEffect` async · `DisposableEffect` cleanup · `SideEffect` post-recompose · `Key-driven` · `Cancellation safety`

<details>
<summary>💻 Code Example</summary>

```kotlin
// LaunchedEffect: fetch on userId change
LaunchedEffect(userId) {
    val user = repo.getUser(userId)
    updateUI(user)  // Cancelled if userId changes
}

// DisposableEffect: listener with cleanup
DisposableEffect(Unit) {
    repo.subscribe(listener)
    onDispose { repo.unsubscribe(listener) }  // Always called
}
```

</details>

| Effect | Triggers | Cleanup | When to Use |
|---|---|---|---|
| **LaunchedEffect** | Key change (enters once per key) | Coroutine cancelled | Async work, API calls, Flow collection |
| **DisposableEffect** | Enters scope | onDispose block | Listeners, observers, state registration |
| **SideEffect** | After every recomposition | None | Analytics, logging, non-Compose state |
| **remember** | Composition tree slot | Never | Cache expensive computations |

<details>
<summary>🔩 Under the Hood</summary>

### LaunchedEffect lifecycle & cancellation

**What happens:**
```kotlin
LaunchedEffect(userId) {  // Key = userId
    val user = repo.getUser(userId)  // API call starts
    updateUI(user)
}

// Execution timeline:
// 1. Composable enters: LaunchedEffect block starts (launches coroutine in scope)
// 2. userId unchanged: block runs to completion, nothing happens
// 3. userId changes: CURRENT coroutine cancelled (CancellationException), NEW block launches with new userId
// 4. Composable leaves: coroutine cancelled (scope cleared)
```

**Cancellation safety:**
```kotlin
LaunchedEffect(userId) {
    try {
        val user = repo.getUser(userId)  // If cancelled here, exception thrown
        updateUI(user)  // If cancelled here, updateUI not called
    } catch (e: CancellationException) {
        // Cleanup happens automatically (scope handles it)
        throw e  // Re-throw (required by coroutine protocol)
    }
}
```

### DisposableEffect cleanup semantics

**Execution order:**
```kotlin
@Composable
fun Screen() {
    DisposableEffect(Unit) {
        println("Enter")  // Called when composable enters
        val listener = MyListener()
        repo.subscribe(listener)

        onDispose {  // Called when:
            println("Exit")  // 1. Composable leaves
            repo.unsubscribe(listener)  // 2. Key changes
            // 3. Parent recomposition
        }
    }
}

// Typical flow:
// Enter Screen → "Enter" printed, listener subscribed
// Leave Screen → "Exit" printed, listener unsubscribed
```

**Key difference from LaunchedEffect:**
- LaunchedEffect: Coroutine (async, cancellable)
- DisposableEffect: No async (synchronous), explicit cleanup

### SideEffect: Run after all recompositions

```kotlin
@Composable
fun Counter(count: Int) {
    SideEffect {
        println("Count is now $count")  // Called after EVERY recomposition
        analytics.logEvent("count_changed", mapOf("value" to count))
    }
}

// Execution:
// First render (count=0): SideEffect runs → "Count is now 0"
// User taps button (count=1): Recomposition → SideEffect runs → "Count is now 1"
// Repeat...
```

**Use carefully:** SideEffect runs on every recomposition (not just when recomposing). Use only for critical side effects.

### What each reuses & relies on

**LaunchedEffect:**
- Coroutine scope (composable lifecycle tied to CoroutineScope)
- Job cancellation mechanism
- Structured concurrency

**DisposableEffect:**
- Composition lifecycle callbacks
- cleanup/disposal pattern (observer)
- No coroutines (synchronous execution)

**SideEffect:**
- Composition snapshot mechanism
- Runs after snapshot applied (guaranteed state is stable)

### Why this design was chosen

**LaunchedEffect for async:**
- Async work (API calls) shouldn't block recomposition
- Key-driven re-execution lets you re-run async when deps change
- Cancellation prevents memory leaks

**DisposableEffect for listeners:**
- Listeners need cleanup (important!)
- synchronous, not async (listeners usually sync)
- onDispose guaranteed called (can't be skipped like finally in Kotlin)

**SideEffect for analytics:**
- Some side effects must happen after recomposition (when state stable)
- Not for heavy work (runs too frequently)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "LaunchedEffect runs once per key" | Coroutine launched in composable scope. Key change → previous cancelled, new launched. Composable leave → scope cleared. |
| "DisposableEffect has onDispose" | onDispose ALWAYS called: when leaving, key changes, or parent recomposes. Guaranteed cleanup. |
| "Don't update vars in recomposition" | Recomposition runs multiple times per frame (can run N times). Only use State<T> or remember. |
| "SideEffect runs after recomposition" | Runs AFTER snapshot applied (state stable). Use sparingly; runs frequently. |

### Gotchas at depth

- **LaunchedEffect with mutable state:** If lambda captures mutable state that changes, captures old value. Use derivedStateOf or key on state value.
- **DisposableEffect with lazy init:** onDispose can access state captured in Effect. If state becomes null, NullPointerException in cleanup. Use safe casts.
- **SideEffect overhead:** Runs after EVERY recomposition (including parent changes, theme changes, etc.). Heavy work = jank. Consider remember + callback instead.
- **Multiple effects order:** Multiple LaunchedEffect blocks in same composable run in order. DisposableEffect cleanup runs in REVERSE order (stack discipline).

</details>

### Snapshotting State & Stability Tricks

> **TL;DR:** Snapshot system captures state at recomposition. Immutable data prevents unnecessary recompositions (Stability = Compose can skip recomposition if args didn't change). Use `@Stable` or immutable collections to optimize.

Snapshot isolation · Stability · `@Stable` annotation · Immutable collections · Recomposition skipping

**Problem:** State mutates mid-recomposition → UI flickers.

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ Bad: Mutable list causes recompositions
val items = listOf(1, 2, 3)  // New list instance every recomposition
LazyColumn {
    items(items) { ItemRow(it) }  // params changed = child recompose
}

// ✅ Good: Cache list or use immutable
val items = remember { listOf(1, 2, 3) }
// Or use kotlinx-collections-immutable
val items: ImmutableList<Int> = persistentListOf(1, 2, 3)
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Snapshot System for State Isolation

**What happens during recomposition:**
```
Before recomposition: snapshot A (all state values frozen)
  ↓
Recomposition runs (might read new state)
  ↓
After recomposition: snapshot B (new state values captured)
  ↓
If recomposition fails: revert to snapshot A (atomic)
```

**State mutations:**
```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }

    // Snapshot A: count = 0
    Button(onClick = { count++ }) {  // Mutation happens
        // Snapshot B: count = 1
        Text("$count")
    }
    // Recomposition re-renders with count = 1
}
```

### Stability & Recomposition Skipping

**Composable params marked `@Stable`:**
```kotlin
@Stable
data class User(val id: Int, val name: String)

@Composable
fun UserCard(user: User) {  // Param is @Stable
    Text(user.name)
}

// Compose tracks: if User instance didn't change, skip recomposition
```

**Without @Stable:**
```kotlin
data class User(val id: Int, val name: String)  // Not marked @Stable

// Every parent recomposition → UserCard recomposition (even if User same)
```

**Performance impact:**
```
Unstable params: LazyColumn with 100 items + parent updates
  → All 100 items recompose (even if items param unchanged)
  → Jank

Stable params: LazyColumn with 100 items + parent updates
  → 0 items recompose (Compose skipped them)
  → Smooth
```

### Immutable Collections & Stability

**kotlinx-collections-immutable:**
```kotlin
val items: ImmutableList<Int> = persistentListOf(1, 2, 3)
// ImmutableList is @Stable (compile-time marker)

@Composable
fun ItemList(items: ImmutableList<Int>) {  // Param is stable
    LazyColumn {
        items(items) { item -> ItemRow(item) }
    }
}
// Compose skips recomposition if items unchanged (persistent reference)
```

**Why immutable helps:**
- Reference equality = instance didn't change
- Instance didn't change = safe to assume content unchanged
- Compose skips recomposition

**Mutable list problem:**
```kotlin
val items = mutableListOf(1, 2, 3)  // Mutable, not @Stable

@Composable
fun ItemList(items: MutableList<Int>) {  // Param unstable
    // Every parent recomposition → recomposes (unsafe to skip)
    // Even if items.add() never called
}
```

### What it reuses & relies on

- **Kotlin data class equality** — reference equality for stability checks
- **State machine** — tracks which composables ran, which can skip
- **Snapshot infrastructure** — transactional state updates
- **kotlinx-collections-immutable** — @Stable persistent data structures

### Why this design was chosen

**Problem:** Recomposition expensive. Need to skip unnecessary recomposition safely.

**Solution: Stability markers + snapshots.**
- @Stable = "this object is immutable (reference stable)"
- Snapshot = "capture state atomically"
- Skip recomposition = "if stable args unchanged, don't recompose"

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Mutable params cause recompositions" | Mutable = unstable = Compose can't skip. Even if content unchanged, reference is new. |
| "Use persistent collections" | ImmutableList marked @Stable; reference equality sufficient for stability checks. |
| "Snapshot captures state" | Snapshot = frozen view of state at recomposition moment. Mutations applied atomically to new snapshot. |
| "@Stable on data classes" | Compiler trusts @Stable = immutable. Recomposition skipped if instance unchanged. |

### Gotchas at depth

- **Manual @Stable misuse:** Marking mutable class @Stable = lie to compiler. Recomposition skipped, but state mutated. Use only for truly immutable types.
- **Reference equality != content equality:** Same data, different instance = recompose. Pass same instance via remember {} or memoize.
- **Snapshot cycles:** If recomposition triggers state update (circular), Compose detects and errors. Avoid LaunchedEffect → state.value update in same frame.
- **Persistent collection overhead:** ImmutableList adds indirection (linked lists). Fast reference equality, slightly slower iteration. Trade-off worth it for recomposition skipping.

</details>

---

## 17. Room Database Advanced Patterns

### Migrations & Schema Evolution

> **TL;DR:** Room migrations handle schema version bumps. Define `Migration(oldVersion, newVersion)` with SQL. Always test migrations (data loss + crashes common if untested). Use `@Query @PrimaryKey` to catch schema mismatches at compile-time.

Migration path · `ALTER TABLE` · Schema versioning · Test migrations · Data loss risks

<details>
<summary>💻 Code Example</summary>

```kotlin
val database = Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .addMigrations(MIGRATION_1_2, MIGRATION_2_3)
    .build()

val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        // Add new column
        db.execSQL("ALTER TABLE users ADD COLUMN created_at INTEGER NOT NULL DEFAULT ${System.currentTimeMillis()}")
    }
}

val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(db: SupportSQLiteDatabase) {
        // Rename table
        db.execSQL("ALTER TABLE users RENAME TO user_profiles")
        // Create index for performance
        db.execSQL("CREATE INDEX idx_user_email ON user_profiles(email)")
    }
}
```

</details>

**Best practice:** Test migrations!
<details>
<summary>💻 Code Example</summary>

```kotlin
@RunWith(AndroidTestRunner::class)
class MigrationTest {
    @Rule val helper = MigrationTestHelper(InstrumentationRegistry.getContext(), AppDatabase::class.java)

    @Test
    fun migrate1To2() {
        var db = helper.createDatabase("app.db", 1)
        db.execSQL("INSERT INTO users VALUES (1, 'Alice')")
        db.close()

        db = helper.runMigrationsAndValidate("app.db", 2, true, MIGRATION_1_2)
        val cursor = db.query("SELECT * FROM users")
        assertTrue(cursor.moveToFirst())
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### SQLite ALTER TABLE Limitations

**What you CAN'T do in SQLite:**
```sql
ALTER TABLE users DROP COLUMN email;        // ❌ Not supported
ALTER TABLE users MODIFY COLUMN name TEXT;  // ❌ Not supported
ALTER TABLE users CHANGE COLUMN ...         // ❌ Not supported (MySQL only)
```

**SQLite workaround (copy pattern):**
```sql
-- Step 1: Create new table with new schema
CREATE TABLE users_new (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    -- email column removed
);

-- Step 2: Copy data (no email)
INSERT INTO users_new (id, name) SELECT id, name FROM users;

-- Step 3: Drop old table
DROP TABLE users;

-- Step 4: Rename new table
ALTER TABLE users_new RENAME TO users;
```

**Room example:**
```kotlin
val MIGRATION_drop_email = object : Migration(3, 4) {
    override fun migrate(db: SupportSQLiteDatabase) {
        // Step 1-4 above
        db.execSQL("CREATE TABLE users_new (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        db.execSQL("INSERT INTO users_new SELECT id, name FROM users")
        db.execSQL("DROP TABLE users")
        db.execSQL("ALTER TABLE users_new RENAME TO users")
        db.execSQL("CREATE INDEX idx_user_name ON users(name)")
    }
}
```

### Schema Version Tracking

**In Room:**
```kotlin
@Database(
    entities = [User::class],
    version = 3  // Current schema version
)
abstract class AppDatabase : RoomDatabase() { ... }
```

**On device (first run with version 3):**
```
SQLite PRAGMA user_version = 3
  ↓
User opens app with version 3 code
  ↓
Room checks: version on device vs code version
  ↓
If match: no migration needed
  ↓
If device version < code version: apply migrations
  ↓
If device version > code version: error (new app, old DB)
```

### Migration Strategies

**Strategy 1: Linear chain**
```
Version 1 → 2 → 3 → 4 (each migration supplied)
```
Most reliable; requires all intermediate migrations.

**Strategy 2: Destructive** (nuke old data)
```kotlin
.fallbackToDestructiveMigration()  // Delete all data
```
Fast, but users lose data. Only for dev/testing.

**Strategy 3: Destructive on downgrade**
```kotlin
.fallbackToDestructiveMigrationOnDowngrade()
```
User downgraded app → nuke DB. Risky (data loss).

### What it reuses & relies on

- **SQLite PRAGMA user_version** — stores schema version on device
- **SQLite transaction system** — migrations atomic (all-or-nothing)
- **Room schema inspection** — `.schema` file tracks entity definitions
- **Cursor/ResultSet** — iterates rows for copy-paste logic

### Why this design was chosen

**Problem:** App updates add/change schema. Users' old DBs must upgrade without losing data.

**Solution: Migrations.**
- Version number tracks schema state
- Migrations explicitly define transformation
- Atomic transactions ensure consistency

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Add Migration for schema changes" | Room reads PRAGMA user_version; runs migrations in order until current version reached. |
| "Test migrations" | MigrationTestHelper creates old DB, applies migration, verifies schema. Catches data loss bugs. |
| "Can't drop columns in SQLite" | SQLite lacks DROP COLUMN. Workaround: copy table (with new schema), drop old, rename new. |
| "Fallback to destructive" | Nukes DB if migration not provided. Users lose data. Only use for dev. |

### Gotchas at depth

- **Missing migration:** If user on version 1, app is version 3, but migration 2→3 missing. Room crashes. Always supply all intermediate migrations.
- **Data type changes:** Changing column type (TEXT → INTEGER) requires copy (no direct ALTER). Conversion bugs (invalid cast) crash migration.
- **Foreign key constraints:** ALTER TABLE with FK references risky. Disable FK temporarily: `PRAGMA foreign_keys = OFF`, then re-enable.
- **Performance:** Large tables (millions of rows) = slow migrations (copy entire table). Migration can take minutes; user sees "app updating..." UI.

</details>

### Query Optimization: N+1 Prevention

> **TL;DR:** N+1 = fetch 1 user, then N queries for posts (1 + N queries total). Fix: use JOIN in SQL or Room @Relation (auto-joins). Massive performance difference at scale.

`N+1 problem` · `JOIN optimization` · `@Relation` auto-join · `Scale matters` · `Single query vs N queries`

<details>
<summary>💻 Code Example</summary>

```kotlin
// ❌ N+1 Performance Disaster
val users = db.getUsers()           // Query 1
for (user in users) {
    user.posts = db.getPostsByUserId(user.id)  // Queries 2...N+1 (one per user)
}
// Total: 1 + N queries. With 100 users = 101 queries!

// ✅ Solution 1: SQL JOIN (single query)
@Query("""
    SELECT u.*, p.* FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
""")
suspend fun getUsersWithPosts(): List<UserWithPosts>

// ✅ Solution 2: Room @Relation (Room handles join)
@Query("SELECT * FROM users")
suspend fun getUsersWithPosts(): List<UserWithPosts>
```

</details>

| Problem | Queries | Time (100 users) |
|---|---|---|
| **N+1** | 101 (1 + 100) | ~500ms (100 DB round-trips) |
| **JOIN** | 1 | ~5ms (single query) |
| **Speedup** | ~100x | ~100x improvement |

<details>
<summary>🔩 Under the Hood</summary>

### SQLite JOIN execution

**Query plan (N+1):**
```sql
SELECT * FROM users                    -- 1 scan: full table scan → 100 rows
                                       -- Application loops:
SELECT * FROM posts WHERE user_id = 1 -- Round-trip to DB
SELECT * FROM posts WHERE user_id = 2 -- Round-trip to DB
...
SELECT * FROM posts WHERE user_id = 100 -- Round-trip to DB

Total: 101 queries, 101 round-trips
```

**Query plan (JOIN):**
```sql
SELECT u.id, u.name, p.id, p.title, p.user_id
FROM users u
LEFT JOIN posts p ON u.id = p.user_id
-- Single query execution:
-- 1. Scan users table (100 rows)
-- 2. For each row, find matching posts (B-tree index lookup on user_id)
-- 3. Return all rows (1 query result, multiple rows per user)

Total: 1 query, 1 round-trip
```

### Room @Relation implementation

**What you write:**
```kotlin
data class UserWithPosts(
    @Embedded val user: User,
    @Relation(
        parentColumn = "id",
        entityColumn = "user_id"
    )
    val posts: List<Post>
)

@Query("SELECT * FROM users WHERE id = :userId")
suspend fun getUserWithPosts(userId: Int): UserWithPosts
```

**What Room generates:**
```kotlin
// Room creates wrapper query:
suspend fun getUserWithPosts(userId: Int): UserWithPosts {
    val user = db.query("SELECT * FROM users WHERE id = ?", userId)
    val posts = db.query("SELECT * FROM posts WHERE user_id = ?", user.id)
    return UserWithPosts(user, posts)
}
```

**Note:** @Relation still does 2 queries (one per entity type), but Room batches them efficiently (not loop-based N+1).

### Batch loading optimization

**Better than @Relation (for lists):**
```kotlin
@Query("""
    SELECT u.*, p.* FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
    ORDER BY u.id, p.id
""")
suspend fun getUsersWithPostsBatch(): List<UserWithPosts>

// Room cursor parsing:
// Cursor rows: (user1, post1), (user1, post2), (user2, post3)...
// Room groups by user, builds UserWithPosts objects
// Single query, cursor handles grouping
```

### What it reuses & relies on

- **SQLite query optimizer** — chooses index-based join strategy
- **B-tree indices** — fast lookups on foreign key columns
- **Cursor/ResultSet** — iterates query results
- **Room cursor parsing** — groups results by parent entity

### Why N+1 is so bad

**Scaling:**
- 10 users: 11 queries (not noticeable)
- 100 users: 101 queries (visible lag)
- 1000 users: 1001 queries (crash/timeout)

**Network overhead:** Each query = HTTP round-trip (if remote). 100 queries = 100 round-trips (seconds of latency).

**SQLite overhead:** Each query = parsing + planning + execution. 100 simple queries slower than 1 complex query (plan reuse).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "N+1 is bad" | N+1 = 1 query (parent) + N queries (children). Total = N+1 queries. Cursor/network round-trips = O(N). |
| "Use JOIN to fix" | JOIN combines tables in single query. SQLite index-joins parent+children efficiently (B-tree lookups). Single query = single round-trip. |
| "@Relation does auto-join" | Room still issues 2 queries (one per entity), but batches them (not loop-based). Still faster than N+1 loop. |
| "Performance matters" | 100x difference at scale. 100 queries = seconds. 1 query = milliseconds. |

### Gotchas at depth

- **JOIN result explosion:** If user has 100 posts, JOIN returns 100 rows (one per post). Room cursor parsing groups back into 1 UserWithPosts. Large result sets can be slow.
- **LEFT vs INNER:** LEFT JOIN keeps users without posts. INNER JOIN drops them. Choose based on use case (usually LEFT for "get all users").
- **Complex grouping:** Room handles simple 1-to-N. Complex N-to-N relationships need manual cursor handling (rare but possible).
- **Pagination with JOIN:** LIMIT 10 on JOIN counts result rows (100 posts per user = only 1 user returned). Use DISTINCT or window functions.

</details>

### Transactions & Atomicity

> **TL;DR:** `@Transaction` wraps multiple queries in SQLite transaction (all succeed or all fail). Use for multi-step operations (insert user → insert posts). Atomicity prevents partial updates (user created, posts failed = data corruption).

ACID properties · All-or-nothing · Rollback on error · SQLite transaction · `@Transaction` annotation

<details>
<summary>💻 Code Example</summary>

```kotlin
@Transaction  // All-or-nothing
suspend fun updateUserAndPosts(user: User, posts: List<Post>) {
    insertUser(user)       // Succeeds
    insertPosts(posts)     // Fails → rollback both
    // If any fails, entire operation reverts
}

// Manual transaction
db.withTransaction {
    insertUser(user)
    insertPosts(posts)
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### SQLite ACID Properties

**Atomicity (all-or-nothing):**
```kotlin
db.withTransaction {
    insertUser(User(1, "Alice"))        // Step 1
    insertPost(Post(1, 1, "Hello"))     // Step 2
    throw Exception("Oops!")             // Step 3: ERROR
    // Rollback: both insert operations undone
}
// User AND Post NOT in DB (atomic)
```

**Consistency (valid state before & after):**
```sql
-- Before transaction:
-- users: [User(1, "Alice")]
-- posts: []
-- Constraint: every post.user_id must exist in users

-- During transaction (ERROR):
-- Cannot create post with non-existent user_id
-- Constraint violation prevented

-- After transaction (rolled back):
-- Same state as before (consistent)
```

**Isolation (concurrent transactions):**
```
User A transaction: START → read user balance (100)
  ↓
User B transaction: START → deduct 50 (balance now 50)
  ↓
User A transaction: deduct 30 → ?
  // A sees 100 or 50? Depends on isolation level
```

**Durability (written to disk):**
```
INSERT user → SQLite writes to disk
  ↓
Power loss / crash
  ↓
On recovery: INSERT persisted (durable)
```

### @Transaction Mechanics

**What Room generates:**
```kotlin
@Transaction
suspend fun updateUserAndPosts(user: User, posts: List<Post>) {
    // Room generates:
    // BEGIN TRANSACTION
    insertUser(user)
    insertPosts(posts)
    // COMMIT (if no errors)
    // or ROLLBACK (if exception)
}
```

**Manual equivalent:**
```sql
BEGIN TRANSACTION;
INSERT INTO users VALUES (...);
INSERT INTO posts VALUES (...);
-- If error anywhere:
ROLLBACK;
-- If success:
COMMIT;
```

### Isolation Levels (Concurrent Transactions)

**Read Uncommitted (dirty reads possible):**
```
Transaction A: INSERT user(balance=100)
Transaction B: SELECT balance → 100 (before commit)
Transaction A: ROLLBACK
// B saw "dirty" data (never committed)
```

**Read Committed (default in SQLite via WAL):**
```
Transaction A: INSERT user(balance=100), COMMIT
Transaction B: SELECT balance → 100 (only committed data)
// B only sees committed data (safe)
```

**SQLite isolation (WAL mode):**
- Write-Ahead Logging (WAL)
- Readers see consistent snapshot
- Writers don't block readers (separate WAL file)
- Room uses WAL by default

### Rollback Strategy

**Exception triggers rollback:**
```kotlin
db.withTransaction {
    insertUser(user)         // Success: in transaction buffer
    throw IOException()       // Exception: ROLLBACK triggered
    insertPost(post)         // Never reached
}
// Both insertions undone (atomic)
```

**Resource cleanup (try-finally):**
```kotlin
db.withTransaction {
    try {
        insertUser(user)
        insertPost(post)
    } finally {
        // Cleanup code (transaction still active)
        // Rollback happens AFTER finally
    }
}
```

### What it reuses & relies on

- **SQLite transaction system** — BEGIN/COMMIT/ROLLBACK
- **Write-Ahead Logging (WAL)** — isolation + concurrency
- **SQLite savepoints** — nested transactions (savepoint/release)
- **Room suspend functions** — async I/O with coroutine scope

### Why this design was chosen

**Problem:** Multiple operations must be all-or-nothing. One failure = data corruption.

**Example:** Transferring money
```
Account A: -$100
Account B: +$100
// Both must succeed, or both must fail
// If B fails after A debited: money vanishes
```

**Solution: Transactions.**
- Wrap all operations
- If any fails: rollback all
- Database stays consistent

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "@Transaction makes all-or-nothing" | Room wraps function in BEGIN/COMMIT (or ROLLBACK). SQLite atomically applies all or none. |
| "Rollback undoes changes" | SQLite reverts all changes to transaction snapshot if error occurs. |
| "Concurrent transactions" | WAL mode allows readers/writers simultaneously (readers see old snapshot, writers create new). |
| "Savepoints for nesting" | SQLite SAVEPOINT allows nested transactions (outer commits, inner can rollback). |

### Gotchas at depth

- **Transaction timeout:** Very long transactions (millions of inserts) may timeout. Batch into smaller transactions if needed.
- **Deadlock on nested transactions:** Two transactions wait for each other's locks. SQLite raises SQLITE_IOERR. Careful with `@Transaction` calling another `@Transaction`.
- **Corrupted DB after crash:** If crash during COMMIT, DB may be corrupt. WAL journal files must be cleaned. Room handles via `databaseBuilder().fallbackToDestructiveMigration()` on corruption.
- **Size growth:** WAL files (.wal, .shm) grow alongside main DB. Not automatically cleaned. Use `pragma wal_checkpoint(RESTART)` to consolidate.

</details>

---

## 18. Permissions & Scoped Storage

### Runtime Permissions Pattern (2026 Modern)

> **TL;DR:** Use `registerForActivityResult()` with `ActivityResultContracts.RequestPermission()`. Check permission first → show rationale if user denied before → request.

`checkSelfPermission()` · `shouldShowRequestPermissionRationale()` · No onActivityResult needed · Composable

<details>
<summary>💻 Code Example</summary>

```kotlin
class MainActivity : ComponentActivity() {
    private val cameraPermission = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted -> if (isGranted) openCamera() else showDenied() }

    fun requestCamera() {
        when {
            checkSelfPermission(Manifest.permission.CAMERA) == PERMISSION_GRANTED -> openCamera()
            shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> showRationale()
            else -> cameraPermission.launch(Manifest.permission.CAMERA)
        }
    }
}
```

</details>

**Pattern:** Always explain *why* before asking—improves UX and interview signal.

<details>
<summary>🔩 Under the Hood</summary>

### How ActivityResult Contracts Work

**What you write:**
```kotlin
registerForActivityResult(ActivityResultContracts.RequestPermission()) { granted -> ... }
```

**What Android framework does:**
- Registers callback internally with activity lifecycle
- On permission request, system shows dialog
- On response, framework calls your lambda (handles activity death/recreation)
- No manual onActivityResult() override needed

### Why Contracts Over onActivityResult

- **Lifecycle-aware:** Callbacks survive activity recreation (config change)
- **Type-safe:** Contract defines input/output types at compile time
- **Composable:** Can register multiple contracts without collision

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use registerForActivityResult" | Contract is registered early (in init/onCreate), callback stored by activity. System calls it via onActivityResult internally. |
| "Check permission before requesting" | checkSelfPermission caches result. Framework caches OS permission state in PackageManager. |
| "Show rationale if user denied" | shouldShowRequestPermissionRationale is true only AFTER user denies once AND you don't have permission yet. |

### Gotchas at depth

- **Registering too late:** Must register in onCreate/init. Late registration (in onStart) crashes.
- **Process death:** If app is killed between request and response, callback is lost. Use SavedStateHandle for state.
- **Permissions denied forever:** If user selects "Don't ask again", shouldShowRequestPermissionRationale returns false. Direct to app settings.

</details>

### Scoped Storage (API 30+)

> **TL;DR:** Can't access shared `/sdcard/DCIM` directly. Use app-specific dirs (no permission) OR MediaStore + permission.

App-specific: `getExternalFilesDir()` · MediaStore: `EXTERNAL_CONTENT_URI` · Permissions required · Query SAF for legacy

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ App-specific (auto cleanup, no permission)
val file = File(context.getExternalFilesDir(Environment.DIRECTORY_PICTURES), "photo.jpg")
file.writeBytes(imageBytes)

// ✅ Shared Pictures (needs READ_EXTERNAL_STORAGE)
val values = ContentValues().apply {
    put(MediaStore.Images.Media.DISPLAY_NAME, "photo.jpg")
    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
}
val uri = context.contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)
uri?.let { context.contentResolver.openOutputStream(it)?.write(imageBytes) }
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Why Scoped Storage Exists

**Pre-Android 10:** Apps had unrestricted `/sdcard` access → privacy risk (read any user's photos, financial data, etc).

**Post-Android 10:** MediaStore + SAF (Storage Access Framework) provide controlled access through OS-managed content providers.

### Implementation Details

- **getExternalFilesDir():** Stored in `/Android/data/<package>/files/`. Deleted when app uninstalled. No MediaStore query needed.
- **MediaStore:** Content provider backed by SQLite database. insert() creates entry + returns URI. You write via ContentResolver stream.
- **SAF (Storage Access Framework):** Shows user a document picker. Grants persistent URI access for specific files.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Can't write to DCIM anymore" | MediaStore is the sole interface to shared storage. OS controls all file access. |
| "Need READ_EXTERNAL_STORAGE permission" | Permission gates whether app can see MediaStore results. Without it, queries return empty. |
| "Use app-specific directory" | getExternalFilesDir() is outside MediaStore. Filesystem access direct (for app only). |

### Gotchas at depth

- **Deleted files still in MediaStore:** After delete, MediaStore entry lingers until app recreates DB. Query might return ghosts.
- **Different paths per Android version:** getExternalFilesDir() may be on different physical storage (if dual-storage device). Check isSdCardWritable().
- **Permissions don't guarantee access:** Even with READ_EXTERNAL_STORAGE, can only see MediaStore. Can't list raw files anymore.

</details>

---

## 19. Fragments & Navigation

### Fragment Lifecycle (Common Pitfalls)

> **TL;DR:** `onCreate` → `onCreateView` → `onViewCreated` → `onStart` → `onResume`. **Key gotcha:** `onStop()` NOT guaranteed on process death—use `SavedStateHandle` for persistence.

Only guaranteed if fragment visible · View access timeline matters · Process death edge case

|Lifecycle|Guaranteed|View Access|Use For|
|---|---|---|---|
|`onCreate`|✅|❌|Initialize, restore bundle|
|`onCreateView`|✅|✅ (first)|Create/inflate views|
|`onViewCreated`|✅|✅|Setup listeners, observers|
|`onStart`|✅|✅|Start animations, foreground|
|`onResume`|✅|✅|Request focus, media playback|
|`onPause`|✅|✅|Pause media, unregister|
|`onStop`|❌ (process death)|✅|Save state to SavedState|
|`onDestroy`|❌|❌|Cleanup only|

<details>
<summary>🔩 Under the Hood</summary>

### Why onStop() Not Guaranteed

**Process death scenario:**
- App in background, system kills process to free RAM
- onPause/onStop never called (no time)
- On resume: onCreate/onViewCreated called again
- State lost unless saved

**Solution: SavedStateHandle**
```kotlin
val savedStateHandle: SavedStateHandle
val count = savedStateHandle.getLiveData("count", 0)
count.observe(this) { /* restored value */ }
```

### What it reuses & relies on

- **Fragment back stack:** Managed by FragmentManager (part of Activity state)
- **SavedStateHandle:** Automatic persistence via lifecycle component
- **Process death resilience:** Android framework checks `isFinishing` during destruction

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "onStop not guaranteed" | Process can be killed by system. onStop is not a reliable hook. Must use SavedStateHandle (which auto-saves to Bundle during onPause). |
| "Use onViewCreated for setup" | Fragment lifecycle can restart multiple times. Each onCreate/onViewCreated gets fresh view instance from Fragment#mView. |
| "Activity death = Fragment death" | Fragment lifecycle tied to activity. Activity destruction cascades onDestroyView → onDestroy. No Fragment outlives activity. |

### Gotchas at depth

- **Retained Fragments:** `setRetainInstance(true)` (deprecated in Fragments 1.3+). Better: Explicit state retention via SavedStateHandle.
- **View pager fragment destruction:** Fragment in ViewPager may be destroyed when off-screen (depending on offscreen limit). Setup listeners in onViewCreated, not onCreate.
- **Memory leaks from listeners:** If listener holds reference to fragment, and fragment not destroyed, memory leak. Always unregister in onDestroyView.

</details>

### Shared ViewModel Between Fragments

> **TL;DR:** Use `activityViewModels()` to get ViewModel scoped to Activity lifetime. Survives Fragment replacement. Both fragments read/write same state.

`activityViewModels()` · StateFlow for state · Activity-scoped lifetime

<details>
<summary>💻 Code Example</summary>

```kotlin
class SharedViewModel : ViewModel() {
    private val _selected = MutableStateFlow<Item?>(null)
    val selected = _selected.asStateFlow()
    fun selectItem(item: Item) { _selected.value = item }
}

class FragmentA : Fragment() {
    private val viewModel: SharedViewModel by activityViewModels()
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        itemList.setOnItemClick { viewModel.selectItem(it) }
    }
}

class FragmentB : Fragment() {
    private val viewModel: SharedViewModel by activityViewModels()
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        lifecycleScope.launch {
            viewModel.selected.collectLatest { item -> item?.let { showDetails(it) } }
        }
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### How activityViewModels() Works

**Fragment creation:**
```
Fragment A created → activityViewModels() retrieves from activity's ViewModelStore
Fragment B created → activityViewModels() retrieves SAME instance from same ViewModelStore
```

**ViewModelStore:** Activity holds a map of ViewModels keyed by class name. All fragments accessing same key get same instance.

**Why it survives fragment replacement:**
- Fragment can be destroyed (onDestroy called)
- Activity still holds ViewModelStore
- Replace with new fragment → new fragment gets same ViewModel instance
- State preserved across fragment navigation

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "activityViewModels() = shared state" | ViewModel scoped to Activity. Stored in Activity#mViewModelStore (Map<String, ViewModel>). Multiple fragments access same instance. |
| "Survives fragment replacement" | Fragment lifecycle independent of ViewModel lifecycle. Fragment #onDestroy destroys view but NOT ViewModel. Activity#onDestroy clears ViewModelStore. |
| "Better than static fields" | ViewModel injection is cleaner than global state. DI framework can replace with test mock. Static fields can't be mocked. |

### Gotchas at depth

- **Fragment back stack:** If Fragment A is on back stack (not visible), ViewModel still active. Memory cost persists.
- **Activity death:** Activity configuration change (rotation) doesn't destroy ViewModel. Process death does (need SavedStateHandle for recovery).
- **Hilt scoping:** With Hilt, use @ActivityScoped. Without Hilt, manually scope to activity via activityViewModels().

</details>

### Back Stack Management

> **TL;DR:** `navigate()` adds to back stack (default). `popUpTo()` pops previous entries. `popBackStack()` returns false if no stack left → finish activity.

`navController.navigate()` · `popUpTo()` · `inclusive` flag · Check return value

<details>
<summary>💻 Code Example</summary>

```kotlin
val navController = findNavController()

// Navigate (adds to back stack)
navController.navigate(R.id.destFragment)

// Navigate & clear back stack to home
navController.navigate(R.id.home, navOptions {
    popUpTo(R.id.home) { inclusive = false }  // Keep home, pop others
})

// Pop back stack programmatically
if (!navController.popBackStack()) {
    requireActivity().finish()  // No stack left
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Navigation Component Back Stack

**Back stack structure:**
```
[home] ← (bottom, won't pop)
[profile]
[settings] ← (top, pops first)
```

**popUpTo(R.id.home, inclusive=false):**
- Pop [settings] and [profile]
- Keep [home]
- Navigate to destination (new [dest] pushed)

**popUpTo(R.id.home, inclusive=true):**
- Pop [settings], [profile], AND [home]
- Navigate to destination (new [dest] is now alone)

### Why Back Stack Matters

- Android expects back button to work (UX standard)
- NavController manages stack automatically
- Without proper popUpTo, app can get "stuck" with many stacked destinations

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "popUpTo clears previous entries" | NavController maintains a Deque of NavBackStackEntry. popUpTo removes entries until matching ID, then navigates. |
| "inclusive flag determines if target stays" | inclusive=true removes the target too. inclusive=false pops up TO (but not including) the target. |
| "popBackStack() returns false if empty" | NavController checks if stack is empty before popping. If empty, navigation stack is destroyed; app must close. |

### Gotchas at depth

- **Deep linking:** NavDeepLinkBuilder synthesizes a back stack. If app killed and relaunched via deep link, back stack is artificial (may not match previous session).
- **popBackStack() in Fragment:** Must call on navController, not FragmentManager. FragmentManager back stack is separate (can cause inconsistency).
- **Navigation lifecycle:** Each destination in back stack has its own lifecycle scope. Popped fragments' lifecycleScope is cancelled (important for Flows).

</details>

---

## 20. Camera & Media Integration

### CameraX Basics

> **TL;DR:** Initialize `ProcessCameraProvider` → build `Preview` + `ImageCapture` use cases → `bindToLifecycle()` to attach to fragment lifecycle. Always `unbindAll()` before rebinding.

`ProcessCameraProvider` · Lifecycle-aware binding · `Preview` + `ImageCapture` · Main thread executor

<details>
<summary>💻 Code Example</summary>

```kotlin
class CameraScreen : Fragment() {
    private lateinit var imageCapture: ImageCapture

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val future = ProcessCameraProvider.getInstance(requireContext())
        future.addListener({
            startCamera(future.result)
        }, ContextCompat.getMainExecutor(requireContext()))
    }

    private fun startCamera(provider: ProcessCameraProvider) {
        val preview = Preview.Builder().build().also {
            it.setSurfaceProvider(previewView.surfaceProvider)
        }
        imageCapture = ImageCapture.Builder().build()
        provider.bindToLifecycle(this, CameraSelector.DEFAULT_BACK_CAMERA, preview, imageCapture)
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### CameraX Architecture

**Use cases:** Preview, ImageCapture, ImageAnalysis, VideoCapture plugged into single `cameraProvider`.

**bindToLifecycle():** Ties use cases to fragment lifecycle. When fragment destroyed, camera releases automatically.

**What you write vs framework does:**
```
You: bindToLifecycle(this, selector, preview, imageCapture)
Framework:
  - Registers fragment lifecycle observer
  - Attaches camera thread lifecycle (separate from UI thread)
  - On fragment destroy: releases camera, stops preview thread
```

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "bindToLifecycle handles cleanup" | Fragment lifecycle observer + camera thread lifecycle observer. On destroy, both stop simultaneously (framework callback). |
| "Use cases are composable" | CameraX supports multiple use cases bound at once (e.g., Preview + ImageAnalysis). Resource conflict = exception. |
| "ProcessCameraProvider is async" | getInstance() returns ListenableFuture (non-blocking). Provider initialized on camera thread, not UI thread. |

### Gotchas at depth

- **Multiple fragments:** Each fragment gets separate camera instance if both bind independently. Sharing camera = Singleton anti-pattern. Better: bind to activity.
- **Permissions timing:** Even with permission granted, ProcessCameraProvider might fail if camera hardware unavailable or already in use.
- **Frame drops:** Too many use cases or slow analysis = frame drops. Profile with Perfetto's camera trace.

</details>

### Media3 (ExoPlayer) Basics

> **TL;DR:** Create `ExoPlayer` → set `MediaItem` (URL or local file) → `prepare()` → `play()`. Always `release()` in `onDestroyView`.

`ExoPlayer` · `MediaItem` · Lifecycle cleanup · Plays local + remote

<details>
<summary>💻 Code Example</summary>

```kotlin
class VideoScreen : Fragment() {
    private lateinit var player: ExoPlayer

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        player = ExoPlayer.Builder(requireContext()).build()
        playerView.player = player
        player.setMediaItem(MediaItem.fromUri("https://example.com/video.mp4"))
        player.prepare()
        player.play()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        player.release()
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### ExoPlayer State Machine

**State transitions:**
```
IDLE → BUFFERING → READY → ENDED
 ↑        ↓
 └────────┴─→ ERROR
```

**prepare():** Starts buffering. Async operation; `onPlayerStateChanged` callback fires when ready.

**release():** Stops all playback threads, releases decoder resources, closes connections. Critical for battery/memory.

### Media3 Architecture

- **Renderer:** Audio, video, text renderers (pluggable)
- **Extractor:** Demuxes container format (MP4, HLS, DASH)
- **Decoder:** Software decoder (fallback) or hardware decoder (preferred)

**Why Media3 over VideoView:**
- VideoView = simple wrapper; no control
- ExoPlayer = full control (speed, quality, buffering)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Always release() in onDestroyView" | ExoPlayer spawns decoder thread + network thread. release() stops threads, frees codec. If not released, threads live until GC (memory leak). |
| "setMediaItem before prepare()" | ExoPlayer parses URL/file in background thread. prepare() starts buffering. If you set item post-prepare, buffering restarts. |
| "PlayerView handles UI" | PlayerView = wrapper around ExoPlayer. Renders player controls, player state callbacks. Alternative: Custom surface render + manual UI. |

### Gotchas at depth

- **Pause vs pause on resume:** ExoPlayer pauses when app goes background (lifecycle pause), then auto-resumes when resumed (configurable). Can interfere with user expectations.
- **Bandwidth throttling:** ExoPlayer adapts bitrate (for HLS/DASH). On slow network, automatically switches to lower quality. Can surprise users.
- **Codec compatibility:** Not all devices support all codecs. Fallback to software decoder (CPU cost). Check supported codecs before playback.

</details>

---

## 21. Push Notifications & FCM

### Firebase Cloud Messaging Integration

> **TL;DR:** Extend `FirebaseMessagingService` → override `onMessageReceived()` for data messages → override `onNewToken()` to sync token with backend. Register service + intent-filter in AndroidManifest.

`FirebaseMessagingService` · Data vs Notification messages · Token refresh · PendingIntent for deep links

<details>
<summary>💻 Code Example</summary>

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Data message = custom logic needed
        remoteMessage.data.takeIf { it.isNotEmpty() }?.let { data ->
            val title = data["title"]
            sendNotification(title, data["body"])
        }
    }

    override fun onNewToken(token: String) {
        uploadTokenToBackend(token)  // Sync with backend
    }

    private fun sendNotification(title: String?, body: String?) {
        val pendingIntent = PendingIntent.getActivity(this, 0, Intent(this, MainActivity::class.java),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
        val notification = NotificationCompat.Builder(this, "default_channel")
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle(title)
            .setContentIntent(pendingIntent)
            .setAutoCancel(true).build()
        NotificationManagerCompat.from(this).notify(System.currentTimeMillis().toInt(), notification)
    }
}
```

</details>

**AndroidManifest.xml:**
<details>
<summary>💻 Code Example</summary>

```xml
<service android:name=".MyFirebaseMessagingService" android:exported="false">
    <intent-filter><action android:name="com.google.firebase.MESSAGING_EVENT" /></intent-filter>
</service>
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### FCM Message Types

**Data message:**
```json
{"data": {"key": "value"}}
```
- App must handle in `onMessageReceived()`
- Custom logic (e.g., deep link, analytics)
- Works even if app killed (system wakes it)

**Notification message:**
```json
{"notification": {"title": "...", "body": "..."}}
```
- Framework auto-displays in notification bar
- `onMessageReceived()` still called, but redundant
- Tap = deep link (specified in Firebase console)

### Token Management

**onNewToken() fired when:**
- App first installed (initial token)
- User uninstalls/reinstalls app (new token)
- Token refreshed by FCM (~6 months, or security reason)

**Backend must persist token** for targeting. Stale tokens → failed delivery.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "onMessageReceived = data message handler" | FCM service runs in separate process. System wakes app if killed. onMessageReceived called on background thread (non-UI). |
| "Token identifies device+app" | Token scoped to (package, device, Firebase project). Token includes device cert, Firebase project ID. Changing ID = new token. |
| "Send token to backend" | Backend stores mapping: (user_id → token list). On logout, delete token. Prevents push after user leaves. |

### Gotchas at depth

- **App killed = wake-up:** System can start your app to handle FCM message even if user force-stopped it. Set up receivers carefully to avoid wasting battery.
- **Token expiry:** Tokens don't have explicit expiry, but can become invalid if cert rotates. Backend should handle HTTP 401 (re-request token).
- **Notification click handler:** Pending intent launched activity may be already running. Use `Intent.FLAG_ACTIVITY_SINGLE_TOP` to avoid duplicate instances.

</details>

### Token Sync & Management

> **TL;DR:** On app startup, get current token via `FirebaseMessaging.getInstance().token`. Sync with backend. Listen for `onNewToken()` refreshes.

Startup sync · onNewToken callbacks · Backend deduplication

<details>
<summary>💻 Code Example</summary>

```kotlin
// On app startup (in Application class)
FirebaseMessaging.getInstance().token.addOnSuccessListener { token ->
    uploadTokenToBackend(token)
}

// Enable auto-init (default true)
FirebaseMessaging.getInstance().isAutoInitEnabled = true
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Token Lifecycle

**Persistence:** Token stored in SharedPreferences by Firebase library (transparent to app).

**When requested:** `getInstance().token` retrieves from SharedPreferences or fetches fresh if expired.

**Sync strategy:**
```
App startup → get token → POST to /api/device-token → backend stores
On token refresh (onNewToken) → POST to /api/device-token again
```

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Get token on startup" | Firebase lib caches token in encrypted SharedPrefs. getInstance().token checks cache first, fetches async if needed. |
| "Dedup on backend" | Backend should use (device_id, package) as composite key. Prevents duplicate token entries on re-installs. |
| "Token can change without user action" | Firebase rotates tokens periodically or on security event. App must always resync on onNewToken(). |

### Gotchas at depth

- **Timing race:** If you request push targeting before token uploaded, backend has no token. Send token sync FIRST, then request notification.
- **Token stickiness:** Old tokens don't invalidate immediately. FCM may attempt delivery to old token for 28 days. Backend should clean up inactive tokens.
- **Disabled push:** If user disables FCM in settings, token still works but messages are dropped. No callback to notify app (check via isAutoInitEnabled).

</details>

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

## 23. Accessibility (a11y) & Localization (i18n)

### Compose Accessibility

> **TL;DR:** Use `.semantics { contentDescription = "..." }` for screen readers (TalkBack). Mark headings with `.semantics { heading() }`. Compose auto-handles text scaling & color contrast if using Material semantics.

Semantics tree · contentDescription · TalkBack testing · heading() marker

<details>
<summary>💻 Code Example</summary>

```kotlin
Box(
    Modifier
        .semantics { contentDescription = "User profile card" }
        .clickable { openProfile() }
) {
    Text("Alice", Modifier.semantics { heading() })
    Text("Engineer")
}

// Test: adb shell settings put secure enabled_accessibility_services \
// com.google.android.marvin.talkback/.TalkBackService
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Semantics Tree

**Compose builds tree of semantic nodes parallel to layout tree.**

```
UI Tree:          Semantics Tree:
Box                │
├─ Text("Alice")   ├─ heading() → "Alice"
├─ Text("Eng")     └─ "Engineer"
```

**Screen reader traverses semantics tree**, reads contentDescription for each node.

### contentDescription vs. Text

- **contentDescription:** For non-text UI (icons, images, buttons without text). Screen reader announces once.
- **Text content:** Auto-detected as readable. Don't duplicate in contentDescription.
- **empty contentDescription:** Tells TalkBack to skip (for decorative elements).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use contentDescription for icons" | Framework generates accessibility event (TYPE_VIEW_ANNOUNCED) with description. TalkBack processes event. |
| "Semantics tree for screen readers" | Compose tracks semantic properties separately. TalkBack queries AccessibilityDelegate (interface). Returns semantics tree. |
| "Test with TalkBack" | TalkBack is open-source Google service. Reads semantics tree aloud, sends haptics. Works via AccessibilityService (system API). |

### Gotchas at depth

- **Duplicate descriptions:** If you set contentDescription but Text already readable, screen reader announces twice (bad UX).
- **Merged semantics:** Multiple composables can merge into one semantic node. contentDescription applies to entire merged node.
- **Custom modifiers:** Custom Modifiers might break semantics. Always call super.measure(), super.layout() to preserve event delivery.

</details>

### String Resources & Localization (i18n)

> **TL;DR:** Create `res/values-<locale>/strings.xml` for each language (e.g., `values-es`, `values-fr`). Framework auto-selects based on device locale. For RTL (Arabic, Hebrew), set `android:supportsRtl="true"`.

Locale-specific resources · values-<locale> · RTL support · Plurals

<details>
<summary>💻 Code Example</summary>

```xml
<!-- res/values/strings.xml (English) -->
<string name="hello">Hello %s</string>
<plurals name="item_count">
    <item quantity="one">%d item</item>
    <item quantity="other">%d items</item>
</plurals>

<!-- res/values-es/strings.xml (Spanish) -->
<string name="hello">Hola %s</string>
<plurals name="item_count">
    <item quantity="one">%d elemento</item>
    <item quantity="other">%d elementos</item>
</plurals>

<!-- AndroidManifest.xml -->
<application android:supportsRtl="true" />
```

</details>

**RTL in Compose:**
<details>
<summary>💻 Code Example</summary>

```kotlin
// Auto-flips for RTL (start = left in LTR, right in RTL)
Text("Hello", Modifier.padding(start = 8.dp))
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Resource Selection

**Framework algorithm:**
```
Get device locale (e.g., "es-ES") → Find matching strings.xml
├─ res/values-es-rES/ (exact match)
├─ res/values-es/ (language match)
├─ res/values/ (default fallback)
```

**Resolution order:** Exact locale → language → default.

### Plurals Handling

```kotlin
// Framework selects plural based on count
val count = 5
val text = resources.getQuantityString(R.plurals.item_count, count, count)
// Selects "other" form, substitutes %d with 5
// Returns: "5 items"
```

**Plural categories vary by language:**
- English: one, other
- Polish: one, few, many, other
- Arabic: zero, one, two, few, many, other

### RTL Layout

**start/end vs. left/right:**
- LTR: start = left, end = right
- RTL: start = right, end = left

**Compose auto-handles:** Use `start`, `end`, avoid `left`, `right`.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Create values-<locale> folder" | ResourceManager queries system locale (via Locale.getDefault()). Finds closest match in APK resources. |
| "RTL auto-flips" | Compose LayoutDirection set by framework from Locale.getDefault().isRTL(). Modifiers check LayoutDirection and reverse start/end. |
| "Plurals vary by language" | ICU library provides plural rules. Framework matches count to plural category. Non-English languages have different categories. |

### Gotchas at depth

- **String quantization:** Using %d in plurals is common, but some languages need formatting (e.g., Arabic uses suffix, not prefix). Use locale-aware NumberFormat.
- **Mixed LTR/RTL:** App with both LTR and RTL content = bidirectional text. Use Unicode direction markers (LRM, RLM) if needed.
- **String length in different languages:** German translations often longer than English. Layouts must flex (can't hardcode widths). Use Text reflow, not clipping.

</details>

---

## 24. Analytics & Crash Reporting

### Firebase Analytics Integration

> **TL;DR:** Initialize `FirebaseAnalytics.getInstance()` → log events with `logEvent(eventName, Bundle)`. Use predefined event constants for standard events (SIGN_UP, PURCHASE). Bundle contains parameters.

Event logging · Predefined events · Bundle parameters · Standard vs. custom

<details>
<summary>💻 Code Example</summary>

```kotlin
val analytics = FirebaseAnalytics.getInstance(context)

analytics.logEvent(FirebaseAnalytics.Event.SIGN_UP, Bundle().apply {
    putString(FirebaseAnalytics.Param.METHOD, "google")
})

analytics.logEvent(FirebaseAnalytics.Event.PURCHASE, Bundle().apply {
    putString(FirebaseAnalytics.Param.ITEM_ID, "item_123")
    putDouble(FirebaseAnalytics.Param.VALUE, 9.99)
    putString(FirebaseAnalytics.Param.CURRENCY, "USD")
})
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Event Batching & Upload

**Framework batches events** in memory, sends to Firebase backend every ~30 seconds or when batch full.

**Local vs. Debug logging:**
- Enable verbose logging: `adb shell setprop log.tag.FA VERBOSE`
- View events in DebugView (real-time, development-only)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Log events with Bundle" | Bundle serialized to JSON. Sent to Firebase backend in batches (HTTP POST). Credentials via google-services.json. |
| "Use predefined event constants" | Firebase recognizes standard events (PURCHASE, SIGN_UP). Tracks automatically in dashboards. Custom events are opaque. |
| "Events are asynchronous" | logEvent() returns immediately (queued). Actual upload happens later. Crashes before upload = event lost. |

### Gotchas at depth

- **PII in events:** Never log user email, phone, payment info in events (privacy violation). Use user_id instead.
- **Event name limits:** Max 32 characters, alphanumeric + underscore. Longer names rejected silently.
- **Parameter count:** Max 25 parameters per event. Firebase silently drops excess.

</details>

### Crash Reporting (Firebase Crashlytics)

> **TL;DR:** Call `FirebaseCrashlytics.getInstance().recordException(exception)` to log crashes. Use `.setCustomKey()` for context, `.setUserId()` for user identification. Crashes auto-reported if unhandled.

Uncaught exceptions auto-logged · recordException() for caught · Custom keys · User tracking

<details>
<summary>💻 Code Example</summary>

```kotlin
// Manual crash logging
val exception = Exception("Payment failed")
FirebaseCrashlytics.getInstance().recordException(exception)

// Add context
FirebaseCrashlytics.getInstance().setCustomKey("payment_method", "credit_card")
FirebaseCrashlytics.getInstance().setUserId("user_123")
FirebaseCrashlytics.getInstance().log("Payment attempt started")
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Exception Handling

**Uncaught exceptions:** Thread.UncaughtExceptionHandler installed by Firebase. Catches uncaught crashes, logs locally, crashes app as normal.

**Caught exceptions:** Explicitly call `recordException()` to upload (optional, not crash-level urgent).

**NDK crashes:** Native code crashes via signal handler (SIGSEGV, etc.). Firebase NDK library catches, symbolizes, sends.

### Local Storage & Retry

- **Crash stored locally** in app's cache directory (encrypted)
- **On next startup**, framework uploads to Firebase backend
- **If upload fails**, retried for ~1 week before discarded

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Uncaught crashes auto-reported" | Thread.setDefaultUncaughtExceptionHandler called by Firebase at app init. Receives uncaught exception, logs, re-throws (app crashes). |
| "Custom keys for context" | Custom keys serialized with crash data. Sent together to backend. Helps in debugging but doesn't prevent crash. |
| "setUserId for user grouping" | User ID hashed and sent with crash. Backend groups crashes by user (how many users affected). |

### Gotchas at depth

- **Crash before upload:** If app crashes before next startup, crash might not upload (if app uninstalled). Use Crashlytics web API for manual uploads if critical.
- **Large crashes:** Very large crash logs (>1MB) might be truncated or rejected. Keep logs concise.
- **Testing crashes:** Use `FirebaseCrashlytics.getInstance().crash()` to force a test crash and verify reporting.

</details>

---

## 25. Code Organization & Architecture

### Module Structure (Large Teams)

> **TL;DR:** Split app into **feature modules** (auth, home) + **core modules** (network, database, ui). Dependency flow: `feature` → `core`, never `feature` → `feature`. Use DI to decouple.

Multi-module structure · Dependency graph · Core shared layers · Feature isolation

<details>
<summary>💻 Code Example</summary>

```
app/
├── feature-auth/     ─→ domain/, data/, ui/, di/
├── feature-home/     ─→ domain/, data/, ui/, di/
├── core-network/     ← shared by features
├── core-database/    ← shared by features
└── core-ui/          ← shared by features
```

</details>

**Dependency rule:** ✅ `feature` imports `core` | ❌ `feature` imports `feature` (break cycle via DI interfaces/events).

| Structure | Benefit | Cost |
|---|---|---|
| Monolithic (1 module) | Simple, fast builds | Circular deps, hard to test |
| Multi-feature | Isolates concerns, parallel build | Build complexity, more coordination |
| Over-modularized (30+ modules) | Maximum isolation | Gradle overhead, hard to navigate |

<details>
<summary>🔩 Under the Hood</summary>

### Gradle Dependency Resolution

**When you import a module:**
```gradle
dependencies {
    implementation(project(":feature-auth"))
}
```

**Gradle resolves to**:
- feature-auth's build.gradle dependencies
- Transitively includes all its imports (core-* modules)
- If circular (auth imports home), build fails

**Build cache:** Gradle caches compiled modules. Only rebuild if source changes.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Modularize to avoid circular deps" | Circular deps break class loader. Gradle detects, fails build. Forces architectural discipline. |
| "DI to decouple features" | DI container (Hilt) lives in app module. Features define interfaces in core-* modules. App wires implementations. |
| "core-* modules never import feature-*" | Prevents tight coupling. core-network usable in any feature without knowing about auth/home. Testable in isolation. |

### Gotchas at depth

- **Transitive dependencies:** Importing :feature-auth pulls all its deps (including Retrofit, Room, etc.). Can bloat app size if not careful.
- **Lint/R class clashes:** Multiple modules defining custom views = R class conflicts. Use namespace in build.gradle.
- **Test fixtures:** Sharing test data across modules is hard. Either duplicate or create test-shared modules (expensive).

</details>

### Documentation Patterns

> **TL;DR:** Write ADR (Architecture Decision Records) for major choices. Add KDoc with `@param`, `@throws`, `@return` for public APIs. Include examples in docstrings.

KDoc · ADR · Examples · Consequences

**Architecture Decision Record:**
<details>
<summary>💻 Code Example</summary>

```markdown
# ADR-001: Use MVI instead of MVVM

## Context
State complexity growing; multiple StateFlow sources = inconsistent UI.

## Decision
Adopt MVI (Model-View-Intent) with single reducer + StateFlow.

## Consequences
✅ Single source of truth (state history)
✅ Pure reducer (testable)
❌ More boilerplate (Intent sealed class)

## Alternatives Considered
- MVVM with multiple LiveData (rejected: hard to coordinate)
- MVP (rejected: no ViewModel lifecycle)
```

</details>

**KDoc for Public APIs:**
<details>
<summary>💻 Code Example</summary>

```kotlin
/**
 * Fetches user with automatic caching and retry.
 *
 * @param userId ID to fetch
 * @return User (cached for 1 hour)
 * @throws NotFoundException if user not found
 * @throws IOException if 3 retries exhausted
 *
 * Example: `val user = getUser(123)`
 */
suspend fun getUser(userId: Int): User
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### KDoc & IDE Support

**IDE generates docs from KDoc** when hovering over function. Parameters, return type, exceptions shown.

**Tooling:** dokka generates HTML documentation from KDoc. Used to generate library docs (like Kotlin std lib docs).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Write KDoc for public APIs" | IDE parses KDoc comments. Generates popup on hover. Extracted by dokka to HTML/PDF. |
| "Include examples in docstrings" | Examples help developers understand intent. Also used for generating tutorials/cookbooks. |
| "ADR documents decisions" | ADRs live in version control. Future devs read history to understand why (vs. what). Prevents rework. |

### Gotchas at depth

- **Stale docs:** KDoc not auto-updated when API changes. Easy to document wrong behavior. Enforce doc updates in code review.
- **Over-documenting:** Documenting obvious APIs (getText()) wastes effort. Document why, not what.
- **ADR tooling:** No standard format. Teams define their own. Can become decision graveyard if not enforced.

</details>

---

## 26. RecyclerView Optimization

### ViewHolder & Recycling Best Practices

> **TL;DR:** Create ViewHolder in `onCreateViewHolder()` (inflation expensive). Bind data in `onBindViewHolder()` (called on recycle). Never inflate in bind—reuse views!

Recycling pool · ViewHolder pattern · onCreateViewHolder efficiency · Avoid stale references

<details>
<summary>💻 Code Example</summary>

```kotlin
class UserAdapter : RecyclerView.Adapter<UserViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_user, parent, false)
        return UserViewHolder(view)
    }

    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        holder.bind(items[position])  // Called on recycle; reuse view
    }

    override fun getItemCount() = items.size
}

class UserViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
    private val nameView: TextView = itemView.findViewById(R.id.name)
    private val avatarView: ImageView = itemView.findViewById(R.id.avatar)
    fun bind(user: User) {
        nameView.text = user.name
        avatarView.load(user.avatarUrl)  // Coil handles recycle cleanup
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### ViewHolder Recycling Pool

**Framework maintains pool of ViewHolders:**
```
Scroll down → Visible ViewHolder moves off-screen
Framework adds to pool (scrap) → Rebinds with new data → Moves to screen
```

**Pool size:** Typically 3-5 visible items. Only create new holders if pool empty.

**Inflating in onBind = catastrophic:** Adds 10ms per bind (you see 60fps drop).

### Image Loading & Recycle

**Without Coil:**
```
Bind position 0 → Start loading image URL
Scroll → Position 0's ViewHolder recycled to position 10
Image loads → Displays wrong image (stale URL)
```

**With Coil:** Image library cancels old request on recycle, loads new request (no flicker).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Inflate in onCreate, bind in onBind" | ViewHolder pool managed by RecyclerView. onCreate creates once; onBind reuses. Every recycle saves layout inflation. |
| "Don't cache ViewHolder data" | If you cache, and item moves, cache stale. Always use getItem(position) in onBind. |
| "Image libraries handle recycling" | Glide/Coil register lifecycle callbacks. On ViewHolder destroy, requests cancelled (prevent memory leak). |

### Gotchas at depth

- **Large layouts:** If single item layout inflates 100 views, first scroll jank. Flatten hierarchy or use ViewStub for optional views.
- **Unbounded ViewHolder pool:** Some configs set pool size to 0 (all ViewHolders recreated). Causes frame drops on fast scroll.
- **Listener cleanup:** If ViewHolder registers listener (onClick), must unregister in onBind (or listener lives across recycles).

</details>

### DiffUtil for Efficient List Updates

> **TL;DR:** Extend `DiffUtil.ItemCallback<T>` with `areItemsTheSame()` + `areContentsTheSame()`. Use `ListAdapter.submitList()` to compute diff and update only changed items.

DiffUtil algorithm · ListAdapter · O(n) cost · Minimal UI updates

<details>
<summary>💻 Code Example</summary>

```kotlin
class UserDiffCallback : DiffUtil.ItemCallback<User>() {
    override fun areItemsTheSame(old: User, new: User) = old.id == new.id
    override fun areContentsTheSame(old: User, new: User) = old == new
}

class UserAdapter : ListAdapter<User, UserViewHolder>(UserDiffCallback()) {
    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        holder.bind(getItem(position))
    }
}

// Usage
viewModel.users.onEach { users ->
    adapter.submitList(users)  // DiffUtil computes changes, updates only changed rows
}.launchIn(viewLifecycleOwner.lifecycleScope)
```

</details>

**Impact:** Full refresh notifyDataSetChanged() = O(n) updates. DiffUtil = O(n) compute, but only rebind changed items (typically 1-2 items on scroll).

<details>
<summary>🔩 Under the Hood</summary>

### Myers' Diff Algorithm

**DiffUtil uses Myers algorithm** to find longest common subsequence. Compares old list vs. new list in background thread.

**Result:** Calculate moves, inserts, deletes with minimal rebuilds.

**Cost:** O(n*m) comparison, but fast in practice for small lists (<1000 items).

### ListAdapter & Coroutines

**submitList() async:**
```
Main thread: submitList(newList) called → returns
Background: DiffUtil computes diff
Main thread: Diff result posted back → notifyItemInserted/Remove/Changed
```

**No blocking.** UI stays smooth.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "DiffUtil finds changed items" | Uses Myers algorithm (longest common subsequence). O(n*m) time, but <100ms for typical lists. |
| "submitList is async" | ListAdapter offloads diff to background thread. Avoids jank on main thread. |
| "areContentsTheSame triggers rebind" | If true, item visually same, skip rebind. If false, rebind called. Custom equality check lets you optimize. |

### Gotchas at depth

- **List mutation:** Never mutate list after submitList(). Framework compares by reference. Create new list (copy old + changes).
- **Identity vs. equality:** areItemsTheSame checks ID (identity). areContentsTheSame checks equality (content). Both needed.
- **Large diffs:** DiffUtil on 10K items = 1 second compute. Run on IO dispatcher for large lists.

</details>

---

## 27. Custom Views & Canvas Drawing

### Custom View Lifecycle & Drawing

> **TL;DR:** Override `onMeasure()` (set size) → `onLayout()` (position) → `onDraw()` (draw). Pre-allocate Paint in member variable—never allocate in onDraw() (garbage = jank).

Measure/layout/draw lifecycle · Canvas API · Paint pooling · invalidate() for redraws

<details>
<summary>💻 Code Example</summary>

```kotlin
class CustomCircleView(context: Context, attrs: AttributeSet?) : View(context, attrs) {
    private var radius = 0f
    private val paint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.BLUE; style = Paint.Style.FILL }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        val size = 200.dp.toPixels().toInt()
        setMeasuredDimension(size, size)
    }

    override fun onLayout(changed: Boolean, left: Int, top: Int, right: Int, bottom: Int) {
        super.onLayout(changed, left, top, right, bottom)
        radius = width / 2f
    }

    override fun onDraw(canvas: Canvas) {
        canvas.drawCircle(width / 2f, height / 2f, radius, paint)
    }

    fun setRadius(r: Float) { radius = r; invalidate() }
}
```

</details>

**Pattern:** Pre-allocate paints/paths in member scope. Never allocate in onDraw().

<details>
<summary>🔩 Under the Hood</summary>

### Measure Spec Decoding

**onMeasure receives MeasureSpec** (parent constraint + child wishes):
```kotlin
val mode = MeasureSpec.getMode(widthMeasureSpec)  // AT_MOST, EXACTLY, UNSPECIFIED
val size = MeasureSpec.getSize(widthMeasureSpec)
```

**Modes:**
- EXACTLY: Parent fixed size (must use)
- AT_MOST: Max size, you can be smaller
- UNSPECIFIED: No constraint (wrap content)

### Canvas Drawing & CPU Cost

**Canvas operations:**
```
drawCircle() → Convert to path → Fill with paint → Rasterize (CPU) → submit to GPU
```

**Every onDraw() call = CPU work.** Allocating Paint = garbage → GC during animation = frame drop.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "onDraw expensive, call sparingly" | onDraw = CPU-bound. Profiler shows time spent (can be >16ms, causing jank). Hardware Canvas helps but still expensive. |
| "invalidate() triggers onDraw()" | invalidate() requests refresh. Choreographer batches, redraws next vsync (60Hz). Many invalidate() calls batched into one onDraw(). |
| "MeasureSpec encodes mode + size" | MeasureSpec = single int. High 2 bits = mode, low 30 bits = size. Parent encodes expectations; child respects. |

### Gotchas at depth

- **Over-drawing:** Drawing layered objects = O(n) depth. Reorder to reduce overdraw (profile with surface flinger). |
| **HW acceleration disabled:** Some canvas ops not GPU-supported (setShader on certain paths). Framework falls back to CPU (slow). |
| **requestLayout vs. invalidate:** requestLayout triggers measure/layout/draw. invalidate only triggers draw. Different costs.

</details>

---

## 28. Animations & Transitions

### Property Animation (ValueAnimator)

> **TL;DR:** `ValueAnimator.ofInt/Float()` animates from start to end over duration with interpolator. `addUpdateListener()` updates view per frame. Manual `requestLayout()` for layout changes.

ValueAnimator · Interpolators · Update listeners · 60fps driven

<details>
<summary>💻 Code Example</summary>

```kotlin
val animator = ValueAnimator.ofInt(0, 100).apply {
    duration = 1000
    interpolator = LinearInterpolator()  // Or AccelerateDecelerateInterpolator, etc.
    addUpdateListener { animation ->
        val value = animation.animatedValue as Int
        myView.layoutParams.height = value
        myView.requestLayout()
    }
}
animator.start()
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Frame-by-Frame Updates

**Choreographer-driven:** Animator registers with Choreographer (60Hz callback). On each vsync, calculates interpolated value, calls listener.

**requestLayout():** Triggers measure/layout/draw cycle. Next frame will render new layout.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Interpolator eases motion" | Interpolator function maps time fraction [0,1] to progress [0,1]. Linear = straight. Ease = curved (feels natural). |
| "Driven by Choreographer" | Animator not self-driving. Choreographer posts callback every 16ms (60Hz). Animator calculates progress, calls listener. |
| "requestLayout for size changes" | Manual measure/layout needed when animation changes view dimensions. Property animation doesn't know about layout. |

### Gotchas at depth

- **Listener leaks:** If Animator holds reference to view/activity, leak occurs. Lifecycle binding needed (or cancel on destroy).
- **Too many animations:** 20+ animators = callback overhead. Combine with transition() or use ObjectAnimator instead.

</details>

### Compose Animations

> **TL;DR:** `animateDpAsState()` observes state, animates to target value. Use `spring()`, `tween()`, or `keyframes()` specs. For multiple properties, use `updateTransition()` (keeps animations in sync).

animateDpAsState · Specs (spring, tween) · updateTransition · State-driven

<details>
<summary>💻 Code Example</summary>

```kotlin
@Composable
fun AnimatedCard(isExpanded: Boolean) {
    val height by animateDpAsState(
        targetValue = if (isExpanded) 300.dp else 100.dp,
        animationSpec = spring(dampingRatio = 0.8f),
        label = "card height"
    )
    Card(Modifier.height(height)) { Text("Content") }
}

@Composable
fun MultiAnimation(state: CardState) {
    val transition = updateTransition(state)
    val bgColor by transition.animateColor { if (it == CardState.Expanded) Color.Blue else Color.Gray }
    val scale by transition.animateFloat { if (it == CardState.Expanded) 1f else 0.8f }
    Box(Modifier.background(bgColor).scale(scale))
}
enum class CardState { Collapsed, Expanded }
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Recomposition & Animation

**State change → recomposition → animateDpAsState() continues over duration → multiple recompositions → final value reached.**

**Each recomposition:** Compose measures/layouts/draws with new animated value.

**updateTransition:** Keeps multiple animations synchronized. One state change → all animations animate together (not separately).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "animateDpAsState triggers recomposition" | State updated per frame → Compose recomposes → new value rendered → 60fps smooth. |
| "Specs control motion curve" | spring() = physics-based (overshoot). tween() = linear or custom easing. Specs are pure functions. |
| "updateTransition syncs animations" | Transition state drives all animations. Single state change → all properties animate coherently. |

### Gotchas at depth

- **Over-recomposition:** If state changes while animating, animation restarts (can feel janky). Use Transition to prevent.
- **Memory in animations:** State in lambda = recomposed per frame. Avoid allocating objects per frame.

</details>

---

## 29. Battery Optimization & Doze Mode

### Doze Mode Behavior (API 21+)

> **TL;DR:** Doze mode (device idle, screen off) defers alarms, stops network, disables wakelocks. Use `WorkManager` for background work. Avoid `setAndAllowWhileIdle()` (throttled if overused).

Doze · Maintenance windows · WorkManager vs. AlarmManager · Wakelocks

| Impact | Doze Behavior |
|---|---|
| Alarms | Deferred to maintenance window (every ~9 hours or on user interaction) |
| Network | Suspended unless maintenance window |
| Location | Updates stopped |
| Wakelocks | Ignored (partial wakelocks don't prevent doze) |
| JobScheduler/WorkManager | Deferred, not cancelled |

**Best practice:** Use WorkManager + `setBackoffCriteria()` for retries. Avoid AlarmManager + `setAndAllowWhileIdle()` (abuses doze).

<details>
<summary>🔩 Under the Hood</summary>

### Doze State Machine

**Device idle detection:**
```
Screen off → No motion (accelerometer) for 30 min → Doze mode activated
Maintenance window every ~9 hours (or on user unlock)
```

**Maintenance window:** System allows network, jobs run, wakelocks honored (briefly).

### WorkManager vs. AlarmManager

- **WorkManager:** Respects Doze (deferred), batch-friendly, modern API
- **AlarmManager + setAndAllowWhileIdle():** Bypasses Doze once (abused → throttled by system after multiple calls)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Doze defers work" | System tracks device idle state (motion sensors + screen). On Doze entry, OS defers jobs until maintenance. |
| "Maintenance windows" | Framework allocates windows every ~9 hours or on user unlock. Jobs batch during windows (efficient). |
| "Wakelocks ignored in Doze" | Partial wakelocks don't prevent device sleep. FullScreen broadcast receivers still work (not deferred). |

### Gotchas at depth

- **whileIdle throttling:** If you call setAndAllowWhileIdle() >10x per app lifetime, system throttles (interval increased to hours).
- **Doze exemption apps:** WhatsApp, Gmail pre-installed = whitelisted. User apps not exempted. Custom exemption request possible but rare.

</details>

### Battery Drain Detection

> **TL;DR:** Use `adb shell dumpsys batterystats` to profile drain. Check for partial wakelocks (held >1 sec = bad), high CPU time, network overhead.

dumpsys batterystats · Partial wakelocks · CPU profiling · Network analysis

<details>
<summary>💻 Code Example</summary>

```bash
# Full battery stats
adb shell dumpsys batterystats

# Key metrics to check:
# "Partial wake lock": Time held (should be <1s total)
# "CPU time": CPU active time (% of battery)
# "Network": Data transferred (expensive)
# "Background": Services using CPU while backgrounded
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Battery Estimation

**Framework calculates drain based on:**
- CPU time @ different frequencies
- Screen on/brightness
- Network activity (wifi vs. cellular)
- GPS usage
- Wakelocks (partial = prevents sleep = drain)

**Data populated by PowerProfile.xml** (per-device configuration).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Check dumpsys batterystats" | Kernel logs power state changes. Framework collects into battery stats. dumpsys reads from /data/system/battery_history. |
| "Partial wakelocks = drain" | Partial wakelock prevents CPU sleep. CPU @ full frequency while device held = significant drain. Check hold duration. |
| "Network expensive" | Cellular radio = high power state. Transferring 1MB = ~5s radio active = several % battery. Batch transfers. |

### Gotchas at depth

- **Stale data:** Battery stats accumulate. Old apps no longer running still appear. Reset with `adb shell dumpsys batterystats --reset`.
- **Profiling overhead:** dumpsys battery stats itself adds overhead. Profile on real device, not emulator (emulator power irrelevant).

</details>

---

## 30. SSL/TLS & Network Security

### Certificate Pinning

> **TL;DR:** Pin specific certificates (SHA256 hash) to prevent MITM attacks. Add pins to OkHttpClient. Generate pin: `openssl s_client | openssl x509 | openssl dgst`.

CertificatePinner · SHA256 pins · Backup pins · OkHttp integration

<details>
<summary>💻 Code Example</summary>

```kotlin
val pinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/AAAAAAA==")  // Primary
    .add("api.example.com", "sha256/BBBBBBB==")  // Backup
    .build()

val httpClient = OkHttpClient.Builder()
    .certificatePinner(pinner)
    .build()

val retrofit = Retrofit.Builder().client(httpClient).build()
```

</details>

**Why:** Normal TLS validates cert against system store. Pinning = only trusts specific pins (harder to MITM even if store compromised).

<details>
<summary>🔩 Under the Hood</summary>

### Certificate Chain Validation

**TLS normally:** Client receives cert chain → validates against system CA store → trusts if any CA matches.

**With pinning:** Client verifies cert chain, then checks if public key hash matches pinned hash. Extra verification layer.

**Pin types:**
- Certificate pin (cert hash)
- Public key pin (public key hash, survives cert renewal)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Pin certificates for extra security" | Pinning = public key hash verification. Even if CA compromised, attacker needs matching public key. |
| "Pin primary + backup" | Primary pin rotates annually. Backup pins allow rotation without app update. Pin set can include 2-3 keys. |
| "Breaks app if pin expires" | If all pins expire/invalid, SSL handshake fails = app can't connect. Requires app update to fix (emergency). |

### Gotchas at depth

- **Pin expiry:** If you forget to rotate pins before cert expires, ALL users locked out. Must plan ahead.
- **Backup pins essential:** Never pin only one cert. Always include backup (prevents lockout).
- **Dynamic pin updates:** Enterprise apps can use dynamic pin updates (server tells client new pins). Complex but safer.

</details>

### Network Security Configuration

> **TL;DR:** Define per-domain security policies in `network_security_config.xml`. Set certificate trust anchors, disable cleartext. Reference in AndroidManifest.

Per-domain policies · Trust anchors · Cleartext control · Dev server exceptions

<details>
<summary>💻 Code Example</summary>

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <domain-config cleartextTrafficPermitted="false">
        <domain includeSubdomains="true">api.example.com</domain>
        <trust-anchors>
            <certificates src="@raw/my_ca" />
        </trust-anchors>
    </domain-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.0.1</domain>  <!-- Dev only -->
    </domain-config>
</network-security-config>

<!-- AndroidManifest.xml -->
<application android:networkSecurityConfig="@xml/network_security_config">
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### System Trust

**By default:** Android uses system's default CA list (Mozilla root certs bundled in OS).

**With custom trust anchors:** Framework validates cert against specified CAs only (ignores system store for that domain).

**Per-domain:** Can have different rules per server. Dev server allows HTTP, production enforces HTTPS.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Set trust anchors per domain" | NetworkSecurityConfig generates X509TrustManager per domain. OkHttp queries it during SSL handshake. |
| "cleartextTrafficPermitted controls HTTP" | Post-Android 9, HTTP disabled by default. cleartextTrafficPermitted="true" allows. Dev use only. |
| "Dev exceptions prevent app breakage" | Developers need localhost/10.0.0.0 for testing. Config allows selective exceptions without compromising prod. |

### Gotchas at depth

- **Certificate mismatch:** Custom CA must issue cert for domain name. Mismatch = SSL error despite CA in trust list.
- **Cleartext upgrade attacks:** Allowing HTTP = vulnerable to downgrade attacks. Only for dev/testing, never production.
- **Config inheritance:** Default-config applies globally unless domain-config overrides. Order matters.

</details>

---

## 31. Instrumentation Tests & UI Testing

### Compose UI Testing

> **TL;DR:** Use `composeRule.setContent {}` to render UI, `.onNodeWithText()` to find nodes, `.performClick()` for interactions, `.assertIsDisplayed()` for assertions.

composeRule · Semantics tree queries · Scroll actions · Assertions

<details>
<summary>💻 Code Example</summary>

```kotlin
@RunWith(AndroidJUnit4::class)
class MyScreenTest {
    @get:Rule val composeRule = createComposeRule()

    @Test
    fun testButtonClick() {
        composeRule.setContent {
            var count by remember { mutableIntStateOf(0) }
            Column {
                Text("Count: $count")
                Button(onClick = { count++ }) { Text("Click me") }
            }
        }
        composeRule.onNodeWithText("Click me").performClick()
        composeRule.onNodeWithText("Count: 1").assertIsDisplayed()
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Compose Test API

**composeRule.setContent():** Renders composable in test environment, not emulator activity. No Android context overhead (unit-like speed).

**onNodeWithText():** Queries semantics tree (not visual). Finds nodes by contentDescription, text, or test tags.

**performClick():** Sends click event to semantics node. Triggers recomposition if state changes.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Find nodes by text" | Searches semantics tree, not visual hierarchy. Text nodes tagged in semantics during composition. |
| "performClick triggers recomposition" | Click event posted → state update → recomposition → new tree. Test continues (no Thread.sleep needed). |
| "No activity context needed" | ComposeTestRule creates synthetic test context. Avoids full activity startup (faster than Espresso). |

</details>

### Espresso for Legacy Views

> **TL;DR:** Use `ActivityScenarioRule` to launch activity. `onView(withId())` to find views. `perform(click())` for actions. `check(matches())` for assertions.

ActivityScenarioRule · View matchers · ViewActions · Idling

<details>
<summary>💻 Code Example</summary>

```kotlin
@RunWith(AndroidJUnit4::class)
class ActivityTest {
    @get:Rule val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun testButtonClick() {
        onView(withId(R.id.button)).perform(click())
        onView(withText("Success")).check(matches(isDisplayed()))
    }

    @Test
    fun testRecyclerView() {
        onView(withId(R.id.recycler)).perform(
            RecyclerViewActions.scrollToPosition<UserViewHolder>(20)
        )
        onView(withText("User 20")).check(matches(isDisplayed()))
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Espresso Idling & Synchronization

**Espresso waits for app idle** before performing actions (waits for background tasks, animations).

**Custom IdlingResource:** If Espresso can't detect idleness (custom thread pool), register IdlingResource.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Espresso waits for idle" | Espresso checks for background tasks/animations. If idle, proceeds. If not, retries for ~5s before failing. |
| "withId/withText are matchers" | Matchers are predicates. onView finds first matching view in hierarchy. Multiple matches = ambiguous, fails. |
| "RecyclerViewActions scrolls to position" | Scrolls RecyclerView until item at position visible (or throws exception). Different from manual scroll. |

</details>

---

## 32. ProGuard/R8 Obfuscation Gotchas

### Common R8 Issues

> **TL;DR:** R8 obfuscates & shrinks code for release. Enable `minifyEnabled true` + `shrinkResources true`. Use `-keep` rules for reflection (data classes, Retrofit models, callbacks).

R8 obfuscation · Keep rules · Shrinking · Testing obfuscated APK

<details>
<summary>💻 Code Example</summary>

```gradle
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true  // Remove unused resources too
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

</details>

**ProGuard rules (proguard-rules.pro):**
<details>
<summary>💻 Code Example</summary>

```pro
-keep class com.example.data.** { *; }  # Reflection/serialization
-keepclasseswithmembernames interface com.example.callbacks.** { *; }  # Callbacks
-keepclassmembers enum * { *; }  # Enum values
-keep class retrofit2.** { *; }  # Keep Retrofit
-keepnames class com.example.api.**  # Keep names, obfuscate members
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### R8 Pipeline

**1. Parse:** Read APK classes, detect unused code.
**2. Shrink:** Remove unused classes/members/fields.
**3. Optimize:** Inline methods, remove dead code.
**4. Obfuscate:** Rename classes/members to short names (a, b, c...).
**5. Preverify:** Generate stack maps for dexer.

**Keep rules prevent removal/obfuscation:**
- `-keep` = keep as-is, don't remove or rename
- `-keepclassmembers` = keep members only (class name can rename)
- `-keepnames` = keep names, allow optimization internally

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use -keep for reflection" | Reflection looks up by name at runtime. Obfuscation renames = lookup fails. -keep preserves names. |
| "Test obfuscated APK" | Generate release build locally, test before upload. Crashes from missing -keep rules only appear in release. |
| "Obfuscation reduces APK size" | Renamed classes/methods are shorter (e.g., `onBindViewHolder` → `a`). Significant size reduction. |

### Gotchas at depth

- **Over-keeping:** Keeping too many classes negates shrinking benefits. Use specific package patterns, not global `-keep`.
- **Third-party libraries:** Library authors should publish proper ProGuard rules. Import via aar:proguard_rules.
- **Runtime errors in release only:** If -keep missing, app crashes in release but works in debug. Use Firebase Crashlytics to detect.

</details>

---

## 33. RxJava vs. Coroutines Comparison

### Mental Model Differences

> **TL;DR:** RxJava = stream abstraction, threading explicit (observeOn/subscribeOn), built-in backpressure. Coroutines = sequential async code, Dispatchers, auto-cancellation. Coroutines preferred in modern Android.

RxJava for complex streams · Coroutines for readability · Both valid · Migration path exists

|Aspect|RxJava|Coroutines|
|---|---|---|
|Abstraction|Stream of values over time|Sequential async (like threads)|
|Threading|`.observeOn()`, `.subscribeOn()`|Dispatchers (Main, IO, Default)|
|Backpressure|Built-in, auto-negotiated|Manual (Flow.buffer, conflate)|
|Learning|Steep (many operators)|Gentle (reads like sync)|
|Ecosystem|Mature, legacy|Modern, Jetpack|
|Cancellation|Manual Disposable|Auto via Job/CoroutineScope|

### Migration Example (RxJava → Coroutines)

<details>
<summary>💻 Code Example</summary>

```kotlin
// RxJava
fun getUser(id: Int): Observable<User> =
    userApi.getUser(id)
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .map { it.toUser() }

// In ViewModel
disposables.add(
    repo.getUser(id).subscribe(
        { user -> _state.value = UiState.Success(user) },
        { error -> _state.value = UiState.Error(error.message) }
    )
)

// Coroutines
fun getUser(id: Int): Flow<User> =
    flow {
        val user = userApi.getUser(id).toUser()
        emit(user)
    }
        .flowOn(Dispatchers.IO)

// In ViewModel
viewModelScope.launch {
    try {
        val user = repo.getUser(id)
        _state.value = UiState.Success(user)
    } catch (e: Exception) {
        _state.value = UiState.Error(e.message)
    }
}
```

</details>

**RxJava still needed for:**
- Complex stream transformations (switchMap, combineLatest on 3+ streams)
- Existing codebases (migration expensive)
- Backpressure critical (many producers, slow consumer)

---

## 34. Biometric Authentication & In-App Billing

### Biometric Authentication

> **TL;DR:** Use `BiometricPrompt.authenticate()` to show fingerprint/face auth dialog. Override `AuthenticationCallback` for success/error. Combine with `CryptoObject` for secure operations.

BiometricPrompt · Fingerprint/Face · CryptoObject · Callback-based

<details>
<summary>💻 Code Example</summary>

```kotlin
val biometricPrompt = BiometricPrompt(this, ContextCompat.getMainExecutor(this),
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
            val cipher = result.cryptoObject?.cipher
            decryptUserToken(cipher)
        }
        override fun onAuthenticationError(errorCode: Int, errString: CharSequence) {
            showError("Auth failed: $errString")
        }
    }
)

val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Authenticate").setSubtitle("Verify identity").setNegativeButtonText("Cancel").build()
biometricPrompt.authenticate(promptInfo)
```

</details>

### Google Play Billing

> **TL;DR:** Initialize `BillingClient` → `queryProductDetailsAsync()` to list products → `launchBillingFlow()` to start purchase. Handle `BillingResult` for success/error.

BillingClient · queryProductDetails · launchBillingFlow · Purchase state tracking

<details>
<summary>💻 Code Example</summary>

```kotlin
val billingClient = BillingClient.newBuilder(context).setListener { billingResult, purchases ->
    if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
        purchases?.forEach { processPurchase(it) }
    }
}.build()

billingClient.queryProductDetailsAsync(QueryProductDetailsParams.newBuilder()
    .setProductIds(listOf("premium")).setProductType(BillingClient.ProductType.SUBS).build()
) { _, products -> showProducts(products) }

val params = BillingFlowParams.newBuilder().setProductDetailsParamsList(list).build()
billingClient.launchBillingFlow(activity, params)
```

</details>

---

## 35. Data Binding & View Binding Best Practices

### ViewBinding (Type-Safe Views)

> **TL;DR:** Enable `viewBinding true` in build.gradle. Use generated `Binding` classes instead of `findViewById()`. Type-safe, null-safe, no reflection.

Type-safe · Null-safe · Compile-time checking · No reflection

<details>
<summary>💻 Code Example</summary>

```kotlin
android { buildFeatures { viewBinding true } }

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.button.setOnClickListener { binding.text.text = "Clicked!" }
    }
}

class MyFragment : Fragment() {
    private var _binding: FragmentMyBinding? = null
    private val binding get() = _binding!!
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, saved: Bundle?): View {
        _binding = FragmentMyBinding.inflate(inflater, container, false)
        return binding.root
    }
    override fun onDestroyView() { super.onDestroyView(); _binding = null }
}
```

</details>

### Data Binding (Two-Way Binding)

> **TL;DR:** Use `<data>` block in layout XML to bind variables + event handlers. Automatic UI updates when ViewModel data changes. Two-way binding with `@={...}`.

Data binding expressions · Event handlers · Two-way binding · Declarative UI

<details>
<summary>💻 Code Example</summary>

```xml
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <variable name="user" type="com.example.User" />
        <variable name="handler" type="com.example.Handler" />
    </data>
    <LinearLayout android:layout_width="match_parent" android:layout_height="match_parent">
        <TextView android:text="@{user.name}" />
        <Button android:onClick="@{handler::onButtonClick}" />
    </LinearLayout>
</layout>
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
        binding.user = User("Alice")
        binding.handler = MyClickHandler()
    }
}
```

</details>

---

## 36. Feature Flags & A/B Testing

### Remote Config Feature Flags

> **TL;DR:** Firebase Remote Config stores feature flags server-side. `fetchAndActivate()` to fetch, `getBoolean()/getLong()` to read. Decouple deployments from feature releases.

Firebase Remote Config · Server-driven features · Zero-downtime rollout

<details>
<summary>💻 Code Example</summary>

```kotlin
val remoteConfig = Firebase.remoteConfig
remoteConfig.setDefaultsAsync(mapOf("show_new_ui" to false, "api_timeout" to 30L))
remoteConfig.fetchAndActivate().addOnCompleteListener { task ->
    if (task.isSuccessful) {
        if (remoteConfig.getBoolean("show_new_ui")) loadNewUI() else loadLegacyUI()
    }
}
```

</details>

### Local Feature Flags (BuildConfig)

> **TL;DR:** Use `buildConfigField` to define compile-time flags (debug vs release). Access via `BuildConfig.FEATURE_NAME`. Fast, no network calls.

BuildConfig fields · Compile-time constants · Per-buildType configuration

<details>
<summary>💻 Code Example</summary>

```gradle
android {
    buildTypes {
        debug { buildConfigField "boolean", "DEBUG_LOGGING", "true" }
        release { buildConfigField "boolean", "DEBUG_LOGGING", "false" }
    }
}
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
if (BuildConfig.DEBUG_LOGGING) enableDebugLogging()
```

</details>

### A/B Testing Pattern

> **TL;DR:** Hash userId + testName to consistently assign variant. Log to analytics. Compare metrics between control and variant.

Deterministic assignment · Analytics tracking · Variant tracking

<details>
<summary>💻 Code Example</summary>

```kotlin
class ABTestManager {
    fun getVariant(testName: String, userId: String): String {
        val hash = (userId + testName).hashCode() % 100
        return if (hash < 50) "control" else "variant"
    }
}

val variant = abTestManager.getVariant("button_color", userId)
val color = if (variant == "control") Color.BLUE else Color.GREEN
analytics.logEvent("ab_test_assigned", mapOf("test" to "button_color", "variant" to variant))
```

</details>

---

## 37. Weak References & Memory Management

### Reference Types

> **TL;DR:** Strong = normal (kept alive). Soft = kept if memory available (caching). Weak = immediately GC'd if unreachable (listener registries). Use Weak to avoid leaks.

Strong · Soft · Weak · GC reclamation rules

| Type | Collected When | Use |
|---|---|---|
| Strong | Never (GC root) | Normal refs, keep alive |
| Soft | Memory pressure | Caching (keep if possible) |
| Weak | Immediately unreachable | Listeners (auto-cleanup) |
| Phantom | Never; signals death | Cleanup hooks (rare) |

### WeakReference Pattern (Listener Registry)

> **TL;DR:** Store listeners in `WeakReference<T>`. Clean dead refs before publishing. Listeners auto-removed when GC'd (no manual unsubscribe needed).

WeakReference · Auto-cleanup · Listener registry · Memory safe

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ GOOD: Weak refs auto-cleanup
class EventBus {
    private val listeners = mutableListOf<WeakReference<EventListener>>()
    fun subscribe(listener: EventListener) { listeners.add(WeakReference(listener)) }
    fun publish(event: Event) {
        listeners.removeAll { it.get() == null }  // Clean dead refs
        listeners.forEach { it.get()?.onEvent(event) }
    }
}
```

</details>

### WeakHashMap for Caches

> **TL;DR:** `WeakHashMap<K, V>` removes entry when key is unreferenced. Useful for caches tied to object lifetime (prevent keeping objects alive).

WeakHashMap · Key-based reclamation · Automatic cleanup

<details>
<summary>💻 Code Example</summary>

```kotlin
val cache: WeakHashMap<String, User> = WeakHashMap()
cache["user_123"] = User(123, "Alice")
// If String key unreferenced elsewhere, entry auto-removed (prevents memory leak)
```

</details>

---

## 38. App Shortcuts & Widgets

### App Shortcuts

> **TL;DR:** Define in `shortcuts.xml` with shortcutId, icon, labels. Register in manifest via `<meta-data>`. Launcher shows long-press menu with quick actions.

Launcher shortcuts · Intent-based · Quick actions

<details>
<summary>💻 Code Example</summary>

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <shortcut android:shortcutId="compose" android:icon="@drawable/ic_compose">
        <intent android:action="android.intent.action.MAIN" android:targetClass="com.example.ComposeActivity" />
    </shortcut>
</shortcuts>
```

</details>

### Home Screen Widgets

> **TL;DR:** Extend `AppWidgetProvider`, override `onUpdate()`, use `RemoteViews` to build UI. Register receiver in manifest with `APPWIDGET_UPDATE` action.

RemoteViews · AppWidgetProvider · Limited widgets · Home screen

<details>
<summary>💻 Code Example</summary>

```kotlin
class MyWidgetProvider : AppWidgetProvider() {
    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {
        appWidgetIds.forEach { id -> updateAppWidget(context, appWidgetManager, id) }
    }
    private fun updateAppWidget(context: Context, mgr: AppWidgetManager, widgetId: Int) {
        val views = RemoteViews(context.packageName, R.layout.widget_layout)
        views.setTextViewText(R.id.text, "Hello!")
        val intent = Intent(context, MainActivity::class.java)
        val pi = PendingIntent.getActivity(context, 0, intent, PendingIntent.FLAG_IMMUTABLE)
        views.setOnClickPendingIntent(R.id.button, pi)
        mgr.updateAppWidget(widgetId, views)
    }
}
```

</details>

---

## 39. App Bundle vs. APK Distribution

### Dynamic Feature Delivery (App Bundle)

> **TL;DR:** Create dynamic feature modules, request download via `SplitInstallManager.startInstall()`. Google Play splits APK by device config (language, density, architecture). Only install needed APKs.

Dynamic features · Splits · On-demand delivery · Smaller downloads

<details>
<summary>💻 Code Example</summary>

```gradle
plugins { id 'com.android.dynamic-feature' }
dependencies { implementation project(':app') }
```

</details>

<details>
<summary>💻 Code Example</summary>

```xml
<dist:module xmlns:dist="http://schemas.android.com/apk/distribution" dist:onDemand="true" />
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
val splitMgr = SplitInstallManagerFactory.create(context)
val req = SplitInstallRequest.newBuilder().addModule("premium_feature").build()
splitMgr.startInstall(req).addOnCompleteListener { result ->
    if (result.isSuccessful) {
        startActivity(Intent().setClassName(packageName, "com.example.premium.Activity"))
    }
}
```

</details>

---

## 40. Testing Strategies by Scenario

### ViewModel + Fake Repository

> **TL;DR:** Inject FakeRepository into ViewModel. Use `runTest` + `advanceUntilIdle()` for coroutines. Assert state transitions.

Unit tests · Fake dependencies · State assertions · runTest for coroutines

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun loadUser_success() = runTest {
    val fakeRepo = FakeUserRepository()
    val vm = UserViewModel(fakeRepo)
    vm.load(); advanceUntilIdle()
    assertIs<UiState.Success>(vm.state.value)
}
```

</details>

### Compose UI Testing

> **TL;DR:** Use `createComposeRule()`. `setContent {}` to render. Find nodes by text/tag, perform actions, assert visibility.

composeRule · Semantics tree · Assertions · No Android context needed

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun searchWorks() {
    composeRule.setContent { SearchScreen() }
    composeRule.onNodeWithTag("search_field").performTextInput("Alice")
    composeRule.onNodeWithText("Results for Alice").assertIsDisplayed()
}
```

</details>

### Navigation Testing

> **TL;DR:** Use `TestNavHostController`. Set up NavHost with test controller. Verify route after navigation clicks.

TestNavHostController · Route verification · Compose navigation

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun navigateToProfile() {
    val navController = TestNavHostController(ApplicationProvider.getApplicationContext())
    composeRule.setContent {
        NavHost(navController, "home") {
            composable("home") { HomeScreen { navController.navigate("profile/123") } }
        }
    }
    composeRule.onNodeWithText("View Profile").performClick()
    assertEquals("profile/123", navController.currentBackStackEntry?.destination?.route)
}
```

</details>

### E2E Integration Testing

> **TL;DR:** Launch activity with `ActivityScenarioRule`. Perform user flows (login → profile → edit). Assert UI state changes.

End-to-end · User flows · Espresso · Full app testing

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun loginToProfile() = runBlocking {
    onView(withId(R.id.email_field)).perform(typeText("test@example.com"))
    onView(withId(R.id.login_button)).perform(click())
    onView(withText("Profile")).check(matches(isDisplayed()))
}
```

</details>

---

## 41. Lint Warnings to Watch

### Critical Warnings to Fix

> **TL;DR:** MissingPermission, UnreachableCode, MissingSuperCall = errors (fix immediately). RecyclerView handlers, NotFragmentAttached = warnings (fix most cases). Suppress only as last resort.

Lint analysis · Common errors · Suppression via @Suppress

| Warning | Fix |
|---|---|
| MissingPermission | Add `<uses-permission>` + runtime checks |
| UnreachableCode | Remove dead code or fix condition |
| MissingSuperCall | Always call `super.method()` first |
| NotFragmentAttached | Check fragment attached before accessing |
| RecyclerView handlers | Use separate click + long-click handlers |
| SerializedName mismatch | Add `@SerializedName` to match JSON |

**Suppress sparingly:**
<details>
<summary>💻 Code Example</summary>

```kotlin
@Suppress("MissingPermission")  // Verified at boundary
fun getLocation() = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER)
```

</details>

---

## 42. Version Compatibility & Graceful Degradation

### API Level Checks

> **TL;DR:** Check `Build.VERSION.SDK_INT >= Build.VERSION_CODES.API_LEVEL`. Use AndroidX helpers (`ContextCompat`). Provide fallbacks for older APIs.

Backward compatibility · API level guards · Fallback patterns

<details>
<summary>💻 Code Example</summary>

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    requestPermission(Manifest.permission.READ_MEDIA_IMAGES)  // API 33+
} else {
    requestPermission(Manifest.permission.READ_EXTERNAL_STORAGE)  // Older fallback
}

if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PERMISSION_GRANTED) {
    openCamera()  // Safe on all API levels
}
```

</details>

### Feature Detection Over Version Checks

> **TL;DR:** Don't assume all API N+ devices have feature X. Use `PackageManager.hasSystemFeature()` to verify feature exists.

Feature detection · More robust · Handles device variations

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ GOOD: Check feature availability
if (context.packageManager.hasSystemFeature(PackageManager.FEATURE_CAMERA)) {
    openCamera()
} else {
    showUnavailableDialog()  // Device lacks camera
}
```

</details>

---

## 43. Common Interview Red Flags (What NOT to Do)

### Anti-Patterns (Instant Fails)

> **TL;DR:** GlobalScope = memory leak. Mutable objects exposed = state bugs. Blocking calls = ANR. Hardcoded credentials = security. Context leaks = memory. Interviewers test these immediately.

Red flags · Memory safety · Concurrency · Security

| ❌ Anti-Pattern | ✅ Correct |
|---|---|
| `GlobalScope.launch {}` | `viewModelScope.launch {}` (lifecycle-aware) |
| `val items: MutableList<Item>` | `val items: StateFlow<List<Item>>` (encapsulated) |
| `api.getUser().blockingGet()` | `withContext(Dispatchers.IO) { repo.getUser() }` (async) |
| `repo.getUser()` (no error handling) | `try { ... } catch (e: Exception) { ... }` (resilient) |
| `this@Activity` in callback | `WeakReference(this)` (prevent leak) |
| `launch { db.getUser() }` on Main | `launch(Dispatchers.IO) { db.getUser() }` (off Main) |
| `GlobalScope + flow.collect()` | `repeatOnLifecycle(STARTED) { flow.collect() }` (lifecycle-bound) |
| `"https://hardcoded.com"` | `BuildConfig.API_URL` or secrets manager (secure) |

---

## 44. Last-Minute Interview Prep (Night Before)

### Core Topics (Memorize These)

> **TL;DR:** 5 questions interviewers ALWAYS ask. Prepare 1-2 min answers. Think out loud. Show reasoning.

Architecture · Concurrency · Memory · Testing · Offline-first

1. **"Explain your architecture"** → MVVM/MVI + Repository + DI (clear layers, testable)
2. **"How do you avoid ANR?"** → Dispatchers (IO/Default off-Main), coroutineScope lifecycle-aware
3. **"How prevent memory leaks?"** → viewModelScope auto-cancels, SavedStateHandle survives config change, WeakReferences for listeners
4. **"Can you write a test?"** → Fake repository, runTest, advanceUntilIdle(), assert state
5. **"How handle offline?"** → Room as SSOT, sync workers, optimistic updates, conflict resolution

### Live Coding Practice (5 min)
<details>
<summary>💻 Code Example</summary>

```
User + Repository + ViewModel + Composable screen
1. data class User + dao.getUser()
2. repo.getUser() with error handling
3. viewModel with StateFlow + viewModelScope.launch
4. @Composable UI observing state + button triggering load()
```

</details>

### Communication Signals
- ✅ "I'd use Repository here because..." (reasoning)
- ✅ "I haven't done X, but I'd explore Y approach..." (honesty + learning)
- ✅ "How many users? Real-time?" (clarifying questions = seniority)
- ❌ "I don't know" (without follow-up = bad)
- ❌ Silent coding (think out loud)

**🚀 YOU'VE GOT THIS! Confidence + clarity = wins interview.**
