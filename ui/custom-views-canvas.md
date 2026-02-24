[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 27. Custom Views & Canvas Drawing

### Custom View Lifecycle & Drawing

> [!WARNING]
> **Override `onMeasure()` (set size) → `onLayout()` (position) → `onDraw()` (draw).** Pre-allocate Paint in
> member variable—never allocate in onDraw() (garbage = jank).

Measure/layout/draw lifecycle · Canvas API · Paint pooling · invalidate() for redraws

<details>
<summary>💻 Code Example</summary>

```kotlin
class CustomCircleView(context: Context, attrs: AttributeSet?) : View(context, attrs) {
    private var radius = 0f
    private val paint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.BLUE; style = Paint.Style.FILL }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        val size = 200.dp.toPixels().toInt()
        setMeasuredDimension(size, size)
    }

    override fun onLayout(changed: Boolean, left: Int, top: Int, right: Int, bottom: Int) {
        super.onLayout(changed, left, top, right, bottom)
        radius = width / 2f
    }

    override fun onDraw(canvas: Canvas) {
        canvas.drawCircle(width / 2f, height / 2f, radius, paint)
    }

    fun setRadius(r: Float) { radius = r; invalidate() }
}
```

</details>

**Pattern:** Pre-allocate paints/paths in member scope. Never allocate in onDraw().

<details>
<summary>🔩 Under the Hood</summary>

### Measure Spec Decoding

**onMeasure receives MeasureSpec** (parent constraint + child wishes):
```kotlin
val mode = MeasureSpec.getMode(widthMeasureSpec)  // AT_MOST, EXACTLY, UNSPECIFIED
val size = MeasureSpec.getSize(widthMeasureSpec)
```

**Modes:**
- EXACTLY: Parent fixed size (must use)
- AT_MOST: Max size, you can be smaller
- UNSPECIFIED: No constraint (wrap content)

### Canvas Drawing & CPU Cost

**Canvas operations:**
```
drawCircle() → Convert to path → Fill with paint → Rasterize (CPU) → submit to GPU
```

**Every onDraw() call = CPU work.** Allocating Paint = garbage → GC during animation = frame drop.

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "onDraw expensive, call sparingly" | onDraw = CPU-bound. Profiler shows time spent (can be >16ms, causing jank). Hardware Canvas helps but still expensive. |
| "invalidate() triggers onDraw()" | invalidate() requests refresh. Choreographer batches, redraws next vsync (60Hz). Many invalidate() calls batched into one onDraw(). |
| "MeasureSpec encodes mode + size" | MeasureSpec = single int. High 2 bits = mode, low 30 bits = size. Parent encodes expectations; child respects. |

### Gotchas at depth

- **Over-drawing:** Drawing layered objects = O(n) depth. Reorder to reduce overdraw (profile with surface flinger). |
| **HW acceleration disabled:** Some canvas ops not GPU-supported (setShader on certain paths). Framework falls back to CPU (slow). |
| **requestLayout vs. invalidate:** requestLayout triggers measure/layout/draw. invalidate only triggers draw. Different costs.

</details>

---

