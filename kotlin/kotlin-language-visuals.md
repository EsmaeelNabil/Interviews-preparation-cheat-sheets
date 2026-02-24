[← Back to kotlin-language.md](kotlin-language.md) | [← Back to folder](README.md)

---

# Kotlin Language — Visual Reference

> Visual companion to `kotlin-language.md`. Every concept rendered as a diagram.

---

## Class Type Hierarchy

```mermaid
classDiagram
    direction TB
    class Any {
        +equals()
        +hashCode()
        +toString()
    }
    class DataClass {
        +auto equals()
        +auto hashCode()
        +auto toString()
        +auto copy()
        +componentN()
    }
    class SealedClass {
        +exhaustive when
        +restricts subclasses
        +same file/module only
    }
    class SealedInterface {
        +type union
        +multi-inheritance ok
        +no shared state
    }
    class EnumClass {
        +ordinal: Int
        +name: String
        +values()
    }
    class ValueClass {
        +zero allocation
        +erased at runtime
        +boxing in 4 contexts
    }
    class ObjectSingleton {
        +thread-safe init
        +lazy by default
        +no constructor
    }
    Any <|-- DataClass
    Any <|-- SealedClass
    Any <|-- EnumClass
    Any <|-- ValueClass
    Any <|-- ObjectSingleton
    SealedClass <|-- SealedInterface : similar concept
```

---

## PART A — Data Classes: What the Compiler Generates

```mermaid
flowchart LR
    subgraph YOU_WRITE["You Write"]
        DC["data class User\n(val id: Int,\nval name: String)"]
    end
    subgraph COMPILER["Compiler Generates"]
        EQ["equals()\nfield-by-field comparison\n31-multiplier hashCode"]
        HASH["hashCode()\nresult = id.hashCode()\nresult = 31*result + name.hashCode()"]
        TS["toString()\nUser(id=1, name=Alice)"]
        COPY["copy(id=this.id, name=this.name)\nnew instance, no mutation"]
        COMP["component1() = id\ncomponent2() = name\nfor destructuring"]
    end
    DC -->|generates| EQ
    DC -->|generates| HASH
    DC -->|generates| TS
    DC -->|generates| COPY
    DC -->|generates| COMP
```

### Destructuring — How It Works

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Compiler as Kotlin Compiler
    participant JVM

    Dev->>Compiler: val (id, name) = user
    Compiler->>JVM: val id = user.component1()
    Compiler->>JVM: val name = user.component2()
    JVM-->>Dev: id = 1, name = "Alice"
```

### copy() Memory Model

```mermaid
flowchart LR
    original["User(id=1, name='Alice')\n@address 0x1000"]
    copy_call["user.copy(name='Bob')"]
    new_obj["User(id=1, name='Bob')\n@address 0x2000\n⬅ NEW ALLOCATION"]

    original -->|"copy()"| copy_call
    copy_call -->|"always allocates"| new_obj
```

---

## PART B — Extension Functions: Static Dispatch

```mermaid
flowchart TD
    subgraph KOTLIN["Kotlin Source"]
        KT["fun String.isValidEmail(): Boolean\n  = this.contains('@')"]
    end
    subgraph JAVA_BYTECODE["Compiled Java Bytecode"]
        JV["public static boolean isValidEmail(String \$this) {\n  return \$this.contains('@');\n}"]
    end
    subgraph DISPATCH["Dispatch Type"]
        STATIC["⚠️ STATIC DISPATCH\nNot virtual — no polymorphism\nCalled by type at compile time"]
    end
    KOTLIN -->|"compiler transforms"| JAVA_BYTECODE
    JAVA_BYTECODE --> DISPATCH
```

### Extension vs Override — Polymorphism Trap

```mermaid
flowchart TD
    subgraph WRONG["❌ Extension (no polymorphism)"]
        A1["Animal ref = Dog()"]
        EXT["fun Animal.sound() = 'generic'\nfun Dog.sound() = 'woof'"]
        R1["animal.sound() → 'generic'\n(static dispatch, type = Animal)"]
        A1 --> EXT --> R1
    end
    subgraph RIGHT["✅ Virtual method (polymorphism)"]
        A2["Animal ref = Dog()"]
        OVR["open fun Animal.sound()\noverride fun Dog.sound()"]
        R2["animal.sound() → 'woof'\n(virtual dispatch, runtime type = Dog)"]
        A2 --> OVR --> R2
    end
```

### Receiver Chain in Scope Functions

```mermaid
flowchart LR
    USER["user.apply { }\n.also { }\n.run { }"]
    APPLY["apply { }\nreceiver = user\nreturns: user"]
    ALSO["also { }\nit = user\nreturns: user"]
    RUN["run { }\nreceiver = user\nreturns: block result"]
    USER --> APPLY --> ALSO --> RUN
