"""
0002 – BFS on a 2-D Grid
==========================
Topic      : agents / pathfinding
Difficulty : Easy

Problem
-------
Find the shortest path (fewest steps) between two cells on a grid
(0 = free, 1 = wall) using Breadth-First Search.

Examples
--------
>>> grid = [[0,0,1],[0,0,0],[1,0,0]]
>>> BFSPathfinder().find_path(grid, (0,0), (2,2))
[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

Complexity
----------
Time : O(rows * cols)
Space: O(rows * cols)
"""

from collections import deque
from typing import Dict, List, Optional, Tuple

GridPos = Tuple[int, int]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _reconstruct(came_from: Dict[GridPos, Optional[GridPos]], goal: GridPos) -> List[GridPos]:
    path: List[GridPos] = []
    cur: Optional[GridPos] = goal
    while cur is not None:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path


class BFSPathfinder:
    """BFS pathfinder for 2-D grids."""

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

        came_from: Dict[GridPos, Optional[GridPos]] = {start: None}
        queue: deque[GridPos] = deque([start])

        while queue:
            current = queue.popleft()
            r, c = current

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                    continue
                neighbour: GridPos = (nr, nc)
                if neighbour in came_from:
                    continue
                came_from[neighbour] = current
                if neighbour == goal:
                    return _reconstruct(came_from, goal)
                queue.append(neighbour)

        return None


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    grid = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0],
    ]
    pf = BFSPathfinder()
    path = pf.find_path(grid, (0, 0), (2, 2))
    print("Path:", path)
