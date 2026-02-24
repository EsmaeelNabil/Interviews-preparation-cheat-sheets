[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 39. App Bundle vs. APK Distribution

### Dynamic Feature Delivery (App Bundle)

> **TL;DR:** Create dynamic feature modules, request download via `SplitInstallManager.startInstall()`. Google Play splits APK by device config (language, density, architecture). Only install needed APKs.

Dynamic features · Splits · On-demand delivery · Smaller downloads

<details>
<summary>💻 Code Example</summary>

```gradle
plugins { id 'com.android.dynamic-feature' }
dependencies { implementation project(':app') }
```

</details>

<details>
<summary>💻 Code Example</summary>

```xml
<dist:module xmlns:dist="http://schemas.android.com/apk/distribution" dist:onDemand="true" />
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
val splitMgr = SplitInstallManagerFactory.create(context)
val req = SplitInstallRequest.newBuilder().addModule("premium_feature").build()
splitMgr.startInstall(req).addOnCompleteListener { result ->
    if (result.isSuccessful) {
        startActivity(Intent().setClassName(packageName, "com.example.premium.Activity"))
    }
}
```

</details>

---

