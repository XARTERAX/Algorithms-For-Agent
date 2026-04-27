"""
Problem: A* Pathfinding on Grid
ID: 0001
Difficulty: Medium
Topics: agent, pathfinding, heuristic-search

Find the shortest path from start to goal on a 2-D grid using A* with the
Manhattan distance heuristic.

Function signature:
    find_path(grid, start, goal) -> list[tuple[int,int]] | None
"""

import heapq
from typing import List, Optional, Tuple

Grid = List[List[int]]
Cell = Tuple[int, int]


def _manhattan(a: Cell, b: Cell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_path(
    grid: Grid,
    start: Cell,
    goal: Cell,
) -> Optional[List[Cell]]:
    """
    A* shortest path on a 2-D grid.

    Parameters
    ----------
    grid  : rows x cols list; 0 = passable, 1 = blocked.
    start : (row, col) of start cell.
    goal  : (row, col) of goal cell.

    Returns
    -------
    List of (row, col) from start to goal inclusive, or None if no path.
    """
    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None

    # heap entries: (f, g, row, col, path)
    h0 = _manhattan(start, goal)
    heap: list = [(h0, 0, start[0], start[1], [start])]
    visited: set = set()

    while heap:
        f, g, r, c, path = heapq.heappop(heap)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == goal:
            return path

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                g2 = g + 1
                h = _manhattan((nr, nc), goal)
                heapq.heappush(heap, (g2 + h, g2, nr, nc, path + [(nr, nc)]))

    return None


# Expose the pathfind interface expected by agent_tasks
def pathfind(
    start: Cell,
    goal: Cell,
    grid: Grid,
    heuristic=None,
) -> Optional[List[Cell]]:
    """Agent framework interface — delegates to find_path."""
    return find_path(grid, start, goal)
