[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 43. Common Interview Red Flags (What NOT to Do)

### Anti-Patterns (Instant Fails)

> [!CAUTION]
> **GlobalScope = memory leak. Mutable objects exposed = state bugs. Blocking calls = ANR. Hardcoded credentials
> = security.** Context leaks = memory. Interviewers test these immediately.

Red flags · Memory safety · Concurrency · Security

| ❌ Anti-Pattern | ✅ Correct |
|---|---|
| `GlobalScope.launch {}` | `viewModelScope.launch {}` (lifecycle-aware) |
| `val items: MutableList<Item>` | `val items: StateFlow<List<Item>>` (encapsulated) |
| `api.getUser().blockingGet()` | `withContext(Dispatchers.IO) { repo.getUser() }` (async) |
| `repo.getUser()` (no error handling) | `try { ... } catch (e: Exception) { ... }` (resilient) |
| `this@Activity` in callback | `WeakReference(this)` (prevent leak) |
| `launch { db.getUser() }` on Main | `launch(Dispatchers.IO) { db.getUser() }` (off Main) |
| `GlobalScope + flow.collect()` | `repeatOnLifecycle(STARTED) { flow.collect() }` (lifecycle-bound) |
| `"https://hardcoded.com"` | `BuildConfig.API_URL` or secrets manager (secure) |

---

