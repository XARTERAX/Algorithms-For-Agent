"""
Problem ID : 0002
Title      : BFS on Grid
Difficulty : Easy
Topics     : graph, bfs, pathfinding
Date       : 2024-01-01
"""

from collections import deque
from typing import List, Tuple


def bfs_grid(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    grid: List[List[int]],
) -> List[Tuple[int, int]]:
    """
    Find the shortest path from start to goal on a 2-D grid using BFS.

    Args:
        start : (row, col) starting cell.
        goal  : (row, col) target cell.
        grid  : 2-D list; 0 = passable, 1 = obstacle.

    Returns:
        List of (row, col) from start to goal inclusive, or [] if none.

    Time:  O(rows * cols)
    Space: O(rows * cols)
    """
    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    if start == goal:
        return [start]

    visited = {start}
    parent = {start: None}
    queue = deque([start])

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            neighbour = (nr, nc)
            if neighbour in visited:
                continue
            visited.add(neighbour)
            parent[neighbour] = (r, c)
            if neighbour == goal:
                # Reconstruct path
                path = []
                node = goal
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            queue.append(neighbour)

    return []


# ---------------------------------------------------------------------------
# Smoke-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    path = bfs_grid((0, 0), (2, 3), grid)
    print("Path:", path)
    assert path[0] == (0, 0) and path[-1] == (2, 3)
    print("Smoke-test passed.")
