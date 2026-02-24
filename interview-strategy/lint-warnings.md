[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 41. Lint Warnings to Watch

### Critical Warnings to Fix

> [!WARNING]
> **MissingPermission, UnreachableCode, MissingSuperCall = errors (fix immediately).** RecyclerView handlers,
> NotFragmentAttached = warnings (fix most cases). Suppress only as last resort.

Lint analysis · Common errors · Suppression via @Suppress

| Warning | Fix |
|---|---|
| MissingPermission | Add `<uses-permission>` + runtime checks |
| UnreachableCode | Remove dead code or fix condition |
| MissingSuperCall | Always call `super.method()` first |
| NotFragmentAttached | Check fragment attached before accessing |
| RecyclerView handlers | Use separate click + long-click handlers |
| SerializedName mismatch | Add `@SerializedName` to match JSON |

**Suppress sparingly:**
<details>
<summary>💻 Code Example</summary>

```kotlin
@Suppress("MissingPermission")  // Verified at boundary
fun getLocation() = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER)
```

</details>

---

