---
title: "A* Search"
id: 0001
source: "custom"
difficulty: "Medium"
topics: ["graph", "pathfinding", "heuristic", "heap"]
languages: ["python"]
time_complexity: "O(E log V)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` is passable and `1` is a wall, find the **shortest path** from `start` to `goal` using the A\* search algorithm with the Manhattan distance heuristic.

**Input:**
- `grid`: `List[List[int]]` — rows × cols grid (0 = free, 1 = wall)
- `start`: `(row, col)` — starting cell
- `goal`: `(row, col)` — target cell

**Output:** `List[(row, col)]` — ordered path from start to goal (inclusive), or `None` if no path exists.

# Examples

```
grid = [
  [0, 0, 0],
  [1, 1, 0],
  [0, 0, 0],
]
start = (0, 0), goal = (2, 2)

Output: [(0,0), (0,1), (0,2), (1,2), (2,2)]
```

```
grid = [[1]]
start = (0, 0), goal = (0, 0)

Output: None   # start is a wall
```

# Brute Force

Explore all possible paths via DFS/BFS without a heuristic; return the shortest one found.
- Correctness: BFS on unweighted grids always finds shortest path.
- Time: O(rows × cols) · Space: O(rows × cols)

# Optimized Idea (思路链)

1. **Model** — Grid as an implicit graph; each cell is a node, 4-directional neighbours are edges.
2. **Brute force recap** — BFS finds shortest path but ignores direction to goal.
3. **Pattern** — A\* = Dijkstra + heuristic: prioritise cells that are *close to start* **and** *close to goal*.
4. **Key invariant** — `f(n) = g(n) + h(n)` where g = cost from start, h = admissible heuristic (Manhattan distance). A\* is optimal when h never overestimates.
5. **Pseudocode**

```
open_set ← MinHeap with (f=h(start), g=0, start)
came_from ← {}
g_score[start] = 0

while open_set not empty:
    _, g, current = open_set.pop()
    if current == goal: return reconstruct_path(came_from, goal)
    for each neighbour of current:
        tentative_g = g + 1
        if tentative_g < g_score.get(neighbour, ∞):
            came_from[neighbour] = current
            g_score[neighbour] = tentative_g
            f = tentative_g + manhattan(neighbour, goal)
            open_set.push((f, tentative_g, neighbour))
return None
```

- Time: O(E log V) · Space: O(V)

# Implementation (Python)

```python
# See implementations/python/0001_a_star.py
```

# Tests

| # | Input | Expected Output | Notes |
|---|-------|-----------------|-------|
| 1 | 3×3 grid with wall row | path around wall | happy path |
| 2 | 1×1 wall | None | start is wall |
| 3 | start == goal | [goal] | trivial path |

# Recap (3 lines)

1. **Key idea:** Use a min-heap ordered by f = g + h (Manhattan distance) to always expand the most promising cell first.
2. **Why correct:** Manhattan distance never overestimates the true cost on a grid, so A\* is admissible and returns the optimal path.
3. **Complexity:** Time O(E log V), Space O(V) where V = rows × cols.
