[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 14. Interview Strategy & Communication Tips

### Live Coding Best Practices

> [!IMPORTANT]
> **Spend 70% on happy path, 20% on errors, 10% on polish.** Clarify requirements first (1 min), sketch
> architecture (1 min), implement visible structure (18 min), then error handling (5 min). Talk
> constantly—interviewers want to hear reasoning.

Time-boxing · Happy path first · Visible architecture · Constant communication · Code quality signals

**Time Budget (25 min total):**

| Phase | Time | Goal | Key Action |
|---|---|---|---|
| **Clarify** | 0-1 min | Write down requirements | Ask about errors, edge cases, scope |
| **Sketch** | 1-2 min | Draw architecture on board | ViewModel + Repository + UI pattern |
| **Stub** | 2-5 min | Class structure only | Data classes, interfaces, minimal logic |
| **Happy path** | 5-20 min | Core feature working | Main flow, happy case, ignore errors |
| **Polish** | 20-25 min | Error handling, edge cases | Try-catch, validation, "nice to have" |

**Code Quality Signals (What Interviewers See):**

1. **Type safety** — sealed interfaces, specific exception types
2. **Naming** — `UserViewModel` not `VM`, `onUserLoaded` not `onSuccess`
3. **Immutability** — `data class`, `val`, immutable collections
4. **Error handling** — try-catch or Result type (not ignored)
5. **Testing-friendly** — injected dependencies, no hardcoded singletons

<details>
<summary>💻 Code Example</summary>

```kotlin
// Strong signal code:
class UserViewModel(private val repo: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow<UiState>(UiState.Loading)
    val state = _state.asStateFlow()

    fun loadUser(id: Int) {
        viewModelScope.launch {
            try {
                val user = repo.getUser(id)
                _state.value = UiState.Success(user)
            } catch (e: IOException) {
                _state.value = UiState.Error("Network error")
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

<details>
<summary>🔩 Under the Hood</summary>

### Why Time-Boxing Matters

**Problem (writing too much):**
```
Interview starts: 2 min questions
Candidate starts coding: spends 20 min on perfect architecture
Interviewer: "We're out of time. Show me it working."
Candidate: "Just need 5 more minutes..."
Result: Interview ends. Feature half-done. Interviewer unsure of ability.
```

**Solution (time-boxing):**
```
Interview starts: 1 min questions
Clarify: 1 min
Sketch: 1 min
Stub: 3 min (data classes, interface structure visible early)
Happy path: 15 min (Feature works, core logic visible)
Error handling: 4 min (Shows robustness)
Result: Interviewer sees working feature + signal of quality.
```

### "Talk While Coding" Psychology

**Why interviewers want you talking:**
- They can't see your thinking (silent coding = black box)
- Communication is 50% of senior engineer skill
- If you're stuck, talking helps them guide you

**Script to start:**
```
"I'll use a ViewModel to manage state, a Repository to abstract the API,
and expose a StateFlow so the UI automatically updates. The ViewModel
launches a coroutine on the IO dispatcher to fetch data without blocking
the main thread. I'll use a sealed interface for UiState to represent
Success/Loading/Error states exhaustively."
```

Communicates:
- Architecture (ViewModel + Repository)
- Concurrency (coroutines, dispatcher)
- Safety (sealed interface, exhaustive when)
- User experience (reactive updates)

### Common Live-Code Mistakes & How to Fix

**Mistake 1: Forgetting viewModelScope**
```kotlin
// ❌ BAD: GlobalScope outlives ViewModel
GlobalScope.launch {
    val user = api.getUser()
}

// ✅ GOOD: Cancelled when ViewModel destroyed
viewModelScope.launch {
    val user = api.getUser()
}
```
**Signal:** Shows understanding of lifecycle, memory safety.

**Mistake 2: Blocking on Main**
```kotlin
// ❌ BAD: withContext still runs on Main (blocks UI)
withContext(Dispatchers.Main) {
    val data = expensiveComputation()  // ANR if too slow
}

// ✅ GOOD: Computation on IO, then Main update
val data = withContext(Dispatchers.IO) {
    expensiveComputation()
}
updateUI(data)  // Implicit Main (in ViewModel)
```
**Signal:** Shows understanding of threading, performance.

**Mistake 3: No error handling**
```kotlin
// ❌ BAD: Happy path only
_state.value = repo.getUser()  // Crashes on error

// ✅ GOOD: Distinguishes error types
try {
    _state.value = repo.getUser()
} catch (e: IOException) {
    _state.value = UiState.Error("Network unavailable")
} catch (e: Exception) {
    _state.value = UiState.Error("Unexpected error")
}
```
**Signal:** Shows production readiness, defensive coding.

### What it reuses & relies on

- **ViewModel lifecycle** — scope tied to ViewModel
- **Coroutine dispatchers** — threading model
- **Sealed interfaces** — exhaustive pattern matching
- **Kotlin syntax** — data classes, extension functions

### Why this design was chosen

**Interview context:** Limited time, high stakes. Prioritize visible working code over perfect abstraction.

**Interviewers evaluate:**
1. Can you solve the problem? (working code)
2. Do you know Android patterns? (ViewModel + Repository)
3. Are you production-ready? (error handling)
4. Can you communicate? (talk while coding)

Spending 70% time on happy path maximizes the chance of showing #1 and #2.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Clarify requirements first" | Ambiguous requirements = wrong solution. Asking shows senior thinking. |
| "Sketch before coding" | Architecture design before implementation. Prevents rewriting mid-interview. |
| "Time-box each section" | Happy path is 15/25 min because core logic matters most. Error handling is polish. |
| "Talk while coding" | Communication = part of assessment. Interviewer guides if you explain thinking. |

### Gotchas at depth

- **Over-engineering for time:** Building perfect architecture takes 10 min. Then no time for logic. Stick to ViewModel + Repository (boring is good).
- **Asking permission too much:** "Is it OK if I...?" costs time. Ask once (requirements), then code confidently.
- **Fixing typos and syntax:** Spend 10 min on `data class` syntax. Ask interviewer: "Remind me the order?" (saves time, shows humility).
- **Running code:** If no IDE, don't try to test. Pseudocode + logic is fine. Testing is separate from live-code signal.

</details>

### System Design Interview Structure

> [!TIP] 5-step interview structure:
> 1. Clarify scope—ask about scale, offline, real-time, conflicts (2 min)
> 2. Sketch architecture—Room + Repository + ViewModel (3 min)
> 3. Deep dive critical paths—load failures, sync conflicts (7 min)
> 4. Trade-offs—why these decisions (2 min)
> 5. Invite follow-up (1 min)

Clarify scope · Sketch architecture · Deep critical paths · Trade-offs · Invite follow-up

**Problem Example:** "Design an offline-capable user profile screen with sync."

**Time Allocation (15 min typical system design):**

| Step | Time | Action | Goal |
|---|---|---|---|
| **Clarify** | 2 min | Ask 4 questions | Define constraints |
| **Architecture** | 3 min | Sketch boxes/arrows | Show structure understanding |
| **Deep dive** | 7 min | Explain critical paths | Show depth, problem-solving |
| **Trade-offs** | 2 min | Why these decisions | Show judgment |
| **Follow-up** | 1 min | Invite questions | Show confidence, readiness |

**Example Clarifying Questions:**

<details>
<summary>💻 Code Example</summary>

```
"Before I design, let me ask:
1. Scale: How many users? Millions → need pagination and sharding?
2. Offline: Completely offline-first, or fetch on open?
3. Real-time: Real-time sync, or eventual consistency OK?
4. Conflicts: Last-write-wins, or ask user to resolve?
5. Updates: Who can edit? Just user, or admins too?"
```

</details>

**Architecture Sketch (3 min—draw on board):**

<details>
<summary>💻 Code Example</summary>

```
UI Layer (Compose)
     ↓ (observes StateFlow)
ViewModel (loads data, manages state)
     ↓ (requests via suspend funs)
Repository (abstraction layer)
     ├─ API Layer (Retrofit + OkHttp)
     └─ Local DB (Room + Coroutines)

Sync Layer (separate):
  WorkManager → Work Queue in Room → Sync Service → API
```

</details>

**Deep Dive: Critical Paths (7 min—talk through each):**

<details>
<summary>💻 Code Example</summary>

```
Scenario 1: First load, no internet
  → Room empty, API fails
  → Show empty state + "Retrying..."
  → When network returns, auto-fetch + cache in Room

Scenario 2: Offline edit, then sync
  → User edits profile (Room updated immediately)
  → WorkManager queues sync task
  → Network returns → execute sync
  → Conflict? Last-write-wins (server timestamp > local)

Scenario 3: Real-time: Other user updates profile
  → Server notifies via WebSocket (or poll)
  → Room invalidated + refetch
  → UI observes Room → auto-updates
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Why This Structure Works

**For interviewer:**
- Clarify: Shows you think before designing (not jumping to code)
- Architecture: Shows understanding of layering
- Deep dive: Shows you think through edge cases
- Trade-offs: Shows judgment (context matters)
- Invite follow-up: Shows confidence (not defensive)

**For candidate:**
- Scope limits prevents over-design
- Architecture gives talking points
- Deep dives show depth
- Trade-offs prevent "best possible" debates
- Follow-up invites guidance if stuck

### Common System Design Mistakes

**Mistake 1: Over-scoping**
```
Candidate designs: "Pagination, infinite scroll, lazy load, image caching,
video streaming, P2P sync, mesh networking, distributed consensus..."
Interviewer: "We have 15 minutes..."
Candidate: "Oh. I'll simplify."
Result: Too late. Interview derailed.
```

**Better:** Scope consciously. "Let me focus on offline-first with Room.
If time, we can add pagination."

**Mistake 2: No critical paths**
```
"So it's Repository → Room + API."
Interviewer: "What if both fail?"
Candidate: "Hmm... I didn't think about that."
Result: Shows lack of depth.
```

**Better:** Pre-think failure modes. "When API fails, we show cached + retry.
When cache missing, show empty state + fetch in background."

**Mistake 3: Defending design without trade-offs**
```
Interviewer: "Why Room as SSOT?"
Candidate: "Because it's better."
Interviewer: "Better how?"
Candidate: "It just is..."
Result: Shows weak judgment.
```

**Better:** "Room as SSOT because: (1) persists across process death,
(2) single consistency point, (3) simpler than distributed cache.
Alternative would be in-memory cache, but then we'd lose data on crash."

### What it reuses & relies on

- **Architecture patterns** (layered, dependency inversion)
- **Android components** (ViewModel, Repository, Room, WorkManager)
- **Concurrency** (coroutines, threading)
- **Consistency models** (eventual consistency, last-write-wins)

### Why this design was chosen

**Interview context:** 15-30 min to evaluate system design thinking.

**Interviewer assesses:**
1. Can you scope problems? (Clarify)
2. Do you know Android patterns? (Architecture)
3. Can you think through edge cases? (Deep dive)
4. Do you have good judgment? (Trade-offs)
5. Are you coachable? (Invite follow-up)

This structure demonstrates all five.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Clarify scope first" | Ambiguous requirements = wrong design. Interviewer tests whether you ask before diving. |
| "Use Room as SSOT" | Single source of truth simplifies consistency. Room survives process death (unlike caches). |
| "Sync offline writes" | WorkManager persists sync work across reboots. Room + timestamps enable conflict resolution. |
| "Show critical paths" | Edge cases (failures) matter more than happy path. Depth = system design thinking. |

### Gotchas at depth

- **Analysis paralysis:** Too many clarifying questions (10+) wastes time. Ask 4-5, then design.
- **Infinite scaling:** "What if 1B users?" Keep it practical. Use Paging 3 + server-side pagina pagination. Don't redesign entire backend.
- **Technology debates:** "But why not Firebase?" Stick to your choice. Defend briefly, move on.
- **Whiteboarding mistakes:** Don't erase. Cross out, draw on top. Interviewer wants to see your thinking process.

</details>

### How to Answer Architecture Questions

> [!TIP]
> Answer formula: (1) "I would..." [solution] (2) "Because..." [reasoning/trade-off] (3) "Alternative..."
> [option B] (4) "Choose A because..." [rationale]. Structured answers signal seniority—shows you think in
> trade-offs, not dogma.

Answer formula · Trade-offs first · Alternatives · Context matters · No dogma

**Interview Question Formula:**

| Question | Your Formula | Why It Works |
|---|---|---|
| "How would you...?" | "I would **[solution]**. Reasoning: **[why]**. Alternative: **[B]**. Choose A because **[rationale]**." | Shows depth: not just right answer, but why |
| "What do you prefer?" | "Depends on context. **[Scenario A]** → **[solution A]**. **[Scenario B]** → **[solution B]**." | Avoids dogma. Shows judgment. |
| "What's the problem with...?" | "The problem is **[specific issue]**. **[Real example]**. Solution: **[fix]**." | Specific, not vague. Backed by example. |

**Real Interview Examples:**

<details>
<summary>💻 Code Example</summary>

```
Q: "How would you handle a slow API?"
A: "I'd cache in Room with TTL. First load: fetch from API → save to Room.
   Subsequent loads: check Room first (instant). If stale (>1 hour), fetch
   fresh in background. If network fails, show cached + 'stale' indicator.
   Reasoning: Fast UX + reliability. Alternative: in-memory cache, but
   would lose on process death. Choose Room because persists + ACID."

Q: "MVI vs MVVM—which do you prefer?"
A: "Depends on complexity. Simple screens (list view): MVVM is simpler.
   Complex screens (search + filter + sort simultaneously): MVI's reducer
   pattern ensures one consistent state path. My last project: MVVM with
   custom logic for complex screen—worked, but MVI would've been cleaner.

Q: "How do you test ViewModel with async?"
A: "I inject a fake Repository returning known values. Use runTest builder
   (virtual clock). Assert state transitions: Loading → Success. Network
   error: Loading → Error. Why: Deterministic (no actual network), fast,
   covers error paths."
```

</details>

**Red Flags (What NOT to Say):**

- ❌ "Room is always better than..." (no always—depends on scale)
- ❌ "I never use GlobalScope" (yes you do, know when it's OK)
- ❌ "The best approach is..." (context matters—what's best for whom?)
- ❌ "Everyone should..." (no dogma in interviews)

### Reverse Questions to Ask

> [!TIP] Ask questions that show thinking about trade-offs and culture fit.
> - **Technical companies:** deep technical questions (modularization, offline strategy)
> - **Product companies:** growth/shipping questions
> - **Team:** "biggest challenge" signals you want to solve real problems, not just pass time

Signal competence · Tailor to company · Cultural fit · Technical depth · Show interest

**Question Taxonomy:**

| Company Type | Why They Care | Your Question | Signal |
|---|---|---|---|
| **Technical** (Bolt, Blinkist) | Code quality, systems | "Modularization at scale? Convention plugins?" | You care about engineering |
| **Product-driven** (Babbel, N26) | Speed, market | "Feature velocity vs. tech debt?" | You understand business |
| **Early-stage** | Survival | "Biggest technical challenge?" | You want to impact |
| **Large** (Google, Meta) | Process, scale | "How do you handle X at scale?" | You think systems |

**Strong Technical Reverse Questions:**

<details>
<summary>💻 Code Example</summary>

```
"How do you handle modularization and Gradle build times at scale?
 Do you use convention plugins or manual configurations?"

"What's your current offline-first strategy? Do you handle sync
 conflicts, or do you rebuild from server on reconnect?"

"What's the biggest performance bottleneck on Android right now?
 Startup, rendering, or network? How do you measure it?"

"How do you test critical paths? Unit tests + integration tests +
 UI tests? Manual QA? Flakiness strategy?"
```

</details>

**Strong Cultural Reverse Questions:**

<details>
<summary>💻 Code Example</summary>

```
"What does success look like in the first 3 months?"

"What's the biggest technical challenge the team faces right now?"

"How does the team approach on-call? Is there a rotation? What's
 the escalation process?"

"How do you balance shipping fast with maintaining code quality?
 Any horror stories from moving too fast?"
```

</details>

**Red Flags (Don't Ask):**
- ❌ "What's the salary?" (save for recruiter or offer stage)
- ❌ "How many vacation days?" (not the time)
- ❌ "Will I work from home?" (OK to ask, but frame professionally)
- ❌ "Do you have ping-pong tables?" (signals you care about perks, not work)

**Strong Closer (Last 2 min):**
<details>
<summary>💻 Code Example</summary>

```
"This sounds like an exciting challenge. The offline-first + sync
 strategy is exactly the kind of problem I want to solve. I'm ready
 to roll up my sleeves and contribute."
```

</details>
Shows enthusiasm + confidence + willingness to work hard.

## 12. Strategic "Reverse" Questions

### For Bolt (Technical)

1. "What's your biggest **performance bottleneck** on Android — startup, rendering, or network? How do you measure it?"
2. "How does your team handle **modularization and build times** — convention plugins, monorepo?"

### For Babbel (Culture/Process)

1. "What's the biggest **challenge and win in KMP adoption** — how much logic do you share today?"
2. "How do Android and iOS teams **collaborate on shared KMP modules** — shared ownership or platform maintainers?"

---

