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

Implement a **min-priority queue** that supports:
- `push(item, priority)` — insert item with given priority.
- `pop()` — remove and return the item with the lowest priority value.
- `peek()` — return the item with lowest priority without removing.
- `is_empty()` — return True if the queue is empty.

This data structure is the backbone of A\* and Dijkstra.

**Input/Output:** See test cases below.

# Examples

```python
pq = MinPriorityQueue()
pq.push("A", 3)
pq.push("B", 1)
pq.push("C", 2)
pq.pop()   # → "B"  (priority 1)
pq.peek()  # → "C"  (priority 2, not removed)
```

# Brute Force

Store items in an unsorted list; scan all items on every pop — O(n) per pop.

# Optimized Idea (思路链)

1. **Model** — Binary min-heap: parent ≤ children, so root is always the minimum.
2. **Brute force recap** — Linear scan is too slow for Dijkstra/A\* with large graphs.
3. **Pattern** — Heap: push is O(log n) (sift up), pop is O(log n) (sift down).
4. **Key invariant** — Heap property: `heap[i] ≤ heap[2i+1]` and `heap[i] ≤ heap[2i+2]`.
5. **Pseudocode**

```
push(item, priority):
    heapq.heappush(heap, (priority, counter, item))
    counter++

pop():
    priority, _, item = heapq.heappop(heap)
    return item
```

Python's `heapq` module provides a min-heap; we use a tie-breaking counter to handle equal priorities.

- Time: O(log n) push/pop · Space: O(n)

# Implementation (Python)

```python
# See implementations/python/0004_priority_queue.py
```

# Tests

| # | Input | Expected Output | Notes |
|---|-------|-----------------|-------|
| 1 | Push A(3), B(1), C(2); pop twice | B then C | ordering |
| 2 | pop from empty | raises IndexError | edge case |
| 3 | Equal priorities | FIFO order maintained | tie-break |

# Recap (3 lines)

1. **Key idea:** Wrap Python's `heapq` with a tuple `(priority, counter, item)` to get a stable min-priority queue.
2. **Why correct:** The heap property guarantees the minimum priority is always at the root.
3. **Complexity:** Push and pop are O(log n); peek is O(1).
