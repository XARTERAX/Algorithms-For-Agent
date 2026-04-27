---
title: "Priority Queue"
id: 0004
source: "data structures"
difficulty: "Easy"
topics: ["data-structure", "heap", "agent"]
languages: ["python"]
time_complexity: "O(log n) push/pop"
space_complexity: "O(n)"
date: 2026-04-27
---

# Problem

Implement a **min-priority queue** supporting:
- `push(item, priority)` — insert item with given priority.
- `pop()` — remove and return the item with the **lowest** priority value.
- `peek()` — return the lowest-priority item without removing it.
- `is_empty()` — return `True` if the queue is empty.

Used in A\* and Dijkstra as the open-set data structure.

# Examples

```
pq = PriorityQueue()
pq.push("node_B", 3)
pq.push("node_A", 1)
pq.push("node_C", 2)

pq.pop()   → "node_A"   (priority 1)
pq.pop()   → "node_C"   (priority 2)
pq.pop()   → "node_B"   (priority 3)

pq.is_empty() → True
```

# Brute Force

Store items in a list; scan the whole list to find the minimum — O(n) per pop.

# Optimized Idea (思路链)

1. **Model** — wrap Python's `heapq` module (min-heap).
2. **Pattern** — heap maintains the invariant: parent priority ≤ children.
3. **Invariant** — `heap[0]` is always the minimum-priority element.
4. **Tie-breaking** — use a counter to break ties and avoid comparing items.

# Implementation

See `implementations/python/0004_priority_queue.py`.

# Tests

- Push multiple items; verify pop order matches priority.
- Peek does not remove the item.
- Push after pop.
- is_empty on fresh and used queue.

# Review (fill in after solving)

- **Key idea**: Binary min-heap gives O(log n) push/pop vs O(n) for naïve list scan.
- **Complexity**: time O(log n) per operation | space O(n)
- **Improvement**: Use a Fibonacci heap for O(1) amortized push and O(log n) pop (complex to implement).
