[← Back to design-patterns.md](design-patterns.md) | [← Back to folder](README.md)

---

# Design Patterns — Visual Reference

> Visual companion to `design-patterns.md`. Every concept rendered as a diagram.

---

## GoF Patterns Classification

```mermaid
mindmap
    root((GoF Patterns))
        Creational
            Singleton
            Factory Method
            Abstract Factory
            Builder / DSL
            Prototype
        Structural
            Adapter
            Decorator
            Facade
            Proxy
            Composite
        Behavioral
            Observer
            Strategy
            State
            Iterator
            Template Method
            Command
```

---

## Singleton — Kotlin `object` Code Generation

```mermaid
flowchart LR
    subgraph KOTLIN_SRC["Kotlin Source"]
        K["object UserManager {\n  fun getUsers() = listOf()\n}"]
    end
    subgraph JAVA_GEN["Java Bytecode (generated)"]
        J["public final class UserManager {\n  public static final UserManager INSTANCE\n    = new UserManager();  // ← ClassLoader init\n  private UserManager() {}\n  public List getUsers() { return ...; }\n}"]
    end
    KOTLIN_SRC -->|"compiler"| JAVA_GEN
```

### Singleton Thread Safety

```mermaid
sequenceDiagram
    participant JVM as JVM ClassLoader
    participant T1 as Thread 1
    participant T2 as Thread 2

    T1->>JVM: first access to UserManager
    JVM->>JVM: load class (synchronized)
    JVM->>JVM: initialize INSTANCE = new UserManager()
    JVM-->>T1: INSTANCE reference
    T2->>JVM: access UserManager
    JVM-->>T2: same INSTANCE (already initialized)
    Note over JVM: No locking needed after init (JVM guarantee)
```

### Singleton: Testing Problem

```mermaid
flowchart TD
    subgraph TEST_PROBLEM["❌ Singleton — Test Isolation Broken"]
        T1["Test 1:\nUserManager.users = [Alice]"]
        T2["Test 2:\nUserManager.users = [Alice, Bob]"]
        SHARED["⚠️ SHARED STATE\nTest 2 sees Test 1 leftovers"]
        T1 --> SHARED --> T2
    end
    subgraph DI_SOLUTION["✅ DI — Fresh Instance Each Test"]
        F1["Test 1:\nUserManager(FakeRepo())"]
        F2["Test 2:\nUserManager(FakeRepo())"]
        ISOLATED["✅ ISOLATED\nEach test has own instance"]
        F1 --> ISOLATED
        F2 --> ISOLATED
    end
```

---

## Observer Pattern — Callbacks vs Flows

```mermaid
flowchart TD
    subgraph CALLBACK["❌ Callbacks (old)"]
        C_SUB["subscribe(listener)"]
        C_FIRE["notify all listeners"]
        C_LEAK["⚠️ Must unsubscribe\nin onDestroy()\nor MEMORY LEAK"]
        C_NO_OPS["No operators\n(manual filter/map)"]
        C_SUB --> C_FIRE --> C_LEAK
        C_FIRE --> C_NO_OPS
    end
    subgraph FLOW_PAT["✅ Flow (modern)"]
        F_COLLECT["collect { }"]
        F_OPS["map, filter, catch\ncomposable operators"]
        F_SCOPE["Scope cancelled\n→ collection stops\nauto cleanup ✅"]
        F_BP["Backpressure\nbuilt-in ✅"]
        F_COLLECT --> F_OPS --> F_SCOPE
        F_COLLECT --> F_BP
    end
```

### Memory Leak: Callback vs Flow

```mermaid
sequenceDiagram
    participant ACT as Activity
    participant MGR as UserManager (global)

    ACT->>MGR: subscribe(listener)
    Note over ACT: Activity destroyed (back button)
    MGR->>MGR: still holds listener reference
    Note over ACT: ❌ Activity in memory (LEAK!)
    Note over MGR: listener has reference to Activity

    ACT->>ACT: [with Flow]
    ACT->>ACT: viewModelScope.launch { collect() }
    Note over ACT: ViewModel cleared → scope cancelled
    Note over ACT: ✅ collect() cancelled, no leak
```

### Flow Backpressure