```

---

## PART C — Inline & Reified: Compilation Flow

```mermaid
flowchart TD
    subgraph CALL_SITE["Call Site"]
        CS["val user: User = parseJson(json)"]
    end
    subgraph INLINE_EXPANSION["After Compiler Inlines"]
        EXP["// Body pasted here\nval \$klass = User.class  ← type materialized!\nif (\$klass == User.class) {\n  user = parseUserJson(json)\n}"]
    end
    subgraph WHY["Why Only Inline Can Be Reified"]
        ER["JVM type erasure:\nList&lt;String&gt; → List at runtime\nT is UNKNOWN at runtime"]
        INL["inline = body copied to call site\nactual type inserted by compiler\nT is KNOWN at compile time"]
    end
    CS -->|"inline fun parseJson"| INLINE_EXPANSION
    ER -->|"workaround"| INL
```

### Lambda Allocation: Regular vs Inline

```mermaid
flowchart LR
    subgraph REGULAR["Regular Function"]
        RL["fun process(items, action: (Int)->Unit)"]
        OBJ["🗑️ Lambda Object\nallocated on heap\n~16 bytes + GC pressure"]
        RL --> OBJ
    end
    subgraph INLINE["Inline Function"]
        IL["inline fun process(items, action: (Int)->Unit)"]
        INLINED["✅ Code inlined\nNo lambda object\nDirect method call"]
        IL --> INLINED
    end
```

### Inline Trade-off

```mermaid
quadrantChart
    title Inline Function Trade-offs
    x-axis Small Function --> Large Function
    y-axis Rare Call --> Frequent Call
    "ideal inline": [0.1, 0.9]
    "reified needed": [0.3, 0.5]
    "ok to inline": [0.2, 0.7]
    "avoid inline": [0.8, 0.9]
    "don't inline large": [0.9, 0.3]
```

---

## PART D — suspend / CPS State Machine

```mermaid
flowchart TD
    subgraph YOU_WRITE["You Write"]
        SW["suspend fun getUser(id: Int): User {\n  val cached = cache.get(id)\n  val user = api.fetch(id)  // suspend point\n  return user\n}"]
    end
    subgraph COMPILER_GEN["Compiler Generates (simplified)"]
        CG["fun getUser(id: Int, cont: Continuation&lt;User&gt;): Any {\n  when (cont.label) {\n    0 -> { cont.label = 1; api.fetch(id, cont) }\n    1 -> { return cont.result }\n  }\n}"]
    end
    subgraph RUNTIME["Runtime Execution"]
        S0["State 0: check cache\nThread freed ✅"]
        SUSPEND["⏸ SUSPENDED\ncoroutine = heap object\nthread = free for others"]
        S1["State 1: resume after fetch\nback on thread pool"]
    end
    YOU_WRITE -->|"CPS transform"| COMPILER_GEN
    S0 --> SUSPEND --> S1
```

### Coroutine vs Thread Memory

```mermaid
xychart-beta
    title "Memory: Threads vs Coroutines (for 100K units)"
    x-axis ["1K", "10K", "50K", "100K"]
    y-axis "Memory (MB)" 0 --> 100000
    bar [1000, 10000, 50000, 100000]
    line [1, 10, 50, 100]
```

> Threads: ~1MB each → 100K threads = 100 GB RAM ❌
> Coroutines: ~1KB each → 100K coroutines = 100 MB RAM ✅

---

## PART E — Sealed Class vs Sealed Interface

```mermaid
flowchart TD
    subgraph SEALED_CLASS["sealed class (shared state)"]
        SC["sealed class ApiResponse&lt;T&gt;(val statusCode: Int)"]
        SC_S["Success(data: T, code: Int)"]
        SC_E["Error(msg: String, code: Int)"]
        SC --> SC_S
        SC --> SC_E
    end
    subgraph SEALED_IFACE["sealed interface (type union)"]
        SI["sealed interface UiState"]
        SI_L["data object Loading : UiState"]
        SI_S["data class Success(val data: String) : UiState, Parcelable"]
        SI_E["data class Error(val msg: String) : UiState"]
        SI --> SI_L
        SI --> SI_S
        SI --> SI_E
    end
```

### When to Use Which

```mermaid
flowchart TD
    Q{Do subtypes share\ncommon fields/state?}
    Q -->|Yes| SC["✅ sealed class\nexample: all have statusCode: Int"]
    Q -->|No| Q2{Need subtype to also\nextend another interface?}
    Q2 -->|Yes| SI["✅ sealed interface\nexample: UiState + Parcelable"]
    Q2 -->|No| EITHER["Either works\nprefer sealed interface\nmore flexible"]
```

### Compiler Exhaustiveness Check

```mermaid
flowchart LR
    subgraph PERMITTED["Permitted Subclasses (compiler tracked)"]
        LIST["Loading\nSuccess\nError"]
    end
    subgraph WHEN_EXPR["when(state) expression"]
        W1["Loading -> showSpinner()"]
        W2["Success -> showData()"]
        MISSING["❌ Error missing\n→ COMPILE ERROR"]
    end
    PERMITTED -->|"enforces"| WHEN_EXPR
