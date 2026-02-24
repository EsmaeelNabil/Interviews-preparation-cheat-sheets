[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 1. Data Structures & Big O (The "Under the Hood" Section)

### ArrayList vs. LinkedList

|Feature|ArrayList|LinkedList|
|---|---|---|
|**Backing**|Dynamic array|Doubly-linked nodes|
|**Access**|O(1) random access|O(n) traversal|
|**Insert (end)**|O(1) amortized|O(1)|
|**Insert (middle)**|O(n) shift elements|O(1) if at node, O(n) to find|
|**Memory**|Contiguous, cache-friendly|Per-node overhead, scattered|
|**When to use**|95% of cases. Read-heavy, index-based|Frequent insert/remove at head/middle with iterator|

**ArrayList resize:** When capacity is exceeded, it allocates a **new array ~1.5x** the current size and copies all elements — amortized O(1) but worst-case O(n) for that single insertion. **Why 1.5x?** Sweet spot: reduces reallocation frequency (exponential growth) vs. memory waste. Cost is spread: one O(n) spike per ~log(n) insertions.

**Memory reality:** LinkedList has **24-40 bytes per node** overhead (object header + next/prev refs). For 1000 integers: ArrayList ≈ 4KB; LinkedList ≈ 40KB. Cache efficiency: ArrayList accesses contiguous memory (L1 cache hit); LinkedList scatters (L3 cache miss). **Practical impact:** ArrayList often faster even for inserts due to modern CPU speeds.

### HashMap Internals (Deep Dive)

**Buckets & Hashing:** A HashMap is an array of "buckets"; the bucket index is `key.hashCode() & (capacity - 1)` (bitwise AND, equivalent to modulo for power-of-2 sizes). Capacity is **always a power of 2** (1, 2, 4, 8...) for this trick to work.

**Collisions & Treeification:** When two keys hash to the same bucket, they form a **linked list**. In Java 8+/Kotlin JVM, when a bucket exceeds **8 entries**, it converts to a **red-black tree**. Why 8? A threshold study found it balances: linked list overhead for small counts vs. tree rebalancing overhead. Nodes store `hash`, `key`, `value`, `next` (~40 bytes).

**Load Factor & Resize:** Default load factor = **0.75**. Triggers resize at 75% capacity (e.g., 12 entries in 16-bucket map). Why 0.75? Empirical trade-off: <0.75 = wasted space; >0.75 = higher collision rate. Resize: capacity **doubles** (e.g., 16 → 32), all entries **rehashed** (O(n)). Worst case: many adds push load beyond 0.75 repeatedly.

**Complexity Guarantees:**
- **Average O(1):** Assumes good hash distribution. Most keys in different buckets.
- **Worst O(n):** Bad hashing (many keys → same bucket) or deliberate collision attack (DoS). After treeification, degrades to **O(log n)** instead.
- **String hashing:** Java caches `.hashCode()` after first call. Custom objects: override `hashCode()` and `equals()` together, always.

### Big O Quick-Table

|Operation|Array|HashMap|LinkedList|
|---|---|---|---|
|**Access**|O(1)|O(1) avg|O(n)|
|**Search**|O(n)|O(1) avg|O(n)|
|**Insert**|O(n)|O(1) avg|O(1) at head|
|**Delete**|O(n)|O(1) avg|O(1) at node|

---

