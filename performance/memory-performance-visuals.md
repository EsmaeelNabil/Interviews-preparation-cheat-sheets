[← Back to memory-performance.md](memory-performance.md) | [← Back to folder](README.md)

---

# Memory & Performance — Visual Reference

> Visual companion to `memory-performance.md`. Every concept rendered as a diagram.

---

## Memory Leak Detection Flowchart

```mermaid
flowchart TD
    LEAK["🚨 Memory Leak Suspected\n(OOM, profiler, LeakCanary)"]
    SOURCE{What type?}
    GS["GlobalScope / static field\nholds Activity ref"]
    LIS["Unregistered listener\nFramework holds strong ref"]
    CTX["Lambda captures Context\nimplicit this"]
    COMPOSE["remember captures Activity\nComposition tree holds ref"]

    FIX_GS["✅ Use viewModelScope\nor lifecycleScope"]
    FIX_LIS["✅ Unregister in onStop()\nor repeatOnLifecycle"]
    FIX_CTX["✅ Pass data only\nor use WeakReference"]
    FIX_COMPOSE["✅ rememberUpdatedState\nor LocalContext.current"]
    VERIFY["Run LeakCanary\nverify no leak path"]

    LEAK --> SOURCE
    SOURCE --> GS & LIS & CTX & COMPOSE
    GS --> FIX_GS
    LIS --> FIX_LIS
    CTX --> FIX_CTX
    COMPOSE --> FIX_COMPOSE
    FIX_GS & FIX_LIS & FIX_CTX & FIX_COMPOSE --> VERIFY
```

---

## GC Root Chain — Why Objects Stay Alive

```mermaid
flowchart TD
    subgraph GC_ROOTS["GC Roots (always alive)"]
        STACK["Thread Stacks\n(local variables)"]
        STATIC["Static Fields\n(class-level vars)"]
        JNI["JNI References\n(C++ holding Java objects)"]
        MONITOR["Monitor Objects\n(synchronized locks)"]
    end

    subgraph LEAK_CHAIN["Leak Chain Example"]
        GLOBAL_SCOPE["GlobalScope\n(static, lives forever)"]
        JOB["Coroutine Job\n(held by GlobalScope)"]
        CLOSURE["Lambda closure\n(captured Activity)"]
        ACTIVITY["Activity\n(trapped in heap!)"]
        FRAGMENT["Fragment"]
        VIEW["View"]
        VIEW_MODEL["ViewModel"]

        GLOBAL_SCOPE --> JOB --> CLOSURE --> ACTIVITY
        ACTIVITY --> FRAGMENT & VIEW & VIEW_MODEL
    end

    STATIC --> GLOBAL_SCOPE

    style ACTIVITY fill:#5c1a1a,color:#fff
    style LEAK_CHAIN fill:#2a1a1a
```

### Fix — Scope Lifetime Alignment

```mermaid
flowchart LR
    subgraph BAD["❌ GlobalScope"]
        GS_L["GlobalScope\n♾️ lives forever"]
        JOB_L["Job holds Activity ref"]
        GS_L --> JOB_L
    end
    subgraph GOOD["✅ viewModelScope"]
        VS_L["viewModelScope\n📱 tied to ViewModel"]
        ON_CLEAR["ViewModel.onCleared()\n→ scope cancelled\n→ Activity GC eligible"]
        VS_L --> ON_CLEAR
    end
```

---

## JVM/ART Generational GC — Heap Structure

```mermaid
flowchart TD
    subgraph HEAP["Android Heap (ART)"]
        YOUNG["Young Generation\n~70% of heap\nShort-lived objects\nCollected frequently"]
        OLD["Old Generation\n~30% of heap\nLong-lived objects\nCollected rarely"]
        PERM["Non-moving Space\nClass metadata\nLarge objects"]
    end

    ALLOC["New Object Allocated"] --> YOUNG
    YOUNG -->|"survives 1-2 GC cycles"| OLD
    YOUNG -->|"dies in GC"| FREED1["♻️ Freed"]
    OLD -->|"full GC (rare)"| FREED2["♻️ Freed"]
```

### Strong vs Weak vs Soft References

```mermaid
flowchart LR
    subgraph STRONG["Strong Reference\n(normal)"]
        SG["var ref: Activity = activity"]
        SG_NOTE["GC CANNOT collect\nActivity stays in heap"]
    end
    subgraph WEAK["WeakReference"]
        WK["val ref = WeakReference(activity)"]
        WK_NOTE["GC CAN collect immediately\nref.get() returns null after GC"]
    end
    subgraph SOFT["SoftReference"]
        SF["val ref = SoftReference(bitmap)"]
        SF_NOTE["GC collects ONLY under\nmemory pressure (LRU cache)"]
    end
```

---

## LeakCanary — How It Works

```mermaid
sequenceDiagram
    participant APP as App
    participant LC as LeakCanary
    participant GC as Garbage Collector
    participant HEAP as Heap Analyzer

    APP->>LC: Activity.onDestroy() triggered
    LC->>LC: watch this Activity
    Note over LC: wait 5 seconds
    LC->>GC: force GC()
    GC-->>LC: GC done
    LC->>LC: is Activity still in heap?
    alt Activity collected (no leak)
        LC-->>APP: ✅ No leak
    else Activity still in heap (leak!)
        LC->>HEAP: dump .hprof file
        HEAP->>HEAP: BFS from GC roots to Activity
        HEAP->>HEAP: find shortest path
        HEAP-->>APP: 🚨 Leak: GlobalScope → Job → closure → Activity
    end
```

