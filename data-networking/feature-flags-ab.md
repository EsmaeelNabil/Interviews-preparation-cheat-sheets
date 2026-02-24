[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 36. Feature Flags & A/B Testing

### Remote Config Feature Flags

> [!TIP]
> **Firebase Remote Config stores feature flags server-side.** `fetchAndActivate()` to fetch,
> `getBoolean()/getLong()` to read. Decouple deployments from feature releases.

Firebase Remote Config · Server-driven features · Zero-downtime rollout

<details>
<summary>💻 Code Example</summary>

```kotlin
val remoteConfig = Firebase.remoteConfig
remoteConfig.setDefaultsAsync(mapOf("show_new_ui" to false, "api_timeout" to 30L))
remoteConfig.fetchAndActivate().addOnCompleteListener { task ->
    if (task.isSuccessful) {
        if (remoteConfig.getBoolean("show_new_ui")) loadNewUI() else loadLegacyUI()
    }
}
```

</details>

### Local Feature Flags (BuildConfig)

> [!TIP] **Use `buildConfigField` to define compile-time flags (debug vs release).** Access via `BuildConfig.FEATURE_NAME`. Fast, no network calls.

BuildConfig fields · Compile-time constants · Per-buildType configuration

<details>
<summary>💻 Code Example</summary>

```gradle
android {
    buildTypes {
        debug { buildConfigField "boolean", "DEBUG_LOGGING", "true" }
        release { buildConfigField "boolean", "DEBUG_LOGGING", "false" }
    }
}
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
if (BuildConfig.DEBUG_LOGGING) enableDebugLogging()
```

</details>

### A/B Testing Pattern

> [!TIP] Hash userId + testName to consistently assign variant. Log to analytics. Compare metrics between control and variant.

Deterministic assignment · Analytics tracking · Variant tracking

<details>
<summary>💻 Code Example</summary>

```kotlin
class ABTestManager {
    fun getVariant(testName: String, userId: String): String {
        val hash = (userId + testName).hashCode() % 100
        return if (hash < 50) "control" else "variant"
    }
}

val variant = abTestManager.getVariant("button_color", userId)
val color = if (variant == "control") Color.BLUE else Color.GREEN
analytics.logEvent("ab_test_assigned", mapOf("test" to "button_color", "variant" to variant))
```

</details>

---

