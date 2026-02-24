[← Back to components-lifecycles.md](components-lifecycles.md) | [← Back to folder](README.md)

---

# Android Components & Lifecycles — Visual Reference

> Visual companion to `components-lifecycles.md`. Every concept rendered as a diagram.

---

## Activity Lifecycle State Machine

```mermaid
stateDiagram-v2
    [*] --> Created : onCreate()
    Created --> Started : onStart()
    Started --> Resumed : onResume()
    Resumed --> Paused : onPause()
    Paused --> Resumed : user returns
    Paused --> Stopped : onStop()
    Stopped --> Started : user navigates back
    Stopped --> Destroyed : onDestroy()
    Destroyed --> [*]

    note right of Resumed : ✅ Foreground\nUser interacting\nFull resource access
    note right of Paused : ⚡ Partial visibility\n(dialog / another activity)
    note right of Stopped : ⚠️ Not visible\nProcess may be killed
    note right of Destroyed : onDestroy NOT called\non process death!
```

---

## Services vs WorkManager — Decision Tree

```mermaid
flowchart TD
    Q{"Is work\nuser-visible\nright now?"}
    Q -->|"Yes (music, nav, call)"| FGS["✅ Foreground Service\n+ required notification\n+ process priority boosted"]
    Q -->|No| Q2{"Exact timing\nrequired?"}
    Q2 -->|Yes| ALARM["⚠️ AlarmManager\nsetExactAndAllowWhileIdle\nUse sparingly!"]
    Q2 -->|No| WM["✅ WorkManager\nDoze-safe, persists reboots\nauto-retry, constraints"]

    FGS --> FGS_TYPES["FGS Types (must declare):\ncamera, location, mediaPlayback\ndataSync, microphone, phoneCall..."]
    WM --> WM_TYPES["Worker Types:\nCoroutineWorker (recommended)\nListenableWorker"]
```

### FGS vs WorkManager Comparison

```mermaid
flowchart LR
    subgraph FGS["Foreground Service"]
        F1["User sees notification"]
        F2["Process priority = FOREGROUND"]
        F3["OOM killer won't touch it"]
        F4["API 35+: 6h timeout (dataSync)"]
        F5["API 35+: onTimeout() callback"]
    end
    subgraph WORKM["WorkManager"]
        W1["No notification needed"]
        W2["System defers when optimal"]
        W3["Persists across reboots (Room DB)"]
        W4["Constraints: network, charging..."]
        W5["Min 15-min periodic interval"]
    end
```

### WorkManager Scheduler Pipeline

```mermaid
flowchart TD
    REQUEST["WorkRequest created\n(OneTime or Periodic)"]
    PERSIST["Stored in Room DB\n(persists across reboots)"]
    SCHED["JobScheduler (API 31+)\nor AlarmManager (fallback)"]
    DOZE["Doze-safe\n(JobScheduler exempted)"]
    WORKER["CoroutineWorker.doWork()\nruns in background thread"]
    RETRY["Failed? Retry with\nexponential backoff"]

    REQUEST --> PERSIST --> SCHED --> DOZE --> WORKER
    WORKER -->|failure| RETRY
    RETRY --> WORKER
```

---

## FGS Restrictions Timeline (2026)

```mermaid
timeline
    title Foreground Service Restrictions
    API 26 : Notification channel required
    API 28 : FGS permission in manifest
    API 29 : FGS type required (location, etc.)
    API 34 : FOREGROUND_SERVICE_* permission per type
    API 35 : 6h timeout for dataSync / mediaProcessing
           : onTimeout() callback required
    API 36 : Job quotas on background jobs from FGS
```

---

## Lifecycle Saving — Config Change vs Process Death

