---
title: "Priority Queue"
id: 0004
source: "custom"
difficulty: "Easy"
topics: ["data-structures", "heap", "priority-queue"]
languages: ["python"]
time_complexity: "O(log n) push/pop"
space_complexity: "O(n)"
date: 2026-04-27
---

# Problem

Implement a **min-priority queue** supporting:
- `push(item, priority)` — insert item with given priority.
- `pop()` — remove and return the item with the **lowest** priority value.
- `peek()` — return the item with the lowest priority without removing it.
- `__len__()` — return number of items.

## Examples

```
pq = PriorityQueue()
pq.push("B", 5)
pq.push("A", 1)
pq.push("C", 3)
pq.pop()   # → "A"  (priority 1)
pq.pop()   # → "C"  (priority 3)
pq.pop()   # → "B"  (priority 5)
```

## Constraints

- Items may be any hashable object.
- Priorities are comparable numbers.
- On equal priority, any order is acceptable.

---

# Brute Force

Maintain a sorted list: O(n) insertion, O(1) pop.  
Or use an unsorted list: O(1) insertion, O(n) pop.  
Neither is efficient for large n.

---

# Optimised Idea (思路链)

1. **Model:** A *heap* is a complete binary tree maintaining the *heap property* (parent ≤ children for a min-heap).
2. **Key operations:**
   - `push`: append at the end, then **sift up** — O(log n).
   - `pop`: swap root with last element, remove last, then **sift down** — O(log n).
3. **Python:** `heapq` module provides a ready-made binary min-heap on a list.
4. **Tie-breaking:** Use `(priority, counter, item)` tuples so ties are broken by insertion order (counter).

### Pseudocode

```
class PriorityQueue:
    heap = []
    counter = 0

    push(item, priority):
        heappush(heap, (priority, counter, item))
        counter += 1

    pop():
        _, _, item = heappop(heap)
        return item

    peek():
        _, _, item = heap[0]
        return item
```

---

# Implementation

```python
# See implementations/python/0004_priority_queue.py
```

---

# Tests

```python
# See tests/test_0004_priority_queue.py
```

---

# 3-Line Recap

1. **Key idea:** A binary min-heap stores the smallest element at the root and maintains order via O(log n) sift operations.
2. **Complexity:** O(log n) push and pop; O(1) peek; O(n) build.
3. **Why correct:** The heap property guarantees the root is always the global minimum, so `pop` always returns the correct element.
