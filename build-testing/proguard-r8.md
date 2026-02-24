[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 32. ProGuard/R8 Obfuscation Gotchas

### Common R8 Issues

> [!WARNING]
> **R8 obfuscates & shrinks code for release. Enable `minifyEnabled true` + `shrinkResources true`.** Use
> `-keep` rules for reflection (data classes, Retrofit models, callbacks).

R8 obfuscation · Keep rules · Shrinking · Testing obfuscated APK

<details>
<summary>💻 Code Example</summary>

```gradle
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true  // Remove unused resources too
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

</details>

**ProGuard rules (proguard-rules.pro):**
<details>
<summary>💻 Code Example</summary>

```pro
-keep class com.example.data.** { *; }  # Reflection/serialization
-keepclasseswithmembernames interface com.example.callbacks.** { *; }  # Callbacks
-keepclassmembers enum * { *; }  # Enum values
-keep class retrofit2.** { *; }  # Keep Retrofit
-keepnames class com.example.api.**  # Keep names, obfuscate members
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### R8 Pipeline

**1. Parse:** Read APK classes, detect unused code.
**2. Shrink:** Remove unused classes/members/fields.
**3. Optimize:** Inline methods, remove dead code.
**4. Obfuscate:** Rename classes/members to short names (a, b, c...).
**5. Preverify:** Generate stack maps for dexer.

**Keep rules prevent removal/obfuscation:**
- `-keep` = keep as-is, don't remove or rename
- `-keepclassmembers` = keep members only (class name can rename)
- `-keepnames` = keep names, allow optimization internally

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use -keep for reflection" | Reflection looks up by name at runtime. Obfuscation renames = lookup fails. -keep preserves names. |
| "Test obfuscated APK" | Generate release build locally, test before upload. Crashes from missing -keep rules only appear in release. |
| "Obfuscation reduces APK size" | Renamed classes/methods are shorter (e.g., `onBindViewHolder` → `a`). Significant size reduction. |

### Gotchas at depth

- **Over-keeping:** Keeping too many classes negates shrinking benefits. Use specific package patterns, not global `-keep`.
- **Third-party libraries:** Library authors should publish proper ProGuard rules. Import via aar:proguard_rules.
- **Runtime errors in release only:** If -keep missing, app crashes in release but works in debug. Use Firebase Crashlytics to detect.

</details>

---

