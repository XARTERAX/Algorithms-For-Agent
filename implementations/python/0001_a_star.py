"""
0001 – A* Search on a 2-D Grid
================================
Topic      : agents / pathfinding
Difficulty : Medium

Problem
-------
Find the shortest path between two cells on a grid (0 = free, 1 = wall)
using the A* algorithm with the Manhattan distance heuristic.

Examples
--------
>>> grid = [[0,0,0],[1,1,0],[0,0,0]]
>>> AStarPathfinder().find_path(grid, (0,0), (2,2))
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

Complexity
----------
Time : O(E log V)  where V = rows*cols, E = 4*V
Space: O(V)
"""

import heapq
from typing import Dict, List, Optional, Tuple

GridPos = Tuple[int, int]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _manhattan(a: GridPos, b: GridPos) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _reconstruct(came_from: Dict[GridPos, Optional[GridPos]], goal: GridPos) -> List[GridPos]:
    path: List[GridPos] = []
    cur: Optional[GridPos] = goal
    while cur is not None:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path


class AStarPathfinder:
    """A* pathfinder for 2-D grids."""

    def find_path(
        self,
        grid: List[List[int]],
        start: GridPos,
        goal: GridPos,
    ) -> Optional[List[GridPos]]:
        """Return shortest path from start to goal, or None if unreachable."""
        rows, cols = len(grid), len(grid[0])

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
            return None

        if start == goal:
            return [start]

        g_score: Dict[GridPos, int] = {start: 0}
        came_from: Dict[GridPos, Optional[GridPos]] = {start: None}
        # heap entries: (f, g, (row, col))
        heap: List[Tuple[int, int, GridPos]] = [((_manhattan(start, goal)), 0, start)]

        while heap:
            f, g, current = heapq.heappop(heap)

            if current == goal:
                return _reconstruct(came_from, goal)

            # Skip stale heap entries
            if g > g_score.get(current, float("inf")):
                continue

            r, c = current
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                    continue
                neighbour: GridPos = (nr, nc)
                tentative_g = g + 1
                if tentative_g < g_score.get(neighbour, float("inf")):
                    g_score[neighbour] = tentative_g
                    came_from[neighbour] = current
                    f_new = tentative_g + _manhattan(neighbour, goal)
                    heapq.heappush(heap, (f_new, tentative_g, neighbour))

        return None


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    pf = AStarPathfinder()
    path = pf.find_path(grid, (0, 0), (2, 2))
    print("Path:", path)
