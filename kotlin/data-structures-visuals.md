[← Back to data-structures.md](data-structures.md) | [← Back to folder](README.md)

---

# Data Structures — Visual Reference

> Visual companion to `data-structures.md`. Every concept rendered as a diagram.

---

## Performance Matrix

```mermaid
quadrantChart
    title Data Structures: Access Speed vs Insert Speed
    x-axis Slow Access --> Fast Access
    y-axis Slow Insert --> Fast Insert
    HashMap: [0.9, 0.85]
    HashSet: [0.9, 0.83]
    ArrayList: [0.85, 0.2]
    ArrayDeque: [0.75, 0.8]
    TreeMap: [0.6, 0.55]
    LinkedList: [0.1, 0.85]
```

---

## ArrayList vs LinkedList — Memory Layout

```mermaid
flowchart LR
    subgraph ARRAYLIST["ArrayList (contiguous memory)"]
        direction LR
        A0["[0]\n1"]
        A1["[1]\n2"]
        A2["[2]\n3"]
        A3["[3]\n4"]
        A4["[4]\n..."]
        A0 --- A1 --- A2 --- A3 --- A4
    end
    subgraph LINKEDLIST["LinkedList (scattered nodes)"]
        N1["Node\nval=1\nnext=→"]
        N2["Node\nval=2\nprev=←\nnext=→"]
        N3["Node\nval=3\nprev=←\nnext=→"]
        N4["Node\nval=4\nprev=←"]
        N1 --> N2 --> N3 --> N4
        N4 -.->|"prev"| N3 -.->|"prev"| N2 -.->|"prev"| N1
    end
```

### Memory Per Element

```mermaid
xychart-beta
    title "Memory Usage: 1000 Integer Elements"
    x-axis ["ArrayList", "LinkedList"]
    y-axis "Memory (KB)" 0 --> 50
    bar [4, 40]
```

> **ArrayList**: ~4KB (contiguous int array, cache-friendly L1 hits)
> **LinkedList**: ~40KB (24–40 bytes per node: header + value + next + prev refs, L3 cache misses)

---

## ArrayList — Resize Behavior

```mermaid
flowchart TD
    ADD["add(element)"]
    CHECK{"size == capacity?"}
    NORMAL["Store in array[size]\nO(1) ✅"]
    RESIZE["Allocate new array\n× 1.5 capacity\nCopy all elements\nO(n) one-time ⚠️"]
    ADD --> CHECK
    CHECK -->|"No"| NORMAL
    CHECK -->|"Yes"| RESIZE
    RESIZE --> NORMAL
```

### Amortized O(1) — Why It Works

```mermaid
xychart-beta
    title "Insert Cost Over Time (amortized O(1))"
    x-axis [1, 2, 4, 8, 9, 16, 17, 32, 33]
    y-axis "Cost" 0 --> 35
    line [1, 1, 4, 1, 8, 1, 16, 1, 32]
```

> Spikes = resize events (copy old array). Between spikes: constant cost. Average across all inserts = O(1).

---

## HashMap Internals

```mermaid
flowchart TD
    KEY["key = 'Alice'\nhashCode() = 91502"]
    BUCKET["bucket index =\nhashCode() & (capacity - 1)\n= 91502 & 15 = 2"]
    ARRAY["Bucket Array\n[0] → null\n[1] → Entry\n[2] → Entry ← 'Alice' goes here\n[3] → null\n..."]
    KEY --> BUCKET --> ARRAY
```

### Collision Resolution

```mermaid
flowchart TD
    COL["Collision!\n2 keys → same bucket"]
    COUNT{"bucket.size\n≥ 8?"}
    LL["Linked List\n(small buckets)"]
    TREE["Red-Black Tree\n(large buckets)\nO(log n) worst case"]
    COL --> COUNT
    COUNT -->|"< 8"| LL
    COUNT -->|"≥ 8"| TREE
```

### Load Factor & Resize

```mermaid
flowchart LR
    subgraph LOAD_FACTOR["Load Factor = 0.75"]
        LF1["capacity = 16\nthreshold = 12 entries"]
        LF2["At 12 entries:\nresize triggered"]
        LF3["new capacity = 32\nAll entries REHASHED\nO(n) one-time"]
        LF1 --> LF2 --> LF3
    end
    subgraph WHY["Why 0.75?"]
        W1["< 0.75 → wasted space\ntoo many empty buckets"]
        W2["= 0.75 → sweet spot\ngood collision vs memory"]
        W3["> 0.75 → high collisions\nO(n) degradation"]
    end
```

