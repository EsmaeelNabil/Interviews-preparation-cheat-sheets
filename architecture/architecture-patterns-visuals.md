[← Back to architecture-patterns.md](architecture-patterns.md) | [← Back to folder](README.md)

---

# Architecture Patterns — Visual Reference

> Visual companion to `architecture-patterns.md`. Every concept rendered as a diagram.

---

## MVI vs MVVM — Data Flow Comparison

```mermaid
flowchart LR
    subgraph MVVM["MVVM (scattered state)"]
        V_UI["UI"]
        V_VM["ViewModel"]
        V_L["loading: Flow&lt;Boolean&gt;"]
        V_U["user: Flow&lt;User&gt;"]
        V_E["error: Flow&lt;String?&gt;"]
        V_UI -->|"triggers"| V_VM
        V_VM --> V_L & V_U & V_E
        V_L & V_U & V_E -->|"observe"| V_UI
    end

    subgraph MVI["MVI (unified state)"]
        M_UI["UI"]
        M_VM["ViewModel"]
        M_INT["Intent\n(sealed class)"]
        M_RED["Reducer\n(pure function)"]
        M_ST["UiState\n(single StateFlow)"]
        M_UI -->|"emit"| M_INT
        M_INT -->|"reduce(state, intent)"| M_RED
        M_RED -->|"new state"| M_ST
        M_ST -->|"collect"| M_UI
    end
```

### MVI Unidirectional Flow

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant VM as ViewModel
    participant Reducer
    participant State as StateFlow&lt;UiState&gt;

    User->>UI: tap "Search"
    UI->>VM: intent(Search("cats"))
    VM->>Reducer: reduce(currentState, Search("cats"))
    Reducer-->>VM: UiState(loading=true, query="cats")
    VM->>State: emit new state
    State->>UI: recompose
    UI->>User: show loading spinner

    Note over VM: Side effect: launch API call
    VM->>VM: launchSearchEffect("cats")
    VM->>Reducer: reduce(state, ResultsLoaded(items))
    Reducer-->>VM: UiState(loading=false, results=[...])
    VM->>State: emit
    State->>UI: recompose
    UI->>User: show results
```

### State Explosion — MVVM Problem

```mermaid
flowchart TD
    subgraph INVALID_STATES["Invalid State Combos in MVVM"]
        S1["loading=true\nuser=Alice\nerror=null\n✅ valid"]
        S2["loading=true\nuser=Alice\nerror='oops'\n❌ INVALID"]
        S3["loading=false\nuser=null\nerror=null\n❓ initial or stale?"]
    end
    subgraph MVI_STATES["MVI — Sealed State"]
        MS1["Loading\n(single state)"]
        MS2["Success(user=Alice)\n(single state)"]
        MS3["Error('oops')\n(single state)"]
    end
```

---

## Clean Architecture — Layer Diagram

```mermaid
flowchart TB
    subgraph PRES["Presentation Layer"]
        SC["Compose Screen"]
        VM["ViewModel"]
        SC <-->|"state / events"| VM
    end
    subgraph DOMAIN["Domain Layer\n(pure Kotlin, no Android)"]
        UC["Use Cases\nSearchUseCase\nGetUserUseCase"]
        REPO_INT["Repository Interfaces\nSearchRepository\nUserRepository"]
        MODELS["Domain Models\nUser, SearchResult"]
        UC --> REPO_INT
    end
    subgraph DATA["Data Layer"]
        REPO_IMPL["Repository Impls\nSearchRepositoryImpl"]
        API["Remote Data Source\nRetrofit ApiService"]
        DB["Local Data Source\nRoom DAO"]
        MAP["Mappers\nApi → Domain"]
        REPO_IMPL --> API & DB
        REPO_IMPL --> MAP
    end

    VM -->|"uses"| UC
    REPO_IMPL -.->|"implements"| REPO_INT

    style DOMAIN fill:#1a3a1a,color:#cfc
    style PRES fill:#1a1a4a,color:#ccf
    style DATA fill:#3a1a1a,color:#fcc
```

### Dependency Rule — What Can Import What

```mermaid
flowchart LR
    PRES["Presentation\n(imports Domain)"]
    DOMAIN["Domain\n(imports nothing)"]
    DATA["Data\n(imports Domain)"]

    PRES -->|"✅ allowed"| DOMAIN
    DATA -->|"✅ allowed"| DOMAIN
    PRES -->|"❌ NOT allowed"| DATA
    DATA -->|"❌ NOT allowed"| PRES

    style DOMAIN fill:#1a3a1a,color:#cfc
