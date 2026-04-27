"""
0001 – A* Pathfinding
=====================
Problem: Find the shortest path in a 2-D grid from start to goal
         using the A* search algorithm with Manhattan distance heuristic.
Source:  custom
Difficulty: Medium
Topics: graph, heuristic-search, priority-queue

Time  complexity: O(E log V) where V = rows*cols, E = 4*V
Space complexity: O(V)
"""

from __future__ import annotations

import heapq
from typing import List, Optional, Tuple

Grid = List[List[int]]
Cell = Tuple[int, int]
Path = List[Cell]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _manhattan(a: Cell, b: Cell) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid: Grid, start: Cell, goal: Cell) -> Path:
    """Return the shortest path from *start* to *goal* on *grid*.

    *grid* is a 2-D list where 0 = free and 1 = obstacle.
    Returns a list of (row, col) tuples from start to goal (inclusive),
    or an empty list if no path exists.

    Examples:
        >>> grid = [[0,0,0],[0,1,0],[0,0,0]]
        >>> a_star(grid, (0,0), (2,2))
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    """
    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    # heap entries: (f, g, cell)
    h_start = _manhattan(start, goal)
    heap: List[Tuple[int, int, Cell]] = [(h_start, 0, start)]
    g_score = {start: 0}
    came_from: dict[Cell, Optional[Cell]] = {start: None}

    while heap:
        _, g, current = heapq.heappop(heap)

        if current == goal:
            # Reconstruct path
            path: Path = []
            node: Optional[Cell] = current
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            return path

        # Skip stale entries
        if g > g_score.get(current, float("inf")):
            continue

        r, c = current
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            neighbour: Cell = (nr, nc)
            tentative_g = g + 1
            if tentative_g < g_score.get(neighbour, float("inf")):
                g_score[neighbour] = tentative_g
                came_from[neighbour] = current
                f = tentative_g + _manhattan(neighbour, goal)
                heapq.heappush(heap, (f, tentative_g, neighbour))

    return []


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    path = a_star(_grid, (0, 0), (3, 3))
    print("Path:", path)
    print("Cost:", len(path) - 1 if path else "No path")
