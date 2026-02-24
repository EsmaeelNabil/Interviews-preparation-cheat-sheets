[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 44. Last-Minute Interview Prep (Night Before)

### Core Topics (Memorize These)

> [!IMPORTANT]
> **5 questions interviewers ALWAYS ask. Prepare 1-2 min answers.** Think out loud. Show reasoning.

**Night Before Checklist:**
- [ ] Review architecture: MVVM/MVI + Repository + DI (1 min prep)
- [ ] Prepare concurrency answer: Dispatchers + lifecycle scope (1 min prep)
- [ ] Memory leaks: viewModelScope, SavedStateHandle, WeakReferences (1 min prep)
- [ ] Testing: Fake repo, runTest, advanceUntilIdle() pattern (2 min prep)
- [ ] Offline-first: Room SSOT, sync workers, optimistic updates (1 min prep)
- [ ] Live code 3x: User + ViewModel + UI quick sketch (5 min practice)
- [ ] Sleep 7+ hours
- [ ] Morning: Light review, coffee, deep breaths

Architecture · Concurrency · Memory · Testing · Offline-first

1. **"Explain your architecture"** → MVVM/MVI + Repository + DI (clear layers, testable)
2. **"How do you avoid ANR?"** → Dispatchers (IO/Default off-Main), coroutineScope lifecycle-aware
3. **"How prevent memory leaks?"** → viewModelScope auto-cancels, SavedStateHandle survives config change, WeakReferences for listeners
4. **"Can you write a test?"** → Fake repository, runTest, advanceUntilIdle(), assert state
5. **"How handle offline?"** → Room as SSOT, sync workers, optimistic updates, conflict resolution

### Live Coding Practice (5 min)
<details>
<summary>💻 Code Example</summary>

```
User + Repository + ViewModel + Composable screen
1. data class User + dao.getUser()
2. repo.getUser() with error handling
3. viewModel with StateFlow + viewModelScope.launch
4. @Composable UI observing state + button triggering load()
```

</details>

### Communication Signals
- ✅ "I'd use Repository here because..." (reasoning)
- ✅ "I haven't done X, but I'd explore Y approach..." (honesty + learning)
- ✅ "How many users? Real-time?" (clarifying questions = seniority)
- ❌ "I don't know" (without follow-up = bad)
- ❌ Silent coding (think out loud)

**🚀 YOU'VE GOT THIS! Confidence + clarity = wins interview.**