```mermaid
sequenceDiagram
    participant P as Producer (fast)
    participant F as Flow
    participant C as Collector (slow)

    P->>F: emit(1)
    F->>C: deliver(1)
    Note over C: processing... (100ms)
    P->>F: emit(2)
    Note over F: SUSPEND producer\n(backpressure)
    C-->>F: done!
    F->>C: deliver(2)
    F-->>P: resume producing
```

---

## Factory Pattern

```mermaid
flowchart TD
    subgraph DIRECT["Direct Constructor ❌"]
        DC["HttpClient(\n  timeout=30000,\n  headers=defaultHeaders(),\n  interceptors=listOf(LoggingInterceptor()),\n  retryPolicy=RetryPolicy.Exponential\n)"]
        DC_PROB["Caller must know ALL params\nComplex, error-prone"]
    end
    subgraph FACTORY_CLS["Factory Class"]
        FC["class HttpClientFactory {\n  fun create(timeout=30000): HttpClient {\n    return HttpClient(timeout, defaultHeaders(), ...)\n  }\n}"]
        FC_USAGE["HttpClientFactory().create(timeout=60000)"]
        FC --> FC_USAGE
    end
    subgraph DSL_BUILDER["DSL Builder ✅ (most idiomatic)"]
        DSL["httpClient {\n  timeout = 60000\n  retryCount = 5\n}"]
        DSL_HOW["fun httpClient(block: Builder.() -> Unit): HttpClient\nLambda with receiver → Builder"]
        DSL --> DSL_HOW
    end
```

### DSL Builder — Receiver Scope

```mermaid
flowchart LR
    CALL["httpClient { timeout = 60000 }"]
    EXPAND["httpClient {\n  // this = HttpClientBuilder\n  this.timeout = 60000\n}"]
    RESULT["HttpClient(timeout=60000, defaults...)"]
    CALL -->|"receiver injection"| EXPAND
    EXPAND -->|"builder.build()"| RESULT
```

### Factory vs DI

```mermaid
flowchart LR
    subgraph FACTORY_WAY["Factory Pattern"]
        FW["val client = HttpClientFactory()\n  .create(debug = true)"]
        FW_NOTE["Explicit\nManual\nNo framework"]
    end
    subgraph DI_WAY["Dependency Injection"]
        DW["@Provides\nfun provideClient(factory: HttpClientFactory): HttpClient\n  = factory.create(debug = BuildConfig.DEBUG)"]
        DW_NOTE["Declarative\nAuto-injected\nFramework manages"]
    end
    subgraph HYBRID["Hybrid (common)"]
        HW["Factory creates\nDI injects\nBest of both"]
    end
    FACTORY_WAY --> HYBRID
    DI_WAY --> HYBRID
```

---

## Repository Pattern

```mermaid
flowchart TD
    subgraph DOMAIN["Domain Layer"]
        REPO_INT["interface UserRepository {\n  suspend fun getUser(id: Int): User\n  suspend fun saveUser(user: User)\n}"]
    end
    subgraph DATA["Data Layer"]
        REPO_IMPL["class UserRepositoryImpl(\n  api: UserApi,\n  db: UserDao,\n  cache: UserCache\n) : UserRepository"]
    end
    subgraph TEST["Test"]
        FAKE["class FakeUserRepository : UserRepository {\n  override suspend fun getUser(id) = User(id, 'Test')\n}"]
    end
    REPO_INT -.->|"implemented by"| REPO_IMPL
    REPO_INT -.->|"implemented by"| FAKE
```

### Cache-Through Strategy

```mermaid
flowchart TD
    CALL["getUser(id)"]
    C1{"Cache\nhit?"}
    C1 -->|"✅ Yes"| RETURN_C["return cached user\n(fastest)"]
    C1 -->|"❌ No"| C2{"DB\nhit?"}
    C2 -->|"✅ Yes"| UPDATE_C["update cache\nreturn DB user"]
    C2 -->|"❌ No"| API["fetch from API"]
    API --> SAVE["save to DB\nsave to cache"]
    SAVE --> RETURN_A["return API user"]
```

### Repository as Anti-Corruption Layer

