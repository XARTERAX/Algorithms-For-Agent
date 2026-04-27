---
title: "Priority Queue"
id: 0004
source: ""
difficulty: "Easy"
topics: ["data-structures", "heap", "priority-queue"]
languages: ["python"]
time_complexity: "O(log n) push/pop, O(1) peek"
space_complexity: "O(n)"
date: 2024-01-01
---

# Problem

Implement a **min-priority queue** that supports:
- `push(item, priority)` — insert an item with a numeric priority.
- `pop()` — remove and return the item with the **lowest** priority value.
- `peek()` — return the item with the lowest priority without removing it.
- `is_empty()` — return `True` if the queue is empty.

## Examples

**Example 1**
```python
pq = MinPriorityQueue()
pq.push("explore (2,3)", priority=5)
pq.push("explore (1,1)", priority=2)
pq.push("explore (3,4)", priority=8)
pq.peek()   # → "explore (1,1)"
pq.pop()    # → "explore (1,1)"
pq.pop()    # → "explore (2,3)"
```

## Constraints

- Priorities are comparable numbers (int or float).
- Items can be any hashable Python object.

# Approach

## Brute Force

A sorted list supports O(1) peek but O(n) push. Acceptable for small queues.

## Optimized Idea

Use Python's `heapq` module (min-heap):
- Heap entries are `(priority, counter, item)`.
- A monotone counter breaks priority ties deterministically and avoids comparing `item` objects.

```
heap = []
counter = 0

push(item, priority):
    heappush(heap, (priority, counter, item))
    counter += 1

pop():
    _, _, item = heappop(heap)
    return item

peek():
    return heap[0][2]
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| push | O(log n) | O(1) |
| pop | O(log n) | O(1) |
| peek | O(1) | O(1) |

# Implementation (Python)

```python
# See implementations/python/0004_priority_queue.py
```

# 3-Line Recap

1. **Key idea**: A binary min-heap keeps the smallest-priority item at the root, enabling O(log n) push/pop.
2. **Why it works**: `heapq` maintains the heap invariant automatically; the tiebreaker counter ensures stability without comparing items.
3. **Pitfalls / edge cases**: Always include a counter (or another comparable field) between priority and item to avoid `TypeError` when two priorities are equal and items are not comparable.
