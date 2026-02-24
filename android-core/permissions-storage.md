[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 18. Permissions & Scoped Storage

### Runtime Permissions Pattern (2026 Modern)

> [!TIP]
> **Use `registerForActivityResult()` with `ActivityResultContracts.RequestPermission()`.** Check permission
> first → show rationale if user denied before → request.

`checkSelfPermission()` · `shouldShowRequestPermissionRationale()` · No onActivityResult needed · Composable

<details>
<summary>💻 Code Example</summary>

```kotlin
class MainActivity : ComponentActivity() {
    private val cameraPermission = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted -> if (isGranted) openCamera() else showDenied() }

    fun requestCamera() {
        when {
            checkSelfPermission(Manifest.permission.CAMERA) == PERMISSION_GRANTED -> openCamera()
            shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> showRationale()
            else -> cameraPermission.launch(Manifest.permission.CAMERA)
        }
    }
}
```

</details>

**Pattern:** Always explain *why* before asking—improves UX and interview signal.

<details>
<summary>🔩 Under the Hood</summary>

### How ActivityResult Contracts Work

**What you write:**
```kotlin
registerForActivityResult(ActivityResultContracts.RequestPermission()) { granted -> ... }
```

**What Android framework does:**
- Registers callback internally with activity lifecycle
- On permission request, system shows dialog
- On response, framework calls your lambda (handles activity death/recreation)
- No manual onActivityResult() override needed

### Why Contracts Over onActivityResult

- **Lifecycle-aware:** Callbacks survive activity recreation (config change)
- **Type-safe:** Contract defines input/output types at compile time
- **Composable:** Can register multiple contracts without collision

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use registerForActivityResult" | Contract is registered early (in init/onCreate), callback stored by activity. System calls it via onActivityResult internally. |
| "Check permission before requesting" | checkSelfPermission caches result. Framework caches OS permission state in PackageManager. |
| "Show rationale if user denied" | shouldShowRequestPermissionRationale is true only AFTER user denies once AND you don't have permission yet. |

### Gotchas at depth

- **Registering too late:** Must register in onCreate/init. Late registration (in onStart) crashes.
- **Process death:** If app is killed between request and response, callback is lost. Use SavedStateHandle for state.
- **Permissions denied forever:** If user selects "Don't ask again", shouldShowRequestPermissionRationale returns false. Direct to app settings.

</details>

### Scoped Storage (API 30+)

> [!TIP] Can't access shared `/sdcard/DCIM` directly. Use app-specific dirs (no permission) OR MediaStore + permission.

App-specific: `getExternalFilesDir()` · MediaStore: `EXTERNAL_CONTENT_URI` · Permissions required · Query SAF for legacy

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ App-specific (auto cleanup, no permission)
val file = File(context.getExternalFilesDir(Environment.DIRECTORY_PICTURES), "photo.jpg")
file.writeBytes(imageBytes)

// ✅ Shared Pictures (needs READ_EXTERNAL_STORAGE)
val values = ContentValues().apply {
    put(MediaStore.Images.Media.DISPLAY_NAME, "photo.jpg")
    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
}
val uri = context.contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)
uri?.let { context.contentResolver.openOutputStream(it)?.write(imageBytes) }
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Why Scoped Storage Exists

**Pre-Android 10:** Apps had unrestricted `/sdcard` access → privacy risk (read any user's photos, financial data, etc).

**Post-Android 10:** MediaStore + SAF (Storage Access Framework) provide controlled access through OS-managed content providers.

### Implementation Details

- **getExternalFilesDir():** Stored in `/Android/data/<package>/files/`. Deleted when app uninstalled. No MediaStore query needed.
- **MediaStore:** Content provider backed by SQLite database. insert() creates entry + returns URI. You write via ContentResolver stream.
- **SAF (Storage Access Framework):** Shows user a document picker. Grants persistent URI access for specific files.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Can't write to DCIM anymore" | MediaStore is the sole interface to shared storage. OS controls all file access. |
| "Need READ_EXTERNAL_STORAGE permission" | Permission gates whether app can see MediaStore results. Without it, queries return empty. |
| "Use app-specific directory" | getExternalFilesDir() is outside MediaStore. Filesystem access direct (for app only). |

### Gotchas at depth

- **Deleted files still in MediaStore:** After delete, MediaStore entry lingers until app recreates DB. Query might return ghosts.
- **Different paths per Android version:** getExternalFilesDir() may be on different physical storage (if dual-storage device). Check isSdCardWritable().
- **Permissions don't guarantee access:** Even with READ_EXTERNAL_STORAGE, can only see MediaStore. Can't list raw files anymore.

</details>

---

