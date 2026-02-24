[← Back to fragments-navigation.md](fragments-navigation.md) | [← Back to folder](README.md)

---

# Fragments & Navigation — Visual Reference

> Visual companion to `fragments-navigation.md`. Every concept rendered as a diagram.

---

## Fragment Lifecycle State Machine

```mermaid
stateDiagram-v2
    [*] --> Created : onCreate()
    Created --> CreateView : onCreateView()
    CreateView --> ViewCreated : onViewCreated()
    ViewCreated --> Started : onStart()
    Started --> Resumed : onResume()
    Resumed --> Paused : onPause()
    Paused --> Resumed : fragment visible again
    Paused --> Stopped : onStop()
    Stopped --> Started : back stack pop / visible again
    Stopped --> DestroyView : onDestroyView()
    DestroyView --> Destroyed : onDestroy()
    Destroyed --> [*]

    note right of ViewCreated : ✅ View is ready\nSetup listeners\nStart observers
    note right of Stopped : ⚠️ NOT guaranteed\non process death!\nUse SavedStateHandle
    note right of DestroyView : ❌ View refs invalid\nUnregister listeners here!
```

---

## Fragment Lifecycle — What's Safe When

```mermaid
flowchart LR
    subgraph GUARANTEED["✅ Always called"]
        G1["onCreate\nonCreateView\nonViewCreated\nonStart\nonResume\nonPause"]
    end
    subgraph NOT_GUARANTEED["⚠️ NOT guaranteed"]
        NG1["onStop (skipped on process death)"]
        NG2["onDestroy (skipped on process death)"]
    end
    subgraph VIEW_ACCESS["View Access Timeline"]
        VA1["onCreateView → first view access"]
        VA2["onViewCreated → setup listeners ✅"]
        VA3["onDestroyView → last chance to unregister"]
        VA4["onDestroy → NO view access ❌"]
    end
```

### View Access Safety

```mermaid
flowchart TD
    OCV["onCreateView\nView created"] --> OVCD["onViewCreated\n✅ Setup: listeners, observers, animations"]
    OVCD --> ON_START["onStart → onResume\n✅ Start animations, request focus"]
    ON_START --> ON_STOP["onStop\n✅ Save state (if reached)"]
    ON_STOP --> ODV["onDestroyView\n✅ Unregister listeners\n❌ Don't access views after this!"]
    ODV --> OD["onDestroy\n❌ No view access\n✅ Cleanup only"]
```

---

## Shared ViewModel — Fragment Communication

```mermaid
flowchart TD
    subgraph ACTIVITY["Activity"]
        VMSTORE["ViewModelStore\n(map of class → instance)"]
        SHARED["SharedViewModel instance\n_selected: StateFlow&lt;Item?&gt;"]
        VMSTORE --> SHARED
    end

    subgraph FRAG_A["Fragment A"]
        FA["activityViewModels()"]
        FA_ACTION["selectItem(item)"]
        FA --> SHARED
        FA_ACTION --> SHARED
    end

    subgraph FRAG_B["Fragment B"]
        FB["activityViewModels()"]
        FB_OBS["collectLatest { showDetails(it) }"]
        FB --> SHARED
        SHARED --> FB_OBS
    end

    style SHARED fill:#1a3a1a,color:#cfc
```

### activityViewModels() — Resolution Path

```mermaid
sequenceDiagram
    participant FA as Fragment A
    participant VS as Activity.ViewModelStore
    participant VM as SharedViewModel

    FA->>VS: viewModels() with Activity key
    VS->>VS: key = "SharedViewModel"
    VS->>VS: exists in map?
    alt Not exists (first access)
        VS->>VM: create SharedViewModel()
        VS->>VS: store in map
    else Exists
        VS-->>FA: return existing instance
    end
    VS-->>FA: SharedViewModel instance ✅
```

---

## Back Stack Management

