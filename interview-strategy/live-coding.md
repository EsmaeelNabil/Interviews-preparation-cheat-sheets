[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 9. Live Coding Survival (25-Minute Strategy)

### The Checklist (Timer Starts)

1. **Clarify** (1 min) — inputs, outputs, edge cases. "Should I handle errors?"
2. **State approach** (1 min) — "ViewModel + StateFlow + Repository"
3. **Skeleton first** (3 min) — data class, ViewModel stub, Composable collecting state
4. **Fill logic** (remaining) — happy path first, error handling last. **Talk while coding.**

### ViewModel + StateFlow + Repository (Full Pattern with Error Handling)

**Quick skeleton (5 lines — happy path):**
<details>
<summary>💻 Code Example</summary>

```kotlin
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow(UiState())
    val state = _state.asStateFlow()
    fun load() { viewModelScope.launch { _state.update { it.copy(user = repo.getUser()) } } }
}
data class UiState(val user: User? = null, val error: String? = null)
```

</details>

**Production version (with errors + loading):**
<details>
<summary>💻 Code Example</summary>

```kotlin
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow<UiState>(UiState.Loading)
    val state = _state.asStateFlow()

    fun load() {
        viewModelScope.launch {
            try {
                val user = repo.getUser()
                _state.value = UiState.Success(user)
            } catch (e: Exception) {
                _state.value = UiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

sealed interface UiState {
    data object Loading : UiState
    data class Success(val user: User) : UiState
    data class Error(val message: String) : UiState
}
```

</details>

**Why sealed interface over data class:** Exhaustive when, prevents invalid states (can't have both user and error), clearer intent.

**Common live-code gotchas:**
1. **Forget `viewModelScope`** → GlobalScope (memory leak)
2. **Not handling errors** → crashes during demo
3. **Accessing `.value` in UI** → doesn't recompose. Use `collectAsStateWithLifecycle()` instead.
4. **State naming:** Suffix with `ViewModel` (UserViewModel), `UiState` or `UiModel` for state class.

**Quick error handling pattern (2 min to write):**
<details>
<summary>💻 Code Example</summary>

```kotlin
_state.update {
    try {
        it.copy(items = repo.getItems(), isLoading = false)
    } catch (e: Exception) {
        it.copy(error = e.message, isLoading = false)
    }
}
```

</details>

### Modularization — If They Ask

**Benefits:** (1) **Faster builds** — unchanged modules skip recompilation. (2) **Enforced boundaries** — no cross-module internal access.

**Pattern:** `:feature:home`, `:feature:profile`, `:core:network`, `:core:data`, `:core:ui`. Convention plugins in `build-logic/`.

---

