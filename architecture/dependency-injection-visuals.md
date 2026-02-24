[← Back to dependency-injection.md](dependency-injection.md) | [← Back to folder](README.md)

---

# Dependency Injection — Visual Reference

> Visual companion to `dependency-injection.md`. Every concept rendered as a diagram.

---

## Hilt Component Hierarchy

```mermaid
flowchart TD
    APP["SingletonComponent\n@Singleton\n♾️ App lifetime"]
    ARC["ActivityRetainedComponent\n@ActivityRetainedScoped\n🔄 Survives config change"]
    VM_COMP["ViewModelComponent\n@ViewModelScoped\n📱 ViewModel lifetime"]
    ACT["ActivityComponent\n@ActivityScoped\n🎬 Activity lifetime"]
    FRAG["FragmentComponent\n@FragmentScoped\n🧩 Fragment lifetime"]
    VIEW["ViewComponent\n@ViewScoped\n🖼️ View lifetime"]
    SVC["ServiceComponent\n@ServiceScoped\n⚙️ Service lifetime"]

    APP --> ARC & SVC
    ARC --> VM_COMP & ACT
    ACT --> FRAG
    FRAG --> VIEW

    style APP fill:#5c1a1a,color:#fff
    style ARC fill:#1a1a5c,color:#fff
    style VM_COMP fill:#1a5c1a,color:#fff
    style ACT fill:#3d3d00,color:#fff
    style FRAG fill:#2d1a4d,color:#fff
```

### Component Lifetime Visualization

```mermaid
gantt
    title Component Lifetimes (App Session)
    dateFormat X
    axisFormat %s

    section Singleton
    SingletonComponent   :0, 100

    section Config Change
    ActivityRetained     :10, 90
    ViewModel            :20, 80
    ViewModel (after rotate) :35, 70

    section Activity
    Activity 1           :10, 50
    Activity 2 (rotate)  :51, 90

    section Fragment
    Fragment             :20, 45
```

---

## Hilt vs Dagger vs Koin — Decision Tree

```mermaid
flowchart TD
    START([Choosing DI Framework])
    START --> Q1{KMP project?\n(iOS + Android)}
    Q1 -->|Yes| Q2{Simple graph\n&lt; 50 classes?}
    Q1 -->|No| Q3{Legacy Dagger\nalready used?}

    Q2 -->|Yes| MANUAL["Manual DI\n(AppContainer)\nZero overhead, full KMP"]
    Q2 -->|No| KOIN["Koin\nKMP-ready DSL\nRuntime reflection"]

    Q3 -->|Yes| DAGGER["Dagger 2\n(legacy, keep if large)\nManual graph"]
    Q3 -->|No| HILT["Hilt ✅\n(Android standard)\nKSP codegen"]
```

### Compile-time vs Runtime Safety

```mermaid
flowchart LR
    subgraph HILT_SAFE["Hilt / Dagger (compile-time)"]
        H1["@Provides OkHttpClient"]
        H2["@Provides Retrofit(httpClient: OkHttpClient)"]
        H3["Missing binding → 🚨 BUILD FAILS\n(caught before app ships)"]
        H1 --> H2 --> H3
    end
    subgraph KOIN_SAFE["Koin (runtime)"]
        K1["single { OkHttpClient() }"]
        K2["single { Retrofit.Builder().client(get()).build() }"]
        K3["Missing binding → 🚨 CRASH AT RUNTIME\n(caught when code path hit)"]
        K1 --> K2 --> K3
    end
```

---

## Hilt: KSP Codegen Pipeline

```mermaid
flowchart TD
    SRC["Your Source Code\n@HiltAndroidApp\n@AndroidEntryPoint\n@Module @Provides"]
    KSP["KSP Annotation Processor\nscans annotations"]
    GEN["Generated Files\nHilt_MyApp.java\nDaggerAppComponent.java\nMyViewModel_Factory.java"]
    LINK["Linking Phase\nmerge generated + compiled"]
    APK["Final APK\n(zero reflection overhead)"]

    SRC -->|"compile"| KSP
    KSP -->|"generates"| GEN
    GEN & SRC -->|"compile + link"| LINK
    LINK --> APK
```

### Generated Code Structure

```mermaid
classDiagram
    class Hilt_MyApp {
        +GeneratedComponent component
        +onCreate()
    }
    class DaggerAppComponent {
        +inject(MainActivity)
        +userRepository(): UserRepository
    }
    class MyViewModel_Factory {
        +create(): MyViewModel
        -userRepository: UserRepository
    }

    Hilt_MyApp --> DaggerAppComponent : creates
    DaggerAppComponent --> MyViewModel_Factory : uses
```

---

## @Provides vs @Binds

```mermaid
flowchart LR
    subgraph BINDS["@Binds (simple delegation)"]
        B_CODE["@Binds\nabstract fun bind(impl: UserRepositoryImpl): UserRepository"]
        B_GEN["Generated Factory:\nfun get() = impl  ← minimal code"]
        B_CODE -->|"generates"| B_GEN
    end
    subgraph PROVIDES["@Provides (factory logic)"]
        P_CODE["@Provides\nfun provide(client: OkHttpClient): Retrofit =\n  Retrofit.Builder().client(client).build()"]
        P_GEN["Generated Factory:\nfun get() = NetworkModule.provide(httpClient)"]
        P_CODE -->|"generates"| P_GEN
    end
```

