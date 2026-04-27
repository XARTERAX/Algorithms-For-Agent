---
title: "Priority Queue"
id: 0004
source: "classic"
difficulty: "Easy"
topics: ["data-structures", "heap"]
languages: ["python"]
time_complexity: "O(log n) push/pop"
space_complexity: "O(n)"
date: 2026-04-27
---

# Problem

Implement a **stable priority queue** — a min-heap that breaks ties by
insertion order, ensuring FIFO behaviour for equal-priority items.

**Operations:**
- `push(item, priority)` — add item with given priority.
- `pop()` — remove and return the item with the **lowest** priority; ties
  broken by insertion order (FIFO).
- `peek()` — return lowest-priority item without removing it.
- `__len__()` — return number of items.

# Examples

**Example 1:**
```python
pq = PriorityQueue()
pq.push("task_a", 2)
pq.push("task_b", 1)
pq.push("task_c", 1)   # same priority as task_b → FIFO
pq.pop()  # → "task_b"
pq.pop()  # → "task_c"
pq.pop()  # → "task_a"
```

# Brute Force

Maintain a sorted list and re-sort on every push — O(n log n) per push.

# Optimized Idea

1. **Model** — binary min-heap via Python's `heapq`.
2. **Bottleneck** — plain `heapq` is unstable: equal priorities may be returned
   in any order.
3. **Pattern** — add a monotonically-increasing counter as a tie-breaker:
   heap entries are `(priority, counter, item)`.
4. **Invariant** — `(priority, counter)` tuples are always comparable without
   inspecting `item`, so no `__lt__` needed on items.
5. **Complexity** — O(log n) push and pop.

# Pseudocode

```
class PriorityQueue:
    heap    = []
    counter = 0     # tie-breaker

    push(item, priority):
        heappush(heap, (priority, counter, item))
        counter += 1

    pop():
        _, _, item = heappop(heap)
        return item

    peek():
        return heap[0][2]
```

# Implementation

```python
# See implementations/python/0004_priority_queue.py
```

# Tests

```python
# See tests/test_0004_priority_queue.py
```

# Notes

> **Key idea:** Insert a counter alongside priority so that equal-priority items
> are ordered by insertion time, making the heap behave as a stable FIFO queue.  
> **Complexity:** Time O(log n) push/pop, Space O(n).  
> **Next improvements:** support `update_priority`; add a max-heap variant by
> negating priorities.
