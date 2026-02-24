[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 31. Instrumentation Tests & UI Testing

### Compose UI Testing

> [!TIP]
> **Use `composeRule.setContent {}` to render UI, `.onNodeWithText()` to find nodes, `.performClick()` for
> interactions, `.assertIsDisplayed()` for assertions.**

composeRule · Semantics tree queries · Scroll actions · Assertions

<details>
<summary>💻 Code Example</summary>

```kotlin
@RunWith(AndroidJUnit4::class)
class MyScreenTest {
    @get:Rule val composeRule = createComposeRule()

    @Test
    fun testButtonClick() {
        composeRule.setContent {
            var count by remember { mutableIntStateOf(0) }
            Column {
                Text("Count: $count")
                Button(onClick = { count++ }) { Text("Click me") }
            }
        }
        composeRule.onNodeWithText("Click me").performClick()
        composeRule.onNodeWithText("Count: 1").assertIsDisplayed()
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Compose Test API

**composeRule.setContent():** Renders composable in test environment, not emulator activity. No Android context overhead (unit-like speed).

**onNodeWithText():** Queries semantics tree (not visual). Finds nodes by contentDescription, text, or test tags.

**performClick():** Sends click event to semantics node. Triggers recomposition if state changes.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Find nodes by text" | Searches semantics tree, not visual hierarchy. Text nodes tagged in semantics during composition. |
| "performClick triggers recomposition" | Click event posted → state update → recomposition → new tree. Test continues (no Thread.sleep needed). |
| "No activity context needed" | ComposeTestRule creates synthetic test context. Avoids full activity startup (faster than Espresso). |

</details>

### Espresso for Legacy Views

> [!TIP]
> Use `ActivityScenarioRule` to launch activity. `onView(withId())` to find views. `perform(click())` for
> actions. `check(matches())` for assertions.

ActivityScenarioRule · View matchers · ViewActions · Idling

<details>
<summary>💻 Code Example</summary>

```kotlin
@RunWith(AndroidJUnit4::class)
class ActivityTest {
    @get:Rule val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun testButtonClick() {
        onView(withId(R.id.button)).perform(click())
        onView(withText("Success")).check(matches(isDisplayed()))
    }

    @Test
    fun testRecyclerView() {
        onView(withId(R.id.recycler)).perform(
            RecyclerViewActions.scrollToPosition<UserViewHolder>(20)
        )
        onView(withText("User 20")).check(matches(isDisplayed()))
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Espresso Idling & Synchronization

**Espresso waits for app idle** before performing actions (waits for background tasks, animations).

**Custom IdlingResource:** If Espresso can't detect idleness (custom thread pool), register IdlingResource.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Espresso waits for idle" | Espresso checks for background tasks/animations. If idle, proceeds. If not, retries for ~5s before failing. |
| "withId/withText are matchers" | Matchers are predicates. onView finds first matching view in hierarchy. Multiple matches = ambiguous, fails. |
| "RecyclerViewActions scrolls to position" | Scrolls RecyclerView until item at position visible (or throws exception). Different from manual scroll. |

</details>

---

