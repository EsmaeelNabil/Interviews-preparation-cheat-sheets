[← Back to battery-optimization.md](battery-optimization.md) | [← Back to folder](README.md)

---

# Battery Optimization — Visual Reference

> Visual companion to `battery-optimization.md`. Every concept rendered as a diagram.

---

## Doze Mode State Machine

```mermaid
stateDiagram-v2
    [*] --> Active : screen on / motion
    Active --> DozePending : screen off
    DozePending --> Doze : no motion for 30 min
    Doze --> Maintenance : every ~9 hours
    Maintenance --> Doze : maintenance window ends
    Doze --> Active : user unlocks / motion detected

    note right of Active : ✅ Full network\n✅ GPS\n✅ Wakelocks honored
    note right of Doze : ❌ Alarms deferred\n❌ Network suspended\n❌ Wakelocks ignored\n❌ GPS stopped
    note right of Maintenance : ✅ Jobs run briefly\n✅ Network allowed\n✅ Wakelocks honored
```

---

## Doze Mode — Impact on APIs

```mermaid
flowchart TD
    DOZE["📱 Device in Doze Mode\n(screen off, no motion, 30+ min)"]

    DOZE --> ALARM["⏰ AlarmManager\nsetExact() / setRepeating()\n❌ DEFERRED to maintenance window"]
    DOZE --> NET["🌐 Network\nAll requests\n❌ SUSPENDED"]
    DOZE --> GPS["📍 Location Updates\n❌ STOPPED"]
    DOZE --> WAKE["⚡ Partial Wakelocks\nPowerManager.PARTIAL_WAKE_LOCK\n❌ IGNORED"]
    DOZE --> WORK["⚙️ WorkManager / JobScheduler\n✅ DEFERRED (not cancelled)\nruns in next maintenance window"]

    style ALARM fill:#5c1a1a,color:#fff
    style NET fill:#5c1a1a,color:#fff
    style GPS fill:#5c1a1a,color:#fff
    style WAKE fill:#5c1a1a,color:#fff
    style WORK fill:#1a3a1a,color:#cfc
```

---

## WorkManager vs AlarmManager vs JobScheduler

```mermaid
flowchart LR
    subgraph WORK["WorkManager ✅ (recommended)"]
        W1["Respects Doze mode"]
        W2["Batches work efficiently"]
        W3["Persists across reboots"]
        W4["Constraints (network, charging)"]
        W5["Retry with backoff"]
    end
    subgraph ALARM["AlarmManager ⚠️ (for exact timing only)"]
        A1["setAndAllowWhileIdle()"]
        A2["Bypasses Doze ONCE"]
        A3["Throttled if overused (>10x)"]
        A4["No persistence across reboot"]
    end
    subgraph JOB["JobScheduler (deprecated for most cases)"]
        J1["Predecessor to WorkManager"]
        J2["WorkManager uses it internally"]
        J3["Use WorkManager instead"]
    end
```

### Maintenance Window Timeline

```mermaid
gantt
    title Doze Mode — Maintenance Windows
    dateFormat HH:mm
    axisFormat %H:%M

    section Screen Off
    Device idle (screen off)     :00:00, 02:30

    section Doze Mode
    Doze active (first period)   :00:30, 09:30
    Maintenance window #1        :09:30, 09:35
    Doze active (second period)  :09:35, 18:35
    Maintenance window #2        :18:35, 18:40
```

---

## Battery Drain Sources

```mermaid
pie title Battery Drain Breakdown (typical app)
    "CPU Active" : 35
    "Network (cellular)" : 25
    "Screen / GPU" : 20
    "GPS / Location" : 10
    "Wakelocks" : 7
    "Other (sensors)" : 3
```

### Battery Drain by API Usage

```mermaid
xychart-beta
    title "Relative Battery Cost per Operation"
    x-axis ["GPS on", "Cellular TX", "Wakelock 1s", "WiFi TX", "CPU burst", "DB query"]
    y-axis "Relative Cost" 0 --> 100
    bar [100, 80, 60, 40, 30, 5]
```

---

## Battery Stats Inspection

