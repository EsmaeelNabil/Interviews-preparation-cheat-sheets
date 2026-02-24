# Plan: Visual Scanning Overhaul for Android Interview Cheat Sheet

**Status:** ⏳ PENDING — Ready to implement
**Created:** February 24, 2026
**Render target:** GitHub / GitLab
**Goal:** All code fully collapsed (click to see). Cleanest scan. Maximum signal-to-noise.

---

## Context

The cheat sheet is 10,425 lines across 44 sections. After Phase 3 restructuring, every
subsection has a TL;DR + chips line + inline code example + a collapsed `<details>` deep dive.

**The problem:** When scanning quickly, inline code blocks interrupt the reading flow.
Even with TL;DR at the top, the eye still "trips" on 5-15 line code blocks sitting between
concepts. For pre-interview skimming, code is noise — you want facts, not syntax.

---

## 3 Structural Improvements

### Improvement 1: Master Quick-Scan Table at Top of File (Highest ROI)

Insert a single `<details open>` block immediately after the file intro (before `## 1.`)
containing a compact table of all 44 sections with their TL;DR in one line each.
Gives "scan all 44 in 90 seconds" capability on first open.

```markdown
<details open>
<summary>⚡ Quick Scan — All 44 Topics (click to collapse)</summary>

| # | Topic | TL;DR |
|---|---|---|
| 2 | Kotlin Language | Data classes = auto-generated equals/hashCode/copy/toString... |
...
| 44 | Pre-Interview Prep | 5 questions always asked: architecture, ANR, leaks, testing, offline |

</details>
```

`<details open>` = visible on first GitHub load, user can collapse it to reach content.

---

### Improvement 2: TL;DR → Blockquote (Visual Hierarchy)

Change every `**TL;DR:** text` to:

```markdown
> **TL;DR:** text
```

GitHub renders `>` with a left border — visually heavier than body text.
Eye lands on TL;DR first, skips past everything else.
**107 occurrences** to update. Risk: zero. Purely additive.

---

### Improvement 3: All Tier-1 Code Blocks → Collapsed `<details>`

Every fenced code block currently visible in Tier 1 (outside any `<details>`) gets wrapped:

**Before (current):**
```markdown
> **TL;DR:** Coroutines suspend, threads block.

`suspends` · `releases thread` · `state machine`

```kotlin
viewModelScope.launch(Dispatchers.IO) { ... }
```

<details>
<summary>🔩 Under the Hood</summary>
...
</details>
```

**After (target):**
```markdown
> **TL;DR:** Coroutines suspend, threads block.

`suspends` · `releases thread` · `state machine`

<details>
<summary>💻 Code Example</summary>

```kotlin
viewModelScope.launch(Dispatchers.IO) { ... }
```

</details>

<details>
<summary>🔩 Under the Hood</summary>
...
</details>
```

---

## Final Per-Subsection Template (Target State)

```markdown
### [Subsection Name]

> **TL;DR:** [One sentence. What it is + when to use it.]

`chip` · `chip` · `chip` · `chip`

| Quick table (optional, max 5 rows) |

<details>
<summary>💻 Code Example</summary>

```kotlin
// Full code, any length
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### How it works internally
[Compiler output, runtime mechanics]

### User vs Understander
| A user knows | An understander also knows |
|---|---|
| Surface fact | Deep mechanism |

### Gotchas
- Edge case 1
- Edge case 2

</details>
```

**Key contract:**
- Always visible: TL;DR (blockquoted) + chips + optional table = ≤8 lines
- One click `💻`: Full code (any length)
- One click `🔩`: Deep internals + User vs Understander table + gotchas

---

## Scope Analysis

| Area | Current State | Change |
|---|---|---|
| TL;DR lines (107) | `**TL;DR:**` plain bold | `> **TL;DR:**` blockquote |
| Tier-1 code blocks (~90) | Visible inline | Wrap in `<details><summary>💻 Code Example</summary>` |
| `<details>` deep dives (83) | Already collapsed | **No change** |
| Master scan table | Doesn't exist | Create from all 44 TL;DRs |
| Sections 1, 9 (flat) | No structure | Out of scope — Phase 4 |
| Sections 36-44 (no deep dive) | TL;DR + chips only | Out of scope — separate task |

---

## Implementation Order

### Step 1 — Build Master Scan Table

- Insertion point: just before `## 1. Data Structures` (find with grep)
- Extract best TL;DR from each of the 44 sections
- Columns: `# | Topic | TL;DR` (≤15 words per TL;DR)
- Wrap in `<details open>...</details>`

### Step 2 — Promote TL;DR to Blockquotes

- Find: lines matching `^\*\*TL;DR:\*\*`
- Replace: `> **TL;DR:**`
- 107 occurrences, zero risk

### Step 3 — Wrap Tier-1 Code Blocks

**Batch A first (Sections 18-44):** Shorter code blocks (4-8 lines), faster wins. ~60 blocks.
**Batch B second (Sections 2-17):** Larger inline code examples, more care needed. ~30 blocks.

**Rules:**
1. Only wrap fenced code blocks (` ```kotlin ``` `) outside existing `<details>` blocks
2. 1 code block per subsection → `💻 Code Example`
3. 2+ code blocks per subsection → combine in one `<details>` or use `💻 Code Examples`
4. Never touch code already inside `<details>` blocks
5. Inline backtick code (`` `val x = 1` ``) stays inline — don't wrap

### Step 4 — Verify

- [ ] 44-row scan table renders correctly on GitHub
- [ ] Blockquote TL;DRs show left border on GitHub
- [ ] `💻 Code Example` expands correctly on click
- [ ] No double-wrapped code (code inside details inside details)
- [ ] Tier 1 visible content ≤8 lines per subsection when all collapsed

---

## Out of Scope (Separate Tasks)

- Adding `<details>` deep dives to Sections 36-44 (content work, not scanning)
- Restructuring Sections 1 and 9 (completely flat, Phase 4 cleanup)
- Fixing duplicate section numbering (12, 13 duplicates)
- Moving version reference to appendix

---

## Key File

`/Users/esmaeelnabil/Pdev/android/preparation_android_tech_android.md`
