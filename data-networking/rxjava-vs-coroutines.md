[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 33. RxJava vs. Coroutines Comparison

### Mental Model Differences

> **TL;DR:** RxJava = stream abstraction, threading explicit (observeOn/subscribeOn), built-in backpressure. Coroutines = sequential async code, Dispatchers, auto-cancellation. Coroutines preferred in modern Android.

RxJava for complex streams · Coroutines for readability · Both valid · Migration path exists

|Aspect|RxJava|Coroutines|
|---|---|---|
|Abstraction|Stream of values over time|Sequential async (like threads)|
|Threading|`.observeOn()`, `.subscribeOn()`|Dispatchers (Main, IO, Default)|
|Backpressure|Built-in, auto-negotiated|Manual (Flow.buffer, conflate)|
|Learning|Steep (many operators)|Gentle (reads like sync)|
|Ecosystem|Mature, legacy|Modern, Jetpack|
|Cancellation|Manual Disposable|Auto via Job/CoroutineScope|

### Migration Example (RxJava → Coroutines)

<details>
<summary>💻 Code Example</summary>

```kotlin
// RxJava
fun getUser(id: Int): Observable<User> =
    userApi.getUser(id)
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .map { it.toUser() }

// In ViewModel
disposables.add(
    repo.getUser(id).subscribe(
        { user -> _state.value = UiState.Success(user) },
        { error -> _state.value = UiState.Error(error.message) }
    )
)

// Coroutines
fun getUser(id: Int): Flow<User> =
    flow {
        val user = userApi.getUser(id).toUser()
        emit(user)
    }
        .flowOn(Dispatchers.IO)

// In ViewModel
viewModelScope.launch {
    try {
        val user = repo.getUser(id)
        _state.value = UiState.Success(user)
    } catch (e: Exception) {
        _state.value = UiState.Error(e.message)
    }
}
```

</details>

**RxJava still needed for:**
- Complex stream transformations (switchMap, combineLatest on 3+ streams)
- Existing codebases (migration expensive)
- Backpressure critical (many producers, slow consumer)

---