```mermaid
flowchart TD
    ISSUE["App draining battery?"]
    TOOL{"Which tool?"}

    DUMP["adb shell dumpsys batterystats\n→ full session stats\nwakelocks, CPU, network"]
    PROFILER["Android Studio\nEnergy Profiler\n→ real-time CPU/network/GPS"]
    VITALS["Google Play\nAndroid Vitals\n→ production battery alerts"]

    DUMP --> CHECK1["Check: Partial wake lock > 1s?"]
    DUMP --> CHECK2["Check: Background CPU time > 5%?"]
    DUMP --> CHECK3["Check: Network transfers per hour?"]

    CHECK1 & CHECK2 & CHECK3 --> FIX["Apply fixes"]
    FIX --> F1["WorkManager instead of wakelock"]
    FIX --> F2["Batch network requests"]
    FIX --> F3["Release GPS when not needed"]

    ISSUE --> TOOL
    TOOL --> DUMP & PROFILER & VITALS
```

---

## Background Work Decision Tree

```mermaid
flowchart TD
    Q1{"When must work run?"}

    Q1 -->|"Exact time\n(calendar alarm)"| Q_EXACT{"User-visible?"}
    Q1 -->|"Deferrable\n(sync, upload)"| WORK_MAN["✅ WorkManager\nrespects Doze\nbatches efficiently"]
    Q1 -->|"Long-running\n(download, music)"| SERVICE["✅ Foreground Service\n+ Notification\nOS won't kill"]

    Q_EXACT -->|"Yes (reminder)"| ALARM_EXACT["AlarmManager.setExactAndAllowWhileIdle()\n⚠️ Use sparingly"]
    Q_EXACT -->|"No"| WORK_MAN

    WORK_MAN --> W_CON["Add Constraints:\nNetworkType.CONNECTED\nrequiresCharging\nrequiresBatteryNotLow"]
```

### WorkManager Constraint Examples

```mermaid
flowchart LR
    subgraph CONSTRAINTS["WorkManager Constraints"]
        NC["NetworkType.CONNECTED\n(wait for any network)"]
        CC["NetworkType.UNMETERED\n(wait for WiFi)"]
        BC["requiresBatteryNotLow()\n(don't drain low battery)"]
        CHC["requiresCharging()\n(run only while charging)"]
        SC["requiresStorageNotLow()\n(need disk space)"]
    end
    subgraph WHEN_RUNS["Work runs when ALL constraints met"]
        OK["✅ All conditions satisfied\nWorkManager enqueues task"]
    end
    NC & CC & BC & CHC & SC --> OK
```

---

## App Standby Buckets (Android 9+)

```mermaid
flowchart TD
    subgraph BUCKETS["App Standby Buckets"]
        ACTIVE["🟢 ACTIVE\nUser currently using app\nNo restrictions"]
        WORKING["🟡 WORKING SET\nUsed regularly\nFew restrictions"]
        FREQUENT["🟠 FREQUENT\nUsed occasionally\nModerate restrictions"]
        RARE["🔴 RARE\nSeldom used\nHeavy restrictions"]
        RESTRICTED["⛔ RESTRICTED\n(Android 12+)\nNot used in months\nExtreme restrictions"]
    end

    ACTIVE -->|"less usage over time"| WORKING
    WORKING -->|"less usage"| FREQUENT
    FREQUENT -->|"less usage"| RARE
    RARE -->|"very long time"| RESTRICTED
    RESTRICTED -->|"user opens app"| ACTIVE
```

---

## Battery Optimization Mental Map

```mermaid
mindmap
    root((Battery))
        DozeMode
            30 min idle → Doze
            Defers alarms, network, GPS
            Maintenance windows every 9h
            WorkManager = Doze-friendly
        APIs
            WorkManager = deferrable work
            ForegroundService = ongoing
            AlarmManager = exact timing only
            setAndAllowWhileIdle = use sparingly
        DrainSources
            GPS = most expensive
            Cellular TX = high cost
            Partial wakelocks = drain
            Background CPU = significant
        Tools
            dumpsys batterystats
            Android Studio Energy Profiler
            Google Play Android Vitals
        AppStandby
            Active → Working → Frequent → Rare
            Bucket = OS-controlled
            Less usage = more restrictions
```
