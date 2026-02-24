[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 40. Testing Strategies by Scenario

### ViewModel + Fake Repository

> **TL;DR:** Inject FakeRepository into ViewModel. Use `runTest` + `advanceUntilIdle()` for coroutines. Assert state transitions.

Unit tests · Fake dependencies · State assertions · runTest for coroutines

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun loadUser_success() = runTest {
    val fakeRepo = FakeUserRepository()
    val vm = UserViewModel(fakeRepo)
    vm.load(); advanceUntilIdle()
    assertIs<UiState.Success>(vm.state.value)
}
```

</details>

### Compose UI Testing

> **TL;DR:** Use `createComposeRule()`. `setContent {}` to render. Find nodes by text/tag, perform actions, assert visibility.

composeRule · Semantics tree · Assertions · No Android context needed

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun searchWorks() {
    composeRule.setContent { SearchScreen() }
    composeRule.onNodeWithTag("search_field").performTextInput("Alice")
    composeRule.onNodeWithText("Results for Alice").assertIsDisplayed()
}
```

</details>

### Navigation Testing

> **TL;DR:** Use `TestNavHostController`. Set up NavHost with test controller. Verify route after navigation clicks.

TestNavHostController · Route verification · Compose navigation

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun navigateToProfile() {
    val navController = TestNavHostController(ApplicationProvider.getApplicationContext())
    composeRule.setContent {
        NavHost(navController, "home") {
            composable("home") { HomeScreen { navController.navigate("profile/123") } }
        }
    }
    composeRule.onNodeWithText("View Profile").performClick()
    assertEquals("profile/123", navController.currentBackStackEntry?.destination?.route)
}
```

</details>

### E2E Integration Testing

> **TL;DR:** Launch activity with `ActivityScenarioRule`. Perform user flows (login → profile → edit). Assert UI state changes.

End-to-end · User flows · Espresso · Full app testing

<details>
<summary>💻 Code Example</summary>

```kotlin
@Test fun loginToProfile() = runBlocking {
    onView(withId(R.id.email_field)).perform(typeText("test@example.com"))
    onView(withId(R.id.login_button)).perform(click())
    onView(withText("Profile")).check(matches(isDisplayed()))
}
```

</details>

---

