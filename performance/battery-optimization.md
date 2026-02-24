[← Back to main index](../../README.md) | [← Back to folder](../README.md)

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

