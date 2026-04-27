---
title: "A* Search"
id: 0001
source: ""
difficulty: "Medium"
topics: ["graph", "heuristic-search", "pathfinding"]
languages: ["python"]
time_complexity: "O(E log V)"
space_complexity: "O(V)"
date: 2024-01-01
---

# Problem

Given a 2-D grid of cells (0 = passable, 1 = obstacle), a start cell, and a goal cell, find the shortest path from start to goal using the A\* search algorithm.

Return the path as a list of `(row, col)` tuples from start to goal (inclusive), or an empty list if no path exists.

## Examples

**Example 1 — simple path**
- Grid (4×4):
  ```
  0 0 0 0
  0 1 1 0
  0 0 0 0
  0 0 0 0
  ```
- Input: `start=(0,0)`, `goal=(3,3)`
- Output: `[(0,0),(1,0),(2,0),(2,1),(2,2),(2,3),(3,3)]` *(one valid shortest path)*

**Example 2 — no path**
- Grid (2×2):
  ```
  0 1
  1 0
  ```
- Input: `start=(0,0)`, `goal=(1,1)`
- Output: `[]`

## Constraints

- Grid dimensions: 1 ≤ rows, cols ≤ 100
- Only 4-directional movement (up, down, left, right)
- No negative weights

# Approach

## Brute Force

BFS finds the shortest path on unweighted grids but ignores any domain knowledge. A\* improves on BFS by prioritising cells that are already close to the goal.

## Optimized Idea

1. Use a min-heap (priority queue) ordered by `f = g + h`.
   - `g` = cost from start to current cell (number of steps).
   - `h` = heuristic estimate from current cell to goal (Manhattan distance).
2. Expand the cell with the lowest `f` first.
3. When the goal is popped, reconstruct the path via parent pointers.

```
open_set = min-heap {(f, g, node)}
came_from = {}
g_score[start] = 0
push (h(start, goal), 0, start) into open_set

while open_set not empty:
    f, g, current = pop open_set
    if current == goal: reconstruct and return path
    for each neighbour of current:
        tentative_g = g + 1
        if tentative_g < g_score[neighbour]:
            update g_score, came_from
            push (tentative_g + h(neighbour, goal), tentative_g, neighbour)
return []
```

## Complexity Analysis

| | Time | Space |
|---|---|---|
| BFS | O(V + E) | O(V) |
| A\* | O(E log V) | O(V) |

# Implementation (Python)

```python
# See implementations/python/0001_a_star.py
```

# 3-Line Recap

1. **Key idea**: Prioritise nodes by estimated total cost `f = g + h` using a min-heap.
2. **Why it works**: The Manhattan heuristic is admissible (never overestimates), so the first time the goal is expanded the path is guaranteed optimal.
3. **Pitfalls / edge cases**: Tie-break on `g` or a counter to avoid comparing tuples; always check boundary and obstacle conditions before adding neighbours.
