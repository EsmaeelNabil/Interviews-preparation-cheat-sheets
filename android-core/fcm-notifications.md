[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 21. Push Notifications & FCM

### Firebase Cloud Messaging Integration

> **TL;DR:** Extend `FirebaseMessagingService` → override `onMessageReceived()` for data messages → override `onNewToken()` to sync token with backend. Register service + intent-filter in AndroidManifest.

`FirebaseMessagingService` · Data vs Notification messages · Token refresh · PendingIntent for deep links

<details>
<summary>💻 Code Example</summary>

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // Data message = custom logic needed
        remoteMessage.data.takeIf { it.isNotEmpty() }?.let { data ->
            val title = data["title"]
            sendNotification(title, data["body"])
        }
    }

    override fun onNewToken(token: String) {
        uploadTokenToBackend(token)  // Sync with backend
    }

    private fun sendNotification(title: String?, body: String?) {
        val pendingIntent = PendingIntent.getActivity(this, 0, Intent(this, MainActivity::class.java),
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
        val notification = NotificationCompat.Builder(this, "default_channel")
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle(title)
            .setContentIntent(pendingIntent)
            .setAutoCancel(true).build()
        NotificationManagerCompat.from(this).notify(System.currentTimeMillis().toInt(), notification)
    }
}
```

</details>

**AndroidManifest.xml:**
<details>
<summary>💻 Code Example</summary>

```xml
<service android:name=".MyFirebaseMessagingService" android:exported="false">
    <intent-filter><action android:name="com.google.firebase.MESSAGING_EVENT" /></intent-filter>
</service>
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### FCM Message Types

**Data message:**
```json
{"data": {"key": "value"}}
```
- App must handle in `onMessageReceived()`
- Custom logic (e.g., deep link, analytics)
- Works even if app killed (system wakes it)

**Notification message:**
```json
{"notification": {"title": "...", "body": "..."}}
```
- Framework auto-displays in notification bar
- `onMessageReceived()` still called, but redundant
- Tap = deep link (specified in Firebase console)

### Token Management

**onNewToken() fired when:**
- App first installed (initial token)
- User uninstalls/reinstalls app (new token)
- Token refreshed by FCM (~6 months, or security reason)

**Backend must persist token** for targeting. Stale tokens → failed delivery.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "onMessageReceived = data message handler" | FCM service runs in separate process. System wakes app if killed. onMessageReceived called on background thread (non-UI). |
| "Token identifies device+app" | Token scoped to (package, device, Firebase project). Token includes device cert, Firebase project ID. Changing ID = new token. |
| "Send token to backend" | Backend stores mapping: (user_id → token list). On logout, delete token. Prevents push after user leaves. |

### Gotchas at depth

- **App killed = wake-up:** System can start your app to handle FCM message even if user force-stopped it. Set up receivers carefully to avoid wasting battery.
- **Token expiry:** Tokens don't have explicit expiry, but can become invalid if cert rotates. Backend should handle HTTP 401 (re-request token).
- **Notification click handler:** Pending intent launched activity may be already running. Use `Intent.FLAG_ACTIVITY_SINGLE_TOP` to avoid duplicate instances.

</details>

### Token Sync & Management

> **TL;DR:** On app startup, get current token via `FirebaseMessaging.getInstance().token`. Sync with backend. Listen for `onNewToken()` refreshes.

Startup sync · onNewToken callbacks · Backend deduplication

<details>
<summary>💻 Code Example</summary>

```kotlin
// On app startup (in Application class)
FirebaseMessaging.getInstance().token.addOnSuccessListener { token ->
    uploadTokenToBackend(token)
}

// Enable auto-init (default true)
FirebaseMessaging.getInstance().isAutoInitEnabled = true
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Token Lifecycle

**Persistence:** Token stored in SharedPreferences by Firebase library (transparent to app).

**When requested:** `getInstance().token` retrieves from SharedPreferences or fetches fresh if expired.

**Sync strategy:**
```
App startup → get token → POST to /api/device-token → backend stores
On token refresh (onNewToken) → POST to /api/device-token again
```

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Get token on startup" | Firebase lib caches token in encrypted SharedPrefs. getInstance().token checks cache first, fetches async if needed. |
| "Dedup on backend" | Backend should use (device_id, package) as composite key. Prevents duplicate token entries on re-installs. |
| "Token can change without user action" | Firebase rotates tokens periodically or on security event. App must always resync on onNewToken(). |

### Gotchas at depth

- **Timing race:** If you request push targeting before token uploaded, backend has no token. Send token sync FIRST, then request notification.
- **Token stickiness:** Old tokens don't invalidate immediately. FCM may attempt delivery to old token for 28 days. Backend should clean up inactive tokens.
- **Disabled push:** If user disables FCM in settings, token still works but messages are dropped. No callback to notify app (check via isAutoInitEnabled).

</details>

---

