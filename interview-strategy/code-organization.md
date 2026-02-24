[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 25. Code Organization & Architecture

### Module Structure (Large Teams)

> **TL;DR:** Split app into **feature modules** (auth, home) + **core modules** (network, database, ui). Dependency flow: `feature` → `core`, never `feature` → `feature`. Use DI to decouple.

Multi-module structure · Dependency graph · Core shared layers · Feature isolation

<details>
<summary>💻 Code Example</summary>

```
app/
├── feature-auth/     ─→ domain/, data/, ui/, di/
├── feature-home/     ─→ domain/, data/, ui/, di/
├── core-network/     ← shared by features
├── core-database/    ← shared by features
└── core-ui/          ← shared by features
```

</details>

**Dependency rule:** ✅ `feature` imports `core` | ❌ `feature` imports `feature` (break cycle via DI interfaces/events).

| Structure | Benefit | Cost |
|---|---|---|
| Monolithic (1 module) | Simple, fast builds | Circular deps, hard to test |
| Multi-feature | Isolates concerns, parallel build | Build complexity, more coordination |
| Over-modularized (30+ modules) | Maximum isolation | Gradle overhead, hard to navigate |

<details>
<summary>🔩 Under the Hood</summary>

### Gradle Dependency Resolution

**When you import a module:**
```gradle
dependencies {
    implementation(project(":feature-auth"))
}
```

**Gradle resolves to**:
- feature-auth's build.gradle dependencies
- Transitively includes all its imports (core-* modules)
- If circular (auth imports home), build fails

**Build cache:** Gradle caches compiled modules. Only rebuild if source changes.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Modularize to avoid circular deps" | Circular deps break class loader. Gradle detects, fails build. Forces architectural discipline. |
| "DI to decouple features" | DI container (Hilt) lives in app module. Features define interfaces in core-* modules. App wires implementations. |
| "core-* modules never import feature-*" | Prevents tight coupling. core-network usable in any feature without knowing about auth/home. Testable in isolation. |

### Gotchas at depth

- **Transitive dependencies:** Importing :feature-auth pulls all its deps (including Retrofit, Room, etc.). Can bloat app size if not careful.
- **Lint/R class clashes:** Multiple modules defining custom views = R class conflicts. Use namespace in build.gradle.
- **Test fixtures:** Sharing test data across modules is hard. Either duplicate or create test-shared modules (expensive).

</details>

### Documentation Patterns

> **TL;DR:** Write ADR (Architecture Decision Records) for major choices. Add KDoc with `@param`, `@throws`, `@return` for public APIs. Include examples in docstrings.

KDoc · ADR · Examples · Consequences

**Architecture Decision Record:**
<details>
<summary>💻 Code Example</summary>

```markdown
# ADR-001: Use MVI instead of MVVM

## Context
State complexity growing; multiple StateFlow sources = inconsistent UI.

## Decision
Adopt MVI (Model-View-Intent) with single reducer + StateFlow.

## Consequences
✅ Single source of truth (state history)
✅ Pure reducer (testable)
❌ More boilerplate (Intent sealed class)

## Alternatives Considered
- MVVM with multiple LiveData (rejected: hard to coordinate)
- MVP (rejected: no ViewModel lifecycle)
```

</details>

**KDoc for Public APIs:**
<details>
<summary>💻 Code Example</summary>

```kotlin
/**
 * Fetches user with automatic caching and retry.
 *
 * @param userId ID to fetch
 * @return User (cached for 1 hour)
 * @throws NotFoundException if user not found
 * @throws IOException if 3 retries exhausted
 *
 * Example: `val user = getUser(123)`
 */
suspend fun getUser(userId: Int): User
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### KDoc & IDE Support

**IDE generates docs from KDoc** when hovering over function. Parameters, return type, exceptions shown.

**Tooling:** dokka generates HTML documentation from KDoc. Used to generate library docs (like Kotlin std lib docs).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Write KDoc for public APIs" | IDE parses KDoc comments. Generates popup on hover. Extracted by dokka to HTML/PDF. |
| "Include examples in docstrings" | Examples help developers understand intent. Also used for generating tutorials/cookbooks. |
| "ADR documents decisions" | ADRs live in version control. Future devs read history to understand why (vs. what). Prevents rework. |

### Gotchas at depth

- **Stale docs:** KDoc not auto-updated when API changes. Easy to document wrong behavior. Enforce doc updates in code review.
- **Over-documenting:** Documenting obvious APIs (getText()) wastes effort. Document why, not what.
- **ADR tooling:** No standard format. Teams define their own. Can become decision graveyard if not enforced.

</details>

---

