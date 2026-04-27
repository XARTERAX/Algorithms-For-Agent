---
title: "BFS Grid Search"
id: 0002
source: "classic graph"
difficulty: "Easy"
topics: ["graph", "bfs", "agent"]
languages: ["python"]
time_complexity: "O(V + E)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` is passable and `1` is a wall, find the shortest path (fewest steps) from `start` to `goal` using Breadth-First Search.

Return the path as a list of `(row, col)` tuples, or `[]` if unreachable.

# Examples

```
Grid:
  0 0 1
  0 0 0
  1 0 0

Input:  start=(0,0), goal=(2,2)
Output: [(0,0),(1,0),(1,1),(1,2),(2,2)]  # one possible shortest path

Input:  start=(0,0), goal=(0,2)  # (0,2) is a wall
Output: []
```

# Brute Force

There is no simpler correct approach for unweighted graphs — BFS is already the canonical optimal solution.

# Optimized Idea (思路链)

1. **Model** — each passable cell is a node; edges connect 4-adjacent passable cells.
2. **Pattern** — BFS guarantees shortest path (fewest hops) on an unweighted graph.
3. **Key invariant** — when a cell is first dequeued, its distance is optimal.
4. **Pseudocode**:

```
queue = deque([start])
visited = {start}
parent = {start: None}
while queue:
    current = queue.popleft()
    if current == goal: return reconstruct(parent, goal)
    for neighbour in passable_neighbours(current):
        if neighbour not in visited:
            visited.add(neighbour)
            parent[neighbour] = current
            queue.append(neighbour)
return []
```

# Implementation

See `implementations/python/0002_bfs_grid.py`.

# Tests

- Open grid — direct path.
- Path requires detour around walls.
- Goal unreachable.
- Start equals goal.

# Review (fill in after solving)

- **Key idea**: FIFO queue expands nodes level by level → shortest path guaranteed.
- **Complexity**: time O(V + E) | space O(V)
- **Improvement**: Bidirectional BFS halves effective search depth for large grids.