```

---

## PART F — Value Class Boxing Scenarios

```mermaid
flowchart TD
    VC["@JvmInline value class UserId(val value: Int)"]

    VC --> D1["val id: UserId = UserId(123)\n✅ No allocation — erased to Int"]
    VC --> D2["val boxed: Any = id\n❌ BOXED — wrapper object created"]
    VC --> D3["val nullable: UserId? = id\n❌ BOXED — null needs object reference"]
    VC --> D4["val list: List&lt;UserId&gt; = listOf(id)\n❌ BOXED — generic container"]
    VC --> D5["interface method returning UserId\n❌ BOXED — interface boundary"]

    style D1 fill:#1a5c1a,color:#fff
    style D2 fill:#5c1a1a,color:#fff
    style D3 fill:#5c1a1a,color:#fff
    style D4 fill:#5c1a1a,color:#fff
    style D5 fill:#5c1a1a,color:#fff
```

### Value Class: JVM Bytecode Transform

```mermaid
flowchart LR
    subgraph KOTLIN_SRC["Kotlin Source"]
        KT["fun sendEmail(userId: UserId, email: Email)"]
    end
    subgraph JVM_BYTECODE["JVM Bytecode (erased)"]
        JV["static void sendEmail(int userId, String email)"]
    end
    KOTLIN_SRC -->|"compile"| JVM_BYTECODE
    note["UserId wrapper DOESN't\nexist at runtime"]
    JVM_BYTECODE --- note
```

---

## PART G — Flow Operators Decision Tree

```mermaid
flowchart TD
    START([Transforming a Flow?])
    START --> Q1{New inner flow\nper upstream item?}
    Q1 -->|Yes| Q2{Cancel old when\nnew arrives?}
    Q1 -->|No| Q3{Rate limiting needed?}

    Q2 -->|Yes| FML["flatMapLatest\n✅ Search autocomplete\nCancels previous inner flow"]
    Q2 -->|No| Q4{Order matters?}
    Q4 -->|Yes| FMC["flatMapConcat\n✅ Sequential dependencies\nWaits for each inner flow"]
    Q4 -->|No| FMM["flatMapMerge(N)\n✅ Parallel independent\nN concurrent inner flows"]

    Q3 -->|Yes| Q5{Wait for silence\nor emit periodically?}
    Q5 -->|"Wait for silence\n(search input)"| DEB["debounce(300ms)\nEmits only after 300ms gap"]
    Q5 -->|"Periodic\n(click/scroll)"| THR["throttle(500ms)\nMax 1 emit per 500ms"]
    Q3 -->|No| Q6{Drop intermediate\nvalues?}
    Q6 -->|"Only latest matters\n(UI render)"| CON["conflate()\nDrops backlog, keeps latest"]
    Q6 -->|"Decouple speed\n(fast producer)"| BUF["buffer(N)\nProducer ahead by N items"]
```

### Flow Operator Timing Diagrams

```mermaid
sequenceDiagram
    participant U as Upstream
    participant D as debounce(300ms)
    participant C as Collector

    U->>D: emit("a")
    Note over D: timer reset
    U->>D: emit("ab")
    Note over D: timer reset
    U->>D: emit("abc")
    Note over D: 300ms silence...
    D->>C: emit("abc") ✅
```

```mermaid
sequenceDiagram
    participant U as Upstream
    participant FL as flatMapLatest
    participant C as Collector

    U->>FL: emit("cat")
    FL->>C: start inner flow for "cat"
    U->>FL: emit("cats")
    FL->>C: ❌ CANCEL inner flow for "cat"
    FL->>C: start inner flow for "cats"
    C-->>C: only "cats" result delivered
```

### Search Autocomplete Pattern

```mermaid
flowchart LR
    INPUT["searchQuery\nMutableStateFlow"]
    DB["debounce(300)\nwait for pause"]
    DUP["distinctUntilChanged\nskip if same"]
    FML["flatMapLatest\ncancel old search"]
    API["api.search(query)\nnetwork call"]
    CATCH["catch { emit(emptyList()) }\nerror → empty"]
    UI["UI renders results"]

    INPUT --> DB --> DUP --> FML --> API --> CATCH --> UI
```

---

## Summary — Kotlin Language Mental Model

```mermaid
mindmap
    root((Kotlin))
        DataClass
            Auto equals/hashCode/copy
            component1/2 for destructuring
            copy allocates new object
        Extensions
            Static dispatch only
            No private field access
            DSL via receivers
        Inline
            Reified generics
            No lambda allocation
            Code copied to call site
        Sealed
            Exhaustive when
            sealed class = shared state
            sealed interface = type union
        ValueClass
            Zero allocation direct
            Boxing in 4 contexts
            Erased at JVM level
        Flow
            flatMapLatest = cancel
            flatMapConcat = serial
            flatMapMerge = parallel
            debounce = silence
```
