[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 35. Data Binding & View Binding Best Practices

### ViewBinding (Type-Safe Views)

> [!TIP]
> **Enable `viewBinding true` in build.gradle.** Use generated `Binding` classes instead of `findViewById()`.
> Type-safe, null-safe, no reflection.

Type-safe · Null-safe · Compile-time checking · No reflection

<details>
<summary>💻 Code Example</summary>

```kotlin
android { buildFeatures { viewBinding true } }

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.button.setOnClickListener { binding.text.text = "Clicked!" }
    }
}

class MyFragment : Fragment() {
    private var _binding: FragmentMyBinding? = null
    private val binding get() = _binding!!
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, saved: Bundle?): View {
        _binding = FragmentMyBinding.inflate(inflater, container, false)
        return binding.root
    }
    override fun onDestroyView() { super.onDestroyView(); _binding = null }
}
```

</details>

### Data Binding (Two-Way Binding)

> [!TIP]
> Use `<data>` block in layout XML to bind variables + event handlers. Automatic UI updates when ViewModel data
> changes. Two-way binding with `@={...}`.

Data binding expressions · Event handlers · Two-way binding · Declarative UI

<details>
<summary>💻 Code Example</summary>

```xml
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <variable name="user" type="com.example.User" />
        <variable name="handler" type="com.example.Handler" />
    </data>
    <LinearLayout android:layout_width="match_parent" android:layout_height="match_parent">
        <TextView android:text="@{user.name}" />
        <Button android:onClick="@{handler::onButtonClick}" />
    </LinearLayout>
</layout>
```

</details>

<details>
<summary>💻 Code Example</summary>

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
        binding.user = User("Alice")
        binding.handler = MyClickHandler()
    }
}
```

</details>

---