### HashMap Get — Full Path

```mermaid
sequenceDiagram
    participant C as Caller
    participant HM as HashMap
    participant B as Bucket[index]

    C->>HM: get("Alice")
    HM->>HM: hash = "Alice".hashCode()
    HM->>HM: index = hash & (capacity-1)
    HM->>B: check bucket[index]
    alt Bucket empty
        B-->>HM: null
        HM-->>C: null (key not found)
    else Single entry (no collision)
        B-->>HM: entry (hash match + equals match)
        HM-->>C: value ✅
    else Collision — linked list
        B->>B: traverse list, check equals()
        B-->>HM: found or null
        HM-->>C: value or null
    else Treeified (≥8 entries)
        B->>B: tree search O(log n)
        B-->>HM: found or null
        HM-->>C: value or null
    end
```

---

## Big O Quick Reference

```mermaid
flowchart LR
    subgraph TABLE["Big O Comparison"]
        direction TB
        HDR["Structure | Access | Search | Insert | Delete"]
        R1["Array     |  O(1)  |  O(n)  |  O(n)  |  O(n)"]
        R2["ArrayList |  O(1)  |  O(n)  | O(1)am |  O(n)"]
        R3["LinkedList|  O(n)  |  O(n)  |  O(1)* |  O(1)*"]
        R4["HashMap   |  O(1)a |  O(1)a |  O(1)a |  O(1)a"]
        R5["TreeMap   |O(logn) |O(logn) |O(logn) |O(logn)"]
        R6["HashSet   |  O(1)a |  O(1)a |  O(1)a |  O(1)a"]
    end
```

> `a` = amortized, `am` = amortized, `*` = O(1) only if you have a node reference

---

## When to Use Which

```mermaid
flowchart TD
    Q1{Need key-value\nlookup?}
    Q1 -->|Yes| Q2{Sorted order\nneeded?}
    Q1 -->|No| Q3{Unique elements?}

    Q2 -->|Yes| TREEMAP["TreeMap\nO(log n) ops\nNavigable, sorted"]
    Q2 -->|No| HASHMAP["HashMap\nO(1) avg\nFastest lookup"]

    Q3 -->|Yes| Q4{Sorted order?}
    Q3 -->|No| Q5{Index access needed?}

    Q4 -->|Yes| TREESET["TreeSet\nO(log n)\nsorted unique"]
    Q4 -->|No| HASHSET["HashSet\nO(1) avg\nfastest unique"]

    Q5 -->|Yes| Q6{Heavy middle inserts?}
    Q5 -->|No| DEQUE["ArrayDeque\nO(1) head/tail\nqueue/stack"]

    Q6 -->|Yes| LINKED["LinkedList\nO(1) at node\n(rarely needed)"]
    Q6 -->|No| ARRAY["ArrayList\nO(1) access\n95% of cases"]
```

---

## Cache Efficiency — Why ArrayList Beats LinkedList in Practice

```mermaid
flowchart TD
    subgraph CPU_CACHE["CPU Cache Hierarchy"]
        L1["L1 Cache\n~4ns\n~32KB"]
        L2["L2 Cache\n~12ns\n~256KB"]
        L3["L3 Cache\n~40ns\n~8MB"]
        RAM["RAM\n~100ns\nunlimited"]
    end

    subgraph ACCESS_PATTERN["Access Pattern"]
        AL["ArrayList[i]\nContiguous memory\nPrefetcher loads\nnext elements\n→ L1 HIT ✅"]
        LL["LinkedList.get(i)\nScattered memory\nEach node = new\nmemory location\n→ L3 or RAM MISS ❌"]
    end

    L1 --> L2 --> L3 --> RAM
```

---

## Mental Map — Data Structures

```mermaid
mindmap
    root((Data Structures))
        ArrayList
            O(1) access by index
            O(1) amortized insert at end
            1.5x resize on overflow
            contiguous memory, cache-friendly
            95% of use cases
        LinkedList
            O(1) insert at head with reference
            O(n) access by index
            24-40 bytes per node overhead
            scattered memory, cache-unfriendly
            rare: queue/deque needs
        HashMap
            hashCode + & (capacity-1) for bucket
            0.75 load factor default
            linked list → red-black tree at 8
            O(1) avg, O(n) worst (bad hash)
        TreeMap
            Red-black tree internally
            O(log n) all operations
            sorted keys, navigable
            use when order matters
        HashSet
            HashMap with dummy values
            O(1) contains/add
```
