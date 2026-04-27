"""
Problem: BFS Grid Shortest Path
ID: 0002
Difficulty: Easy
Topics: agent, pathfinding, bfs

Find the shortest path (fewest steps) from start to goal on a 2-D grid using
Breadth-First Search.

Function signature:
    find_path(grid, start, goal) -> list[tuple[int,int]] | None
"""

from collections import deque
from typing import List, Optional, Tuple

Grid = List[List[int]]
Cell = Tuple[int, int]


def find_path(
    grid: Grid,
    start: Cell,
    goal: Cell,
) -> Optional[List[Cell]]:
    """
    BFS shortest path on an unweighted 2-D grid.

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

    queue: deque = deque([(start, [start])])
    visited: set = {start}

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == goal:
            return path

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

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