```mermaid
flowchart TD
    subgraph INITIAL["Initial Stack"]
        H["[Home] ← bottom"]
    end
    subgraph AFTER_NAV["After navigate(Profile)"]
        H2["[Home]"]
        P["[Profile] ← top"]
    end
    subgraph AFTER_NAV2["After navigate(Settings)"]
        H3["[Home]"]
        P2["[Profile]"]
        S["[Settings] ← top"]
    end
    subgraph POPUP["popUpTo(Home, inclusive=false)"]
        H4["[Home] ← kept"]
        NEW_DEST["[NewDest] ← pushed"]
    end

    INITIAL --> AFTER_NAV
    AFTER_NAV --> AFTER_NAV2
    AFTER_NAV2 -->|"popUpTo(Home)"| POPUP
```

### popUpTo — Inclusive vs Non-Inclusive

```mermaid
flowchart LR
    subgraph STACK["Stack: [Home][Profile][Settings]"]
        direction TB
        H_S["Home (bottom)"]
        P_S["Profile"]
        S_S["Settings (top)"]
    end
    subgraph NON_INC["popUpTo(Home, inclusive=false)"]
        NON_RESULT["Pops: Profile, Settings\nKeeps: Home\nResult: [Home]"]
    end
    subgraph INC["popUpTo(Home, inclusive=true)"]
        INC_RESULT["Pops: Profile, Settings, Home\nResult: []  (empty!)"]
    end

    STACK --> NON_INC & INC
```

### NavController.popBackStack() Flow

```mermaid
flowchart TD
    CALL["navController.popBackStack()"]
    EMPTY{"Stack empty?"}
    POP["Pop top entry\ncancel its lifecycle scope"]
    RETURN_TRUE["returns true\nnavigation success"]
    RETURN_FALSE["returns false"]
    FINISH["requireActivity().finish()\nclose the app"]

    CALL --> EMPTY
    EMPTY -->|"No"| POP --> RETURN_TRUE
    EMPTY -->|"Yes"| RETURN_FALSE --> FINISH
```

---

## Fragment Back Stack — ViewPager Edge Case

```mermaid
flowchart LR
    subgraph VP["ViewPager2 with Fragments"]
        TAB0["Tab 0: Home Fragment\n(onCreateView)"]
        TAB1["Tab 1: Search Fragment\n(if offscreen limit=1)"]
        TAB2["Tab 2: Profile Fragment\n(DESTROYED when offscreen)"]
    end
    subgraph LIFECYCLE_NOTES["Lifecycle Notes"]
        L1["Fragment may be destroyed\nwhen swiped off-screen"]
        L2["Setup listeners in onViewCreated\nNOT in onCreate"]
        L3["Use SavedStateHandle\nfor state persistence"]
    end
    VP --> LIFECYCLE_NOTES
```

---

## Process Death — Fragment State Recovery

```mermaid
sequenceDiagram
    participant SYS as Android System
    participant FRAG as Fragment
    participant SSH as SavedStateHandle
    participant DISK as Disk

    Note over FRAG: App in background
    SYS->>SYS: low memory → kill process
    Note over FRAG: onStop NOT called!
    Note over SYS: user returns to app
    SYS->>FRAG: onCreate() fresh start
    SYS->>SSH: restore from disk
    SSH-->>FRAG: count = 42 (restored ✅)
    Note over FRAG: UI shows correct state
```

---

## Navigation Mental Map

```mermaid
mindmap
    root((Navigation))
        FragmentLifecycle
            Created → ViewCreated → Resumed
            onStop NOT guaranteed (process death)
            onDestroyView = unregister listeners
            onDestroy = cleanup only
        SharedViewModel
            activityViewModels()
            Stored in Activity.ViewModelStore
            Survives fragment replacement
            Cleared on Activity.onDestroy
        BackStack
            navigate() = push to stack
            popBackStack() = pop top
            popUpTo() = pop multiple
            inclusive = pop target too
        ProcessDeath
            Skip onStop/onDestroy
            SavedStateHandle = disk-persisted
            Restored BEFORE onCreate
            No Binder limit (vs Bundle)
```
