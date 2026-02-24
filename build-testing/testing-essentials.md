[← Back to main index](../../README.md) | [← Back to folder](../README.md)

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

