[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 42. Version Compatibility & Graceful Degradation

### API Level Checks

> [!NOTE] **Check `Build.VERSION.SDK_INT >= Build.VERSION_CODES.API_LEVEL`.** Use AndroidX helpers (`ContextCompat`). Provide fallbacks for older APIs.

Backward compatibility · API level guards · Fallback patterns

<details>
<summary>💻 Code Example</summary>

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    requestPermission(Manifest.permission.READ_MEDIA_IMAGES)  // API 33+
} else {
    requestPermission(Manifest.permission.READ_EXTERNAL_STORAGE)  // Older fallback
}

if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PERMISSION_GRANTED) {
    openCamera()  // Safe on all API levels
}
```

</details>

### Feature Detection Over Version Checks

> [!TIP] Don't assume all API N+ devices have feature X. Use `PackageManager.hasSystemFeature()` to verify feature exists.

Feature detection · More robust · Handles device variations

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ GOOD: Check feature availability
if (context.packageManager.hasSystemFeature(PackageManager.FEATURE_CAMERA)) {
    openCamera()
} else {
    showUnavailableDialog()  // Device lacks camera
}
```

</details>

---

