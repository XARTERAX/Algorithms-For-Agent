---
title: "A* Pathfinding"
id: 0001
source: "classic AI"
difficulty: "Medium"
topics: ["graph", "heuristic-search", "agent"]
languages: ["python"]
time_complexity: "O(E log V)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` is passable and `1` is a wall, find the shortest path (by step count) from `start` to `goal` using the A\* algorithm with Manhattan distance heuristic.

Return the path as a list of `(row, col)` tuples from start to goal, or `[]` if no path exists.

# Examples

```
Grid (0=open, 1=wall):
  0 0 0
  1 1 0
  0 0 0

Input:  start=(0,0), goal=(2,2)
Output: [(0,0),(0,1),(0,2),(1,2),(2,2)]

Input:  start=(0,0), goal=(2,0)  # blocked by walls
Output: []
```

# Brute Force

BFS explores all reachable cells level by level — guaranteed shortest path on an unweighted grid, but expands far more nodes than necessary because it has no directional preference.
- Time: O(V + E) where V = rows × cols, E ≈ 4V for a 4-connected grid.

# Optimized Idea (思路链)

1. **Model** — grid as an implicit graph; each cell is a node, edges connect 4-adjacent passable neighbours.
2. **Brute force** — BFS (uniform cost, ignores direction to goal).
3. **Bottleneck** — BFS expands in all directions equally; we can guide it toward the goal.
4. **Pattern** — A\*: keep a min-heap ordered by `f = g + h` where `g` = cost from start, `h` = Manhattan distance to goal.
5. **Invariant** — when a node is popped from the heap its `g` value is optimal (admissible heuristic, no negative edges).
6. **Pseudocode**:

```
open_heap = [(f(start), start)]
g = {start: 0}
parent = {}
while open_heap:
    _, current = heappop(open_heap)
    if current == goal: return reconstruct(parent, goal)
    for neighbour in passable_neighbours(current):
        tentative_g = g[current] + 1
        if tentative_g < g.get(neighbour, inf):
            g[neighbour] = tentative_g
            parent[neighbour] = current
            heappush(open_heap, (tentative_g + h(neighbour), neighbour))
return []
```

# Implementation

See `implementations/python/0001_a_star.py`.

# Tests

- Straight path with no obstacles.
- Path forced around walls.
- No path exists (goal completely blocked).
- Start equals goal.

# Review (fill in after solving)

- **Key idea**: Guide BFS with a heuristic to reduce node expansions.
- **Complexity**: time O(E log V) | space O(V)
- **Improvement**: Use a tie-breaking heuristic or bidirectional A\* for larger maps.