### LeakCanary Heap Path Analysis

```mermaid
flowchart LR
    GC_ROOT["GC Root\n(static field)"]
    GLOBAL["GlobalScope\ninstance"]
    JOB2["Suspended\nCoroutine Job"]
    LAMBDA["Lambda\n(closure)"]
    ACT["⬅ Activity\n(LEAKED)"]

    GC_ROOT --> GLOBAL --> JOB2 --> LAMBDA --> ACT

    style ACT fill:#5c1a1a,color:#fff
```

---

## Compose Recomposition — Slot Table

```mermaid
flowchart TD
    subgraph COMPOSITION["Composition Tree (in-memory)"]
        COUNTER["Counter @Composable\nSlot 0: MutableIntState(count=5)"]
        BUTTON["Button\nonClick = { count++ }"]
        TEXT["Text\nSlot 0: '5'"]
        COUNTER --> BUTTON --> TEXT
    end
    subgraph RECOMP["When count changes to 6..."]
        STEP1["1. MutableIntState notified"]
        STEP2["2. Counter marked for recomposition"]
        STEP3["3. Counter re-executes"]
        STEP4["4. remember looks up Slot 0 → same object"]
        STEP5["5. count.value = 6 (already updated)"]
        STEP6["6. Button/Text recompose if params changed"]
        STEP1 --> STEP2 --> STEP3 --> STEP4 --> STEP5 --> STEP6
    end
```

### Strong Skipping — Compiler Decision

```mermaid
flowchart TD
    PARENT["Parent recomposes"]
    CHILD_Q{"All params\nstable?"}

    STABLE["String, Int, Boolean\ndata class with stable fields\nImmutableList"]
    UNSTABLE["List&lt;T&gt; (mutable)\nMap&lt;K,V&gt;\nclass without @Stable"]

    SKIP["✅ Skip child\n(no recomposition)"]
    RECOMP2["❌ Recompose child\n(can't trust params unchanged)"]

    PARENT --> CHILD_Q
    CHILD_Q -->|"Yes (stable)"| STABLE --> SKIP
    CHILD_Q -->|"No (unstable)"| UNSTABLE --> RECOMP2
```

### derivedStateOf — Breaking Dependency Chains

```mermaid
flowchart LR
    subgraph WITHOUT["Without derivedStateOf"]
        Q1["query changes"]
        FILTER1["items.filter { } → new List every time"]
        LC1["LazyColumn sees new list object"]
        RECOMP3["Full recompose cascade ❌"]
        Q1 --> FILTER1 --> LC1 --> RECOMP3
    end
    subgraph WITH["With derivedStateOf"]
        Q2["query changes"]
        DERIVED["derivedStateOf { filter } → new State"]
        CHECK["Did filtered result CHANGE?"]
        SKIP2["✅ Same result → skip LazyColumn"]
        RECOMP4["Different result → recompose LazyColumn"]
        Q2 --> DERIVED --> CHECK
        CHECK -->|"no change"| SKIP2
        CHECK -->|"changed"| RECOMP4
    end
```

---

## State Hoisting

```mermaid
flowchart TB
    subgraph STATEFUL["❌ Stateful (un-reusable)"]
        SF1["CounterScreen()"]
        SF2["var count = remember { 0 }"]
        SF3["internal state\nnot testable\nnot previewable"]
        SF1 --> SF2 --> SF3
    end
    subgraph HOISTED["✅ Stateless (hoisted)"]
        H1["CounterScreen(\n  count: Int,\n  onCountChange: (Int) -> Unit\n)"]
        H2["State lives in parent\nor ViewModel"]
        H3["Reusable\nTestable\nPreviewable ✅"]
        H1 --> H2 --> H3
    end
```

### Hoist to Lowest Common Ancestor

```mermaid
flowchart TD
    PARENT2["SearchScreen (holds query state)"]
    SEARCH_BAR["SearchBar\nreads query\nemits onChange"]
    RESULTS["ResultsList\nreads query for filtering"]

    PARENT2 -->|"query: String"| SEARCH_BAR
    SEARCH_BAR -->|"onQueryChange()"| PARENT2
    PARENT2 -->|"query: String"| RESULTS

    note["State hoisted to SearchScreen\n(lowest common ancestor of both children)"]
    PARENT2 --- note
```

---

## Performance Mental Map

```mermaid
mindmap
    root((Performance))
        MemoryLeaks
            GlobalScope → viewModelScope
            Lambda captures → pass data only
            Listeners → repeatOnLifecycle
            LeakCanary detects leaks
        GCRoots
            Thread stacks
            Static fields
            JNI refs
            Reachability = alive
        ComposeRecomp
            Slot table = Composition tree
            remember = cached in slot
            Strong skipping = compiler
            derivedStateOf = break chains
            State hoisting = reusability
        References
            Strong = stays alive
            Weak = GC immediately
            Soft = GC under pressure
            WeakHashMap = key-based cleanup
```
