[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 38. App Shortcuts & Widgets

### App Shortcuts

> **TL;DR:** Define in `shortcuts.xml` with shortcutId, icon, labels. Register in manifest via `<meta-data>`. Launcher shows long-press menu with quick actions.

Launcher shortcuts · Intent-based · Quick actions

<details>
<summary>💻 Code Example</summary>

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <shortcut android:shortcutId="compose" android:icon="@drawable/ic_compose">
        <intent android:action="android.intent.action.MAIN" android:targetClass="com.example.ComposeActivity" />
    </shortcut>
</shortcuts>
```

</details>

### Home Screen Widgets

> **TL;DR:** Extend `AppWidgetProvider`, override `onUpdate()`, use `RemoteViews` to build UI. Register receiver in manifest with `APPWIDGET_UPDATE` action.

RemoteViews · AppWidgetProvider · Limited widgets · Home screen

<details>
<summary>💻 Code Example</summary>

```kotlin
class MyWidgetProvider : AppWidgetProvider() {
    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {
        appWidgetIds.forEach { id -> updateAppWidget(context, appWidgetManager, id) }
    }
    private fun updateAppWidget(context: Context, mgr: AppWidgetManager, widgetId: Int) {
        val views = RemoteViews(context.packageName, R.layout.widget_layout)
        views.setTextViewText(R.id.text, "Hello!")
        val intent = Intent(context, MainActivity::class.java)
        val pi = PendingIntent.getActivity(context, 0, intent, PendingIntent.FLAG_IMMUTABLE)
        views.setOnClickPendingIntent(R.id.button, pi)
        mgr.updateAppWidget(widgetId, views)
    }
}
```

</details>

---

