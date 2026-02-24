[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 24. Analytics & Crash Reporting

### Firebase Analytics Integration

> [!TIP]
> **Initialize `FirebaseAnalytics.getInstance()` → log events with `logEvent(eventName, Bundle)`.** Use
> predefined event constants for standard events (SIGN_UP, PURCHASE). Bundle contains parameters.

Event logging · Predefined events · Bundle parameters · Standard vs. custom

<details>
<summary>💻 Code Example</summary>

```kotlin
val analytics = FirebaseAnalytics.getInstance(context)

analytics.logEvent(FirebaseAnalytics.Event.SIGN_UP, Bundle().apply {
    putString(FirebaseAnalytics.Param.METHOD, "google")
})

analytics.logEvent(FirebaseAnalytics.Event.PURCHASE, Bundle().apply {
    putString(FirebaseAnalytics.Param.ITEM_ID, "item_123")
    putDouble(FirebaseAnalytics.Param.VALUE, 9.99)
    putString(FirebaseAnalytics.Param.CURRENCY, "USD")
})
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Event Batching & Upload

**Framework batches events** in memory, sends to Firebase backend every ~30 seconds or when batch full.

**Local vs. Debug logging:**
- Enable verbose logging: `adb shell setprop log.tag.FA VERBOSE`
- View events in DebugView (real-time, development-only)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Log events with Bundle" | Bundle serialized to JSON. Sent to Firebase backend in batches (HTTP POST). Credentials via google-services.json. |
| "Use predefined event constants" | Firebase recognizes standard events (PURCHASE, SIGN_UP). Tracks automatically in dashboards. Custom events are opaque. |
| "Events are asynchronous" | logEvent() returns immediately (queued). Actual upload happens later. Crashes before upload = event lost. |

### Gotchas at depth

- **PII in events:** Never log user email, phone, payment info in events (privacy violation). Use user_id instead.
- **Event name limits:** Max 32 characters, alphanumeric + underscore. Longer names rejected silently.
- **Parameter count:** Max 25 parameters per event. Firebase silently drops excess.

</details>

### Crash Reporting (Firebase Crashlytics)

> [!TIP]
> Call `FirebaseCrashlytics.getInstance().recordException(exception)` to log crashes. Use `.setCustomKey()` for
> context, `.setUserId()` for user identification. Crashes auto-reported if unhandled.

Uncaught exceptions auto-logged · recordException() for caught · Custom keys · User tracking

<details>
<summary>💻 Code Example</summary>

```kotlin
// Manual crash logging
val exception = Exception("Payment failed")
FirebaseCrashlytics.getInstance().recordException(exception)

// Add context
FirebaseCrashlytics.getInstance().setCustomKey("payment_method", "credit_card")
FirebaseCrashlytics.getInstance().setUserId("user_123")
FirebaseCrashlytics.getInstance().log("Payment attempt started")
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Exception Handling

**Uncaught exceptions:** Thread.UncaughtExceptionHandler installed by Firebase. Catches uncaught crashes, logs locally, crashes app as normal.

**Caught exceptions:** Explicitly call `recordException()` to upload (optional, not crash-level urgent).

**NDK crashes:** Native code crashes via signal handler (SIGSEGV, etc.). Firebase NDK library catches, symbolizes, sends.

### Local Storage & Retry

- **Crash stored locally** in app's cache directory (encrypted)
- **On next startup**, framework uploads to Firebase backend
- **If upload fails**, retried for ~1 week before discarded

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Uncaught crashes auto-reported" | Thread.setDefaultUncaughtExceptionHandler called by Firebase at app init. Receives uncaught exception, logs, re-throws (app crashes). |
| "Custom keys for context" | Custom keys serialized with crash data. Sent together to backend. Helps in debugging but doesn't prevent crash. |
| "setUserId for user grouping" | User ID hashed and sent with crash. Backend groups crashes by user (how many users affected). |

### Gotchas at depth

- **Crash before upload:** If app crashes before next startup, crash might not upload (if app uninstalled). Use Crashlytics web API for manual uploads if critical.
- **Large crashes:** Very large crash logs (>1MB) might be truncated or rejected. Keep logs concise.
- **Testing crashes:** Use `FirebaseCrashlytics.getInstance().crash()` to force a test crash and verify reporting.

</details>

---