### When to Use Which

```mermaid
flowchart TD
    Q{"Need custom\ninitialization logic?"}
    Q -->|Yes| PROVIDES["@Provides\nCustom logic, multiple deps\nConditional creation"]
    Q -->|No| Q2{"Just wrapping\nImpl → Interface?"}
    Q2 -->|Yes| BINDS["@Binds\nSimpler, less generated code\nAbstract module required"]
    Q2 -->|No| PROVIDES2["@Provides\ncomplex scenario"]
```

---

## Scope Binding — Lifetime Rules

```mermaid
flowchart TD
    subgraph SINGLETON["@Singleton\n(app lifetime)"]
        DB["Room Database\nOkHttpClient\nSharedPreferences"]
    end
    subgraph VM_SCOPE["@ViewModelScoped\n(screen lifetime)"]
        REPO["UserRepository\nSearchUseCase\nApiService"]
    end
    subgraph ACT_SCOPE["@ActivityScoped\n(activity lifetime, rare)"]
        NAV["Navigator\nActivity-specific state"]
    end
    subgraph NONE["Unscoped\n(new each injection)"]
        MAPPERS["Mappers\nFormatters\nSimple helpers"]
    end

    SINGLETON -.->|"injected into"| VM_SCOPE
    VM_SCOPE -.->|"injected into"| ACT_SCOPE

    note["⚠️ Can't inject short-lived\ninto long-lived scope\n(memory leak!)"]
```

### Scope Lifetime Mismatch (Bug Pattern)

```mermaid
flowchart LR
    SINGLETON_OBJ["@Singleton ApiManager\n♾️ lives forever"]
    ACTIVITY_OBJ["@ActivityScoped Listener\n🎬 destroyed with Activity"]

    SINGLETON_OBJ -->|"holds reference to"| ACTIVITY_OBJ
    ACTIVITY_OBJ -->|"Activity destroyed\nbut still referenced"| LEAK["🚨 MEMORY LEAK\nActivity can't GC"]
```

---

## Manual DI — Object Graph Construction

```mermaid
flowchart TD
    CONTAINER["AppContainer\n(hand-written factory)"]
    API_SVC["OkHttpApiService\n(created first)"]
    REPO["UserRepositoryImpl\n(needs ApiService)"]
    USE_CASE["GetUserUseCase\n(needs Repository)"]
    VM_FACTORY["SearchViewModelFactory\n(needs UseCase)"]
    VM["SearchViewModel\n(created on demand)"]

    CONTAINER --> API_SVC
    API_SVC --> REPO
    REPO --> USE_CASE
    USE_CASE --> VM_FACTORY
    VM_FACTORY --> VM
```

### DI Framework Comparison

```mermaid
xychart-beta
    title "DI Framework Comparison"
    x-axis ["Setup Effort", "Runtime Perf", "KMP Support", "Compile Safety", "Scale Limit"]
    y-axis "Score (1=bad, 5=best)" 1 --> 5
    line [2, 5, 1, 5, 5]
    line [3, 4, 1, 5, 4]
    line [4, 3, 5, 2, 4]
    line [5, 5, 5, 1, 2]
```

> Lines: Hilt | Dagger | Koin | Manual DI

---

## Koin Module DSL

```mermaid
flowchart TD
    subgraph MODULE["Koin Module Definition"]
        S1["single { OkHttpClient() }\n→ one instance for app"]
        S2["single { Retrofit.Builder().client(get()).build() }\n→ get() resolves OkHttpClient"]
        F1["factory { UserRepository(get()) }\n→ new instance each time"]
        VM_DEF["viewModel { SearchViewModel(get()) }\n→ new per screen"]
    end
    subgraph RESOLVE["Runtime Resolution"]
        R1["get() called"]
        R2["Koin scans registered bindings"]
        R3["Find by type + qualifier"]
        R4["Return instance (single) or create (factory)"]
        R1 --> R2 --> R3 --> R4
    end
```

---

## Hilt Entry Points (Escape Hatch)

```mermaid
flowchart LR
    subgraph NORMAL["Normal Hilt Flow"]
        ACT2["@AndroidEntryPoint\nActivity"]
        INJ["@Inject\nautomatically injected"]
        ACT2 --> INJ
    end
    subgraph ENTRY["Entry Point (manual)"]
        NON_HILT["Non-injectable class\n(custom ContentProvider,\nApplication.onCreate)"]
        EP["@EntryPoint interface\n@InstallIn(SingletonComponent)"]
        EGET["EntryPoints.get(context, EP::class.java)"]
        NON_HILT --> EP --> EGET
    end
```

---

## Full DI Mental Map

```mermaid
mindmap
    root((DI))
        Hilt
            KSP codegen at compile time
            Android lifecycle scopes
            @HiltAndroidApp + @AndroidEntryPoint
            @Provides for factories
            @Binds for delegation
            Android-only
        Dagger
            Manual component graph
            JSR 330 annotations
            Verbose but explicit
            Legacy projects
        Koin
            Runtime reflection
            DSL: single/factory/viewModel
            KMP-ready
            verify() for early detection
        ManualDI
            AppContainer pattern
            Constructor injection
            Zero framework
            Full KMP
            Scales to ~50 classes
        Scopes
            Singleton = app lifetime
            ViewModelScoped = screen
            ActivityScoped = rare
            Unscoped = new each time
```
