[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 23. Accessibility (a11y) & Localization (i18n)

### Compose Accessibility

> [!IMPORTANT]
> **Use `.semantics { contentDescription = "..." }` for screen readers (TalkBack).** Mark headings with
> `.semantics { heading() }`. Compose auto-handles text scaling & color contrast if using Material semantics.

Semantics tree · contentDescription · TalkBack testing · heading() marker

<details>
<summary>💻 Code Example</summary>

```kotlin
Box(
    Modifier
        .semantics { contentDescription = "User profile card" }
        .clickable { openProfile() }
) {
    Text("Alice", Modifier.semantics { heading() })
    Text("Engineer")
}

// Test: adb shell settings put secure enabled_accessibility_services \
// com.google.android.marvin.talkback/.TalkBackService
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Semantics Tree

**Compose builds tree of semantic nodes parallel to layout tree.**

```
UI Tree:          Semantics Tree:
Box                │
├─ Text("Alice")   ├─ heading() → "Alice"
├─ Text("Eng")     └─ "Engineer"
```

**Screen reader traverses semantics tree**, reads contentDescription for each node.

### contentDescription vs. Text

- **contentDescription:** For non-text UI (icons, images, buttons without text). Screen reader announces once.
- **Text content:** Auto-detected as readable. Don't duplicate in contentDescription.
- **empty contentDescription:** Tells TalkBack to skip (for decorative elements).

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Use contentDescription for icons" | Framework generates accessibility event (TYPE_VIEW_ANNOUNCED) with description. TalkBack processes event. |
| "Semantics tree for screen readers" | Compose tracks semantic properties separately. TalkBack queries AccessibilityDelegate (interface). Returns semantics tree. |
| "Test with TalkBack" | TalkBack is open-source Google service. Reads semantics tree aloud, sends haptics. Works via AccessibilityService (system API). |

### Gotchas at depth

- **Duplicate descriptions:** If you set contentDescription but Text already readable, screen reader announces twice (bad UX).
- **Merged semantics:** Multiple composables can merge into one semantic node. contentDescription applies to entire merged node.
- **Custom modifiers:** Custom Modifiers might break semantics. Always call super.measure(), super.layout() to preserve event delivery.

</details>

### String Resources & Localization (i18n)

> [!TIP]
> Create `res/values-<locale>/strings.xml` for each language (e.g., `values-es`, `values-fr`). Framework
> auto-selects based on device locale. For RTL (Arabic, Hebrew), set `android:supportsRtl="true"`.

Locale-specific resources · values-<locale> · RTL support · Plurals

<details>
<summary>💻 Code Example</summary>

```xml
<!-- res/values/strings.xml (English) -->
<string name="hello">Hello %s</string>
<plurals name="item_count">
    <item quantity="one">%d item</item>
    <item quantity="other">%d items</item>
</plurals>

<!-- res/values-es/strings.xml (Spanish) -->
<string name="hello">Hola %s</string>
<plurals name="item_count">
    <item quantity="one">%d elemento</item>
    <item quantity="other">%d elementos</item>
</plurals>

<!-- AndroidManifest.xml -->
<application android:supportsRtl="true" />
```

</details>

**RTL in Compose:**
<details>
<summary>💻 Code Example</summary>

```kotlin
// Auto-flips for RTL (start = left in LTR, right in RTL)
Text("Hello", Modifier.padding(start = 8.dp))
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### Resource Selection

**Framework algorithm:**
```
Get device locale (e.g., "es-ES") → Find matching strings.xml
├─ res/values-es-rES/ (exact match)
├─ res/values-es/ (language match)
├─ res/values/ (default fallback)
```

**Resolution order:** Exact locale → language → default.

### Plurals Handling

```kotlin
// Framework selects plural based on count
val count = 5
val text = resources.getQuantityString(R.plurals.item_count, count, count)
// Selects "other" form, substitutes %d with 5
// Returns: "5 items"
```

**Plural categories vary by language:**
- English: one, other
- Polish: one, few, many, other
- Arabic: zero, one, two, few, many, other

### RTL Layout

**start/end vs. left/right:**
- LTR: start = left, end = right
- RTL: start = right, end = left

**Compose auto-handles:** Use `start`, `end`, avoid `left`, `right`.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Create values-<locale> folder" | ResourceManager queries system locale (via Locale.getDefault()). Finds closest match in APK resources. |
| "RTL auto-flips" | Compose LayoutDirection set by framework from Locale.getDefault().isRTL(). Modifiers check LayoutDirection and reverse start/end. |
| "Plurals vary by language" | ICU library provides plural rules. Framework matches count to plural category. Non-English languages have different categories. |

### Gotchas at depth

- **String quantization:** Using %d in plurals is common, but some languages need formatting (e.g., Arabic uses suffix, not prefix). Use locale-aware NumberFormat.
- **Mixed LTR/RTL:** App with both LTR and RTL content = bidirectional text. Use Unicode direction markers (LRM, RLM) if needed.
- **String length in different languages:** German translations often longer than English. Layouts must flex (can't hardcode widths). Use Text reflow, not clipping.

</details>

---

