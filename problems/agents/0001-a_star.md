---
title: "A* Pathfinding"
id: 0001
source: "custom"
difficulty: "Medium"
topics: ["graph", "heuristic-search", "priority-queue"]
languages: ["python"]
time_complexity: "O(E log V)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a weighted grid (2-D list) where `0` = free and `1` = obstacle, find the **shortest path** from a `start` cell to a `goal` cell.  
Return the path as a list of `(row, col)` tuples, or an empty list if no path exists.

## Examples

| Grid (4×4) | Start | Goal | Path cost |
|------------|-------|------|-----------|
| all zeros  | (0,0) | (3,3) | 6 (Manhattan) |
| wall at row 1 | (0,0) | (3,3) | detoured |

```
Input:
  grid = [[0,0,0,0],
          [0,1,1,0],
          [0,0,0,0],
          [0,0,0,0]]
  start = (0, 0), goal = (3, 3)

Output:
  [(0,0),(1,0),(2,0),(2,1),(2,2),(2,3),(3,3)]   # one valid path
```

## Constraints

- Grid dimensions: 1 ≤ rows, cols ≤ 100
- Moves: 4-directional (up, down, left, right), cost = 1 per step
- `start` and `goal` are always free cells

---

# Brute Force

Run **Dijkstra** with unit weights (= BFS since all edges have equal cost).  
BFS guarantees the shortest path in unweighted graphs, but ignores problem structure.

**Complexity:** O(V + E) = O(rows × cols) time and space.

---

# Optimised Idea (思路链)

1. **Model:** Grid cells are nodes; adjacent free cells share an edge of weight 1.
2. **Brute force:** BFS finds the shortest path but explores in all directions equally.
3. **Bottleneck:** BFS doesn't prioritise cells that are *closer to the goal*.
4. **Pattern:** A\* uses a **priority queue** ordered by `f = g + h` where:
   - `g` = actual cost from start to current cell
   - `h` = heuristic estimate of cost from current cell to goal (Manhattan distance)
5. **Key invariant:** When a node is popped from the priority queue, its `g` value is optimal (assuming h is admissible: never over-estimates).

### Pseudocode

```
open_set = MinHeap()
open_set.push((0 + h(start), 0, start))   # (f, g, node)
came_from = {}
g_score = {start: 0}

while open_set is not empty:
    f, g, current = open_set.pop()
    if current == goal: reconstruct_path and return
    for each neighbour of current:
        tentative_g = g + 1
        if tentative_g < g_score.get(neighbour, ∞):
            g_score[neighbour] = tentative_g
            came_from[neighbour] = current
            open_set.push((tentative_g + h(neighbour), tentative_g, neighbour))

return []   # no path
```

---

# Implementation

```python
# See implementations/python/0001_a_star.py
```

---

# Tests

```python
# See tests/test_0001_a_star.py
```

---

# 3-Line Recap

1. **Key idea:** A\* combines Dijkstra's guaranteed-optimality with a heuristic that guides the search toward the goal, reducing explored nodes.
2. **Complexity:** O(E log V) time with a binary min-heap; O(V) space for g-scores and the open set.
3. **Why correct:** The Manhattan heuristic is admissible (never over-estimates on a grid), so A\* never discards an optimal path.