```mermaid
flowchart TD
    subgraph TRIGGERS["What triggered it?"]
        ROT["Config change\n(rotation, locale)"]
        PD["Process death\n(system killed app)"]
        BACK["Back press"]
    end

    subgraph ONSAVE["onSaveInstanceState"]
        OS_ROT["✅ Saved & Restored"]
        OS_PD["❌ LOST"]
        OS_BACK["❌ LOST (normal)"]
    end

    subgraph SSH["SavedStateHandle"]
        SSH_ROT["✅ Saved & Restored"]
        SSH_PD["✅ Saved & Restored"]
        SSH_BACK["❌ LOST (intentional)"]
    end

    subgraph ONDESTROY["onDestroy()"]
        OD_ROT["✅ Called"]
        OD_PD["❌ NOT CALLED"]
        OD_BACK["✅ Called"]
    end

    ROT --> OS_ROT & SSH_ROT & OD_ROT
    PD --> OS_PD & SSH_PD & OD_PD
    BACK --> OS_BACK & SSH_BACK & OD_BACK
```

### Binder Bundle — Config Change Flow

```mermaid
sequenceDiagram
    participant ACT as Activity
    participant OS as Android OS
    participant BINDER as Binder IPC
    participant NEW_ACT as New Activity

    ACT->>ACT: onSaveInstanceState(bundle)
    ACT->>BINDER: serialize bundle (≤ 1 MB!)
    OS->>OS: destroy old Activity
    OS->>NEW_ACT: onCreate(bundle)
    BINDER->>NEW_ACT: deserialize bundle
    Note over NEW_ACT: state restored ✅
```

### SavedStateHandle — Process Death Flow

```mermaid
sequenceDiagram
    participant VM as ViewModel
    participant SSH as SavedStateHandle
    participant DISK as Disk (persisted)
    participant OS as Android OS

    VM->>SSH: savedState["userId"] = 42
    SSH->>DISK: persist (not Binder!)
    OS->>OS: kill process (memory pressure)
    Note over OS: user returns to app
    OS->>SSH: restore from disk
    SSH-->>VM: savedState["userId"] = 42 ✅
    Note over VM: ViewModel has restored state!
```

---

## Navigation Compose — Type-Safe Routes

```mermaid
flowchart LR
    subgraph OLD["❌ String Routes (error-prone)"]
        O1["navController.navigate('profile/123')"]
        O2["Typos → runtime crash"]
    end
    subgraph NEW["✅ Type-Safe Routes"]
        N1["@Serializable data class Profile(val userId: String)"]
        N2["navController.navigate(Profile('123'))"]
        N3["entry.toRoute&lt;Profile&gt;().userId"]
        N4["Errors caught at compile time"]
        N1 --> N2 --> N3 --> N4
    end
```

### NavHost Graph

```mermaid
flowchart TD
    NH["NavHost(startDestination = Home)"]
    HOME["composable&lt;Home&gt;\nHomeScreen"]
    PROFILE["composable&lt;Profile&gt;\nProfileScreen(userId)"]
    SETTINGS["composable&lt;Settings&gt;\nSettingsScreen"]

    NH --> HOME
    HOME -->|"navigate(Profile('123'))"| PROFILE
    HOME -->|"navigate(Settings)"| SETTINGS
    PROFILE -->|"popBackStack()"| HOME
```

---

## Android Components Mental Map

```mermaid
mindmap
    root((Components))
        Activity
            onCreate/onStart/onResume
            onPause/onStop/onDestroy
            Config change = recreate
            Process death = no onDestroy
        Services
            FGS = user-visible + notification
            API 35+ = 6h timeout (dataSync)
            onTimeout() = graceful shutdown
            WorkManager preferred for bg
        WorkManager
            Doze-safe
            Persists reboots (Room DB)
            Constraints support
            Min 15-min periodic
        LifecycleSaving
            onSaveInstanceState = Binder (1MB limit)
            SavedStateHandle = disk (no limit)
            onStop = always called
            onDestroy = NOT on process death
        Navigation
            Type-safe routes (Serializable)
            popUpTo + inclusive
            Back stack managed by NavController
            Type-safe args via toRoute()
```
