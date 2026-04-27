"""
0002 – BFS on Grid
==================
Problem: Find the minimum number of steps from start to goal
         on a 2-D grid using BFS.
Source:  custom
Difficulty: Easy
Topics: graph, BFS, grid

Time  complexity: O(rows * cols)
Space complexity: O(rows * cols)
"""

from __future__ import annotations

from collections import deque
from typing import List, Tuple

Grid = List[List[int]]
Cell = Tuple[int, int]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs_grid(grid: Grid, start: Cell, goal: Cell) -> int:
    """Return the minimum number of steps from *start* to *goal*.

    Returns -1 if no path exists.
    *grid* cells: 0 = free, 1 = obstacle.

    Examples:
        >>> grid = [[0,0,0],[0,1,0],[0,0,0]]
        >>> bfs_grid(grid, (0,0), (2,2))
        4
        >>> bfs_grid([[0,1],[1,0]], (0,0), (1,1))
        -1
    """
    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    if start == goal:
        return 0

    queue: deque[Tuple[Cell, int]] = deque([(start, 0)])
    visited = {start}

    while queue:
        (r, c), dist = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            neighbour: Cell = (nr, nc)
            if neighbour == goal:
                return dist + 1
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))

    return -1


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print("Steps:", bfs_grid(_grid, (0, 0), (2, 2)))  # expected 4

    _blocked = [[0, 1], [1, 0]]
    print("Blocked:", bfs_grid(_blocked, (0, 0), (1, 1)))  # expected -1