```mermaid
flowchart LR
    subgraph UI_DOMAIN["UI expects"]
        UI["User(id, name, email)"]
    end
    subgraph REPO_LAYER["Repository translates"]
        REPO["UserRepositoryImpl\nmaps all sources to User"]
    end
    subgraph SOURCES["Data sources (different shapes)"]
        API_DTO["API: {userId, fullName, emailAddress}"]
        DB_ROW["DB: users table (snake_case columns)"]
        CACHE["Cache: custom object"]
    end
    UI --> REPO_LAYER
    REPO_LAYER --> API_DTO & DB_ROW & CACHE
```

### Repository — Testability

```mermaid
sequenceDiagram
    participant TEST as Unit Test
    participant VM as ViewModel
    participant FAKE as FakeUserRepository
    participant REAL as UserRepositoryImpl (not used)

    TEST->>VM: UserViewModel(fakeRepo)
    VM->>FAKE: getUser(1)
    FAKE-->>VM: User(1, "Test")
    VM-->>TEST: state = Success(user)
    Note over REAL: Never called in tests ✅
```

---

## Strategy Pattern in Android

```mermaid
flowchart TD
    subgraph STRATEGY["Strategy Pattern"]
        CTX["Context: Sorter"]
        S1["Strategy A: QuickSort"]
        S2["Strategy B: MergeSort"]
        S3["Strategy C: BubbleSort"]
        CTX -->|"uses"| S1 & S2 & S3
    end
    subgraph KOTLIN_IMPL["Kotlin Implementation"]
        FUNC["// Kotlin: pass function directly\nfun sort(items: List&lt;Int&gt;,\n  comparator: (Int, Int) -> Boolean): List&lt;Int&gt;"]
        USAGE["sort(items) { a, b -> a < b }  // ascending\nsort(items) { a, b -> a > b }  // descending"]
        FUNC --> USAGE
    end
```

---

## State Pattern

```mermaid
stateDiagram-v2
    [*] --> Idle : app start
    Idle --> Loading : search triggered
    Loading --> Success : API returns data
    Loading --> Error : API fails
    Success --> Loading : new search
    Error --> Loading : retry
    Success --> Idle : clear

    note right of Loading : showSpinner()
    note right of Success : showResults()
    note right of Error : showError() + retry button
```

### State Pattern in Sealed Class

```mermaid
flowchart LR
    SEALED["sealed interface UiState {\n  data object Idle : UiState\n  data object Loading : UiState\n  data class Success(val data: List&lt;Item&gt;) : UiState\n  data class Error(val msg: String) : UiState\n}"]
    WHEN["when(state) {\n  is Idle -> hideAll()\n  is Loading -> showSpinner()\n  is Success -> showList(state.data)\n  is Error -> showError(state.msg)\n}"]
    SEALED -->|"consumed by"| WHEN
```

---

## Adapter Pattern

```mermaid
flowchart LR
    subgraph INCOMPATIBLE["Incompatible Interface"]
        OLD["OldApiResponse\n{ user_id: Int, full_name: String }"]
        NEW["UserDomainModel\n{ id: Int, name: String }"]
    end
    subgraph ADAPTER["Adapter / Mapper"]
        MAP["fun OldApiResponse.toDomain(): UserDomainModel =\n  UserDomainModel(id = user_id, name = full_name)"]
    end
    OLD -->|"adapted by"| MAP
    MAP -->|"produces"| NEW
```

---

## Decorator Pattern

```mermaid
flowchart LR
    BASE["base: UserRepository"]
    LOG["LoggingRepository(base)\nadds logging"]
    CACHE_DEC["CachingRepository(log)\nadds caching"]
    METRICS["MetricsRepository(cache)\nadds timing metrics"]

    BASE --> LOG --> CACHE_DEC --> METRICS
    METRICS -->|"used by"| VM2["ViewModel"]
```

---

## Design Patterns — Quick Reference

```mermaid
quadrantChart
    title Pattern Frequency in Android Code
    x-axis Rare --> Common
    y-axis Simple --> Complex
    Repository: [0.9, 0.5]
    Observer/Flow: [0.95, 0.4]
    Factory/Builder: [0.7, 0.3]
    Singleton: [0.8, 0.1]
    Adapter/Mapper: [0.8, 0.2]
    Strategy: [0.5, 0.3]
    Decorator: [0.3, 0.5]
    State: [0.6, 0.4]
    Facade: [0.4, 0.4]
    Command: [0.2, 0.6]
```
