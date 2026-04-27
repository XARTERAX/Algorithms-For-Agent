---
title: "BFS on Grid"
id: 0002
source: "custom"
difficulty: "Easy"
topics: ["graph", "BFS", "grid"]
languages: ["python"]
time_complexity: "O(rows × cols)"
space_complexity: "O(rows × cols)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` = free and `1` = obstacle, find the **minimum number of steps** to travel from `start` to `goal` using 4-directional moves.  
Return the step count, or `-1` if no path exists.

## Examples

```
Input:
  grid = [[0,0,0],
          [0,1,0],
          [0,0,0]]
  start = (0, 0), goal = (2, 2)

Output: 4
```

```
Input:
  grid = [[0,1],
          [1,0]]
  start = (0, 0), goal = (1, 1)

Output: -1   # blocked
```

## Constraints

- 1 ≤ rows, cols ≤ 200
- `start` and `goal` are free cells

---

# Brute Force

Enumerate all paths using DFS and return the shortest — O(4^(rows×cols)) in the worst case, clearly impractical.

---

# Optimised Idea (思路链)

1. **Model:** Grid cells = nodes; adjacent free cells = edges (weight 1).
2. **Key property:** All edge weights are equal ⟹ BFS discovers nodes in non-decreasing distance order.
3. **Pattern:** BFS level-by-level exploration guarantees the first time we reach `goal` is via the shortest path.
4. **Invariant:** Every node in the queue at level `d` is exactly `d` steps from `start`.

### Pseudocode

```
queue = deque([(start, 0)])
visited = {start}

while queue:
    (r, c), dist = queue.popleft()
    if (r, c) == goal: return dist
    for each neighbour (nr, nc) of (r, c):
        if in_bounds and not obstacle and not visited:
            visited.add((nr, nc))
            queue.append(((nr, nc), dist + 1))

return -1
```

---

# Implementation

```python
# See implementations/python/0002_bfs_grid.py
```

---

# Tests

```python
# See tests/test_0002_bfs_grid.py
```

---

# 3-Line Recap

1. **Key idea:** BFS explores cells level by level; the first time the goal is dequeued, the distance is provably minimal.
2. **Complexity:** O(rows × cols) time and space — every cell is visited at most once.
3. **Why correct:** Because all edges have equal weight, BFS is equivalent to Dijkstra with unit costs and finds the shortest path.
