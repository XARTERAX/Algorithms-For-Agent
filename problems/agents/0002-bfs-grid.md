---
title: "BFS Grid Shortest Path"
id: 0002
source: "classic"
difficulty: "Easy"
topics: ["agent", "pathfinding", "bfs"]
languages: ["python"]
time_complexity: "O(V + E)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` = passable and `1` = blocked, find the shortest
path (fewest steps) from `start` to `goal` using **BFS**.

**Input:**
- `grid`: `list[list[int]]`
- `start`, `goal`: `(row, col)` tuples

**Output:** List of `(row, col)` tuples (inclusive), or `None` if unreachable.

# Examples

**Example 1:**
```
grid = [[0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]]
start = (0, 0), goal = (2, 2)
Output: [(0,0),(0,1),(0,2),(1,2),(2,2)]
```

**Example 2 (no path):**
```
grid = [[0, 1],
        [1, 0]]
start = (0, 0), goal = (1, 1)
Output: None
```

# Brute Force

DFS with backtracking finds a path but not guaranteed shortest — O(4^(V)).

# Optimized Idea

1. **Model** — passable cells as graph nodes; 4-directional unit-cost edges.
2. **Bottleneck** — DFS does not guarantee minimum steps.
3. **Pattern** — BFS processes nodes layer by layer; the first time goal is
   reached the path length is minimal.
4. **Invariant** — all nodes at depth `d` are dequeued before depth `d+1`.
5. **Complexity** — O(V + E) = O(rows × cols).

# Pseudocode

```
queue = deque([(start, [start])])
visited = {start}

while queue:
    current, path = queue.popleft()
    if current == goal: return path
    for neighbour in 4-neighbours(current):
        if passable and not visited:
            visited.add(neighbour)
            queue.append((neighbour, path + [neighbour]))

return None
```

# Implementation

```python
# See implementations/python/0002_bfs_grid.py
```

# Tests

```python
# See tests/test_0002_bfs_grid.py
```

# Notes

> **Key idea:** BFS on an unweighted grid always finds the shortest path first
> because it explores nodes in non-decreasing distance order.  
> **Complexity:** Time O(V+E), Space O(V).  
> **Next improvements:** bidirectional BFS halves the search frontier; for
> weighted grids switch to Dijkstra or A\*.
