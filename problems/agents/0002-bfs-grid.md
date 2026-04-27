---
title: "BFS on Grid"
id: 0002
source: ""
difficulty: "Easy"
topics: ["graph", "bfs", "pathfinding"]
languages: ["python"]
time_complexity: "O(V + E) = O(rows × cols)"
space_complexity: "O(rows × cols)"
date: 2024-01-01
---

# Problem

Given a 2-D grid (0 = passable, 1 = obstacle), a start cell, and a goal cell, find the shortest path using Breadth-First Search (BFS). Because every step has equal cost, BFS guarantees the minimum number of steps.

Return the path as a list of `(row, col)` tuples, or `[]` if no path exists.

## Examples

**Example 1**
- Grid (3×4):
  ```
  0 0 1 0
  0 0 0 0
  1 0 0 0
  ```
- Input: `start=(0,0)`, `goal=(2,3)`
- Output: `[(0,0),(0,1),(1,1),(1,2),(1,3),(2,3)]` *(one valid shortest path)*

**Example 2 — blocked**
- Grid (2×2):
  ```
  0 1
  1 0
  ```
- Input: `start=(0,0)`, `goal=(1,1)`
- Output: `[]`

## Constraints

- Grid: 1 ≤ rows, cols ≤ 200
- 4-directional movement only

# Approach

## Brute Force

DFS can find *a* path but not necessarily the shortest one.

## Optimized Idea

1. Use a FIFO queue; enqueue `start`.
2. Track visited cells to avoid cycles.
3. For each cell dequeued, enqueue its unvisited passable neighbours.
4. Record the parent of each cell to reconstruct the path.

```
queue = deque([start])
visited = {start}
parent = {start: None}

while queue:
    cell = queue.popleft()
    if cell == goal:
        reconstruct path via parent and return
    for each neighbour:
        if neighbour not in visited and passable:
            visited.add(neighbour)
            parent[neighbour] = cell
            queue.append(neighbour)
return []
```

## Complexity Analysis

| | Time | Space |
|---|---|---|
| DFS | O(V+E) | O(V) |
| BFS | O(V+E) | O(V) |

# Implementation (Python)

```python
# See implementations/python/0002_bfs_grid.py
```

# 3-Line Recap

1. **Key idea**: Explore cells level-by-level with a FIFO queue; the first time the goal is reached, the path is shortest.
2. **Why it works**: BFS visits all cells at distance d before any at distance d+1, so the goal is found at minimum cost.
3. **Pitfalls / edge cases**: Mark cells visited *when enqueued* (not when dequeued) to avoid re-adding the same cell multiple times.