```

### Gradle Module Structure

```mermaid
flowchart TD
    APP["android:app\n(Presentation)"]
    DOMAIN_MOD[":shared:domain\n(no Android deps)"]
    DATA_MOD[":shared:data\n(Room, Retrofit)"]

    APP -->|"implementation"| DOMAIN_MOD
    DATA_MOD -->|"implementation"| DOMAIN_MOD
    APP -.->|"⛔ blocked by\nGradle transitive"| DATA_MOD
```

---

## KMP: expect / actual Compilation Flow

```mermaid
flowchart TD
    subgraph COMMON["commonMain"]
        EXP["expect fun getPlatformName(): String\n(declaration, placeholder)"]
    end
    subgraph ANDROID["androidMain"]
        ACT_A["actual fun getPlatformName(): String\n= 'Android'"]
    end
    subgraph IOS["iosMain"]
        ACT_I["actual fun getPlatformName(): String\n= 'iOS'"]
    end
    subgraph COMPILER["Compiler Phases"]
        P1["Phase 1: Compile commonMain\nnotes 'expects actual'"]
        P2["Phase 2: Compile platform sources\nmatch expect signatures"]
        P3["Phase 3: Link IR\nreplace expect with actual"]
        P4["Final binary\nactual implementation only"]
        P1 --> P2 --> P3 --> P4
    end

    EXP -.->|"matched with"| ACT_A & ACT_I
    COMPILER --> P1
```

### expect/actual Signature Mismatch Error

```mermaid
flowchart LR
    COM["commonMain\nexpect fun get(): String"]
    AND["androidMain\nactual fun get(): Int  ← WRONG TYPE"]
    ERR["🚨 Compile Error\nExpected: String\nFound: Int"]
    COM -->|"compile"| AND
    AND --> ERR
```

---

## KMP Sharing: ViewModel Architecture

```mermaid
flowchart TD
    subgraph COMMON["commonMain"]
        VM["SearchViewModel : ViewModel()"]
        UC["SearchUseCase"]
        REPO_INT["SearchRepository (interface)"]
        VM --> UC --> REPO_INT
    end
    subgraph ANDROID["androidMain"]
        ANDROID_APP["Android Compose Screen"]
        REPO_A["SearchRepositoryImpl\n(Retrofit + Room)"]
        ANDROID_APP -->|"collectAsStateWithLifecycle"| VM
        REPO_A -.->|implements| REPO_INT
    end
    subgraph IOS["iosMain"]
        SWIFT_VIEW["SwiftUI View"]
        REPO_I["SearchRepositoryImpl\n(Ktor + SQLDelight)"]
        SWIFT_VIEW -->|"for await in state.asAsyncSequence()"| VM
        REPO_I -.->|implements| REPO_INT
    end
```

### SKIE: StateFlow → Swift AsyncSequence

```mermaid
sequenceDiagram
    participant KT as Kotlin (commonMain)
    participant SKIE as SKIE Plugin
    participant SWIFT as Swift

    KT->>SKIE: StateFlow&lt;SearchState&gt;
    SKIE->>SKIE: generate Swift extension
    SKIE->>SWIFT: asAsyncSequence(): AsyncSequence&lt;SearchState&gt;
    SWIFT->>SWIFT: for await state in viewModel.state.asAsyncSequence()
    Note over SWIFT: Native Swift async/await semantics
```

---

## KMP Project Structure

```mermaid
flowchart TD
    ROOT["KMP Project"]
    ROOT --> SHARED["shared/\n(Kotlin Multiplatform)"]
    ROOT --> ANDROID_APP["androidApp/\n(Compose, Jetpack)"]
    ROOT --> IOS_APP["iosApp/\n(Xcode, SwiftUI)"]

    SHARED --> CM["commonMain/\nViewModels, UseCases\nRepositories (interfaces)\nDomain Models"]
    SHARED --> AM["androidMain/\nAndroid actuals\nRoom, Retrofit impls"]
    SHARED --> IM["iosMain/\niOS actuals\nKtor, SQLDelight impls"]

    ANDROID_APP -->|"depends on"| SHARED
    IOS_APP -->|"framework (SPM/CocoaPods)"| SHARED
```

---

## Full Architecture Mental Map

```mermaid
mindmap
    root((Architecture))
        MVI
            Intent sealed class
            Reducer pure function
            Single UiState StateFlow
            Deterministic, debuggable
            Time-travel debugging
        MVVM
            Multiple Flow properties
            Simpler for small screens
            Risk: invalid state combos
        CleanArch
            3 layers: Presentation/Domain/Data
            Domain = pure Kotlin
            Dependency Rule: inward only
            Testable without Android
        KMP
            expect/actual = compile-time substitution
            ViewModels in commonMain
            SKIE for Swift interop
            Koin for DI (not Hilt)
```
