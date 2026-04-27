---
title: "BFS on a Grid"
id: 0002
source: "custom"
difficulty: "Easy"
topics: ["graph", "BFS", "pathfinding", "queue"]
languages: ["python"]
time_complexity: "O(rows × cols)"
space_complexity: "O(rows × cols)"
date: 2026-04-27
---

# Problem

Given a 2-D grid where `0` is passable and `1` is a wall, find the **shortest path** (fewest steps) from `start` to `goal` using Breadth-First Search.

**Input:**
- `grid`: `List[List[int]]`
- `start`: `(row, col)`
- `goal`: `(row, col)`

**Output:** `List[(row, col)]` path, or `None` if unreachable.

# Examples

```
grid = [
  [0, 0, 1],
  [0, 0, 0],
  [1, 0, 0],
]
start = (0, 0), goal = (2, 2)

Output: [(0,0), (1,0), (1,1), (1,2), (2,2)]
```

```
grid = [[0, 1], [1, 0]]
start = (0, 0), goal = (1, 1)

Output: None   # no path
```

# Brute Force

DFS explores all paths and picks the shortest — exponential in the worst case.

# Optimized Idea (思路链)

1. **Model** — Grid as an unweighted graph; each free cell has up to 4 neighbours.
2. **Brute force recap** — DFS is not guaranteed to find shortest path first.
3. **Pattern** — BFS processes cells in FIFO order, guaranteeing the first time a cell is reached is via the shortest path.
4. **Key invariant** — A cell in BFS level k is exactly k steps from start.
5. **Pseudocode**

```
queue ← deque([start])
visited ← {start}
came_from ← {start: None}

while queue:
    current = queue.popleft()
    if current == goal: return reconstruct(came_from, goal)
    for neighbour in 4-directions(current):
        if neighbour not visited and grid[neighbour] == 0:
            visited.add(neighbour)
            came_from[neighbour] = current
            queue.append(neighbour)
return None
```

- Time: O(rows × cols) · Space: O(rows × cols)

# Implementation (Python)

```python
# See implementations/python/0002_bfs_grid.py
```

# Tests

| # | Input | Expected Output | Notes |
|---|-------|-----------------|-------|
| 1 | Open 3×3 grid | shortest path | happy path |
| 2 | Blocked grid | None | no path |
| 3 | start == goal | [start] | trivial |

# Recap (3 lines)

1. **Key idea:** BFS explores cells level by level using a queue, so the first path found to the goal is always the shortest.
2. **Why correct:** All edges have equal weight (1 step), so BFS level = distance from start.
3. **Complexity:** Time O(rows × cols), Space O(rows × cols).
