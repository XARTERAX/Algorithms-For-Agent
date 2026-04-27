---
title: "A* Pathfinding on Grid"
id: 0001
source: "classic"
difficulty: "Medium"
topics: ["agent", "pathfinding", "heuristic-search"]
languages: ["python"]
time_complexity: "O((V + E) log V)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` = passable cell and `1` = blocked cell, find the
shortest path from `start` to `goal` using the **A\*** algorithm with the
Manhattan distance heuristic.

**Input:**
- `grid`: `list[list[int]]` — rows × cols, values 0 or 1.
- `start`: `(row, col)` — starting cell (must be passable).
- `goal`: `(row, col)` — target cell (must be passable).

**Output:** List of `(row, col)` tuples from `start` to `goal` (inclusive),
or `None` if no path exists.

# Examples

**Example 1 — open grid:**
```
grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
start = (0, 0), goal = (2, 2)
Output: [(0,0),(1,0),(2,0),(2,1),(2,2)]  # or equivalent shortest path
```

**Example 2 — blocked (no path):**
```
grid = [[0, 1],
        [1, 0]]
start = (0, 0), goal = (1, 1)
Output: None
```

# Brute Force

Enumerate all paths with DFS — exponential O(4^(rows*cols)) in the worst case.
Correct but impractical for any grid larger than ~3×3.

# Optimized Idea

1. **Model** — grid as an implicit graph; each passable cell is a node; edges
   connect 4-directional neighbours with cost 1.
2. **Bottleneck** — BFS explores equally in all directions; A\* uses a heuristic
   to prioritise cells closer to the goal.
3. **Pattern** — A\* with a min-heap (priority queue) on `f = g + h` where
   `g` = cost so far, `h` = Manhattan distance to goal.
4. **Invariant** — when a cell is popped from the heap its `g` cost is optimal
   (admissible heuristic guarantees this).
5. **Complexity** — O((V + E) log V) where V = passable cells, E = 4V edges.

# Pseudocode

```
open_set = min-heap with (f=h(start,goal), g=0, start, path=[start])
visited  = set()

while open_set not empty:
    f, g, current, path = heappop(open_set)
    if current in visited: continue
    visited.add(current)
    if current == goal: return path
    for neighbour in 4-neighbours(current):
        if passable and not visited:
            g2 = g + 1
            h  = manhattan(neighbour, goal)
            heappush(open_set, (g2+h, g2, neighbour, path+[neighbour]))

return None  # no path
```

# Implementation

```python
# See implementations/python/0001_a_star.py
```

# Tests

```python
# See tests/test_0001_a_star.py
```

# Notes

> **Key idea:** A\* extends Dijkstra with an admissible heuristic (Manhattan
> distance) that guides the search toward the goal, drastically reducing
> explored nodes in practice.  
> **Complexity:** Time O((V+E) log V), Space O(V).  
> **Next improvements:** use a closed-list dict to store `g` costs and avoid
> re-inserting duplicates; support diagonal movement; try euclidean heuristic.
