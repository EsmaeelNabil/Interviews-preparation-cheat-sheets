[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 37. Weak References & Memory Management

### Reference Types

> [!IMPORTANT]
> **Strong = normal (kept alive). Soft = kept if memory available (caching). Weak = immediately GC'd if
> unreachable (listener registries).** Use Weak to avoid leaks.

Strong · Soft · Weak · GC reclamation rules

| Type | Collected When | Use |
|---|---|---|
| Strong | Never (GC root) | Normal refs, keep alive |
| Soft | Memory pressure | Caching (keep if possible) |
| Weak | Immediately unreachable | Listeners (auto-cleanup) |
| Phantom | Never; signals death | Cleanup hooks (rare) |

### WeakReference Pattern (Listener Registry)

> [!TIP]
> **Store listeners in `WeakReference<T>`. Clean dead refs before publishing.** Listeners auto-removed when GC'd (no manual unsubscribe needed).

WeakReference · Auto-cleanup · Listener registry · Memory safe

<details>
<summary>💻 Code Example</summary>

```kotlin
// ✅ GOOD: Weak refs auto-cleanup
class EventBus {
    private val listeners = mutableListOf<WeakReference<EventListener>>()
    fun subscribe(listener: EventListener) { listeners.add(WeakReference(listener)) }
    fun publish(event: Event) {
        listeners.removeAll { it.get() == null }  // Clean dead refs
        listeners.forEach { it.get()?.onEvent(event) }
    }
}
```

</details>

### WeakHashMap for Caches

> [!TIP]
> **`WeakHashMap<K, V>` removes entry when key is unreferenced.** Useful for caches tied to object lifetime (prevent keeping objects alive).

WeakHashMap · Key-based reclamation · Automatic cleanup

<details>
<summary>💻 Code Example</summary>

```kotlin
val cache: WeakHashMap<String, User> = WeakHashMap()
cache["user_123"] = User(123, "Alice")
// If String key unreferenced elsewhere, entry auto-removed (prevents memory leak)
```

</details>

---

