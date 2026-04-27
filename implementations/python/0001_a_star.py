"""
Problem ID : 0001
Title      : A* Search
Difficulty : Medium
Topics     : graph, heuristic-search, pathfinding
Date       : 2024-01-01
"""

import heapq
from typing import Callable, List, Optional, Tuple


def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    grid: List[List[int]],
    heuristic: Optional[Callable] = None,
) -> List[Tuple[int, int]]:
    """
    Find the shortest path from start to goal on a 2-D grid using A*.

    Args:
        start     : (row, col) starting cell.
        goal      : (row, col) target cell.
        grid      : 2-D list; 0 = passable, 1 = obstacle.
        heuristic : callable(node, goal) -> float. Defaults to Manhattan.

    Returns:
        List of (row, col) from start to goal inclusive, or [] if none.

    Time:  O(E log V)
    Space: O(V)
    """
    if heuristic is None:
        heuristic = manhattan

    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    def passable(r: int, c: int) -> bool:
        return grid[r][c] == 0

    g_score = {start: 0}
    came_from = {}
    # heap entries: (f, g, node)
    counter = 0
    heap = [(heuristic(start, goal), 0, counter, start)]
    visited = set()

    while heap:
        f, g, _, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            return path[::-1]

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or not passable(nr, nc):
                continue
            neighbour = (nr, nc)
            tentative_g = g + 1
            if tentative_g < g_score.get(neighbour, float("inf")):
                g_score[neighbour] = tentative_g
                came_from[neighbour] = current
                counter += 1
                heapq.heappush(
                    heap,
                    (tentative_g + heuristic(neighbour, goal), tentative_g, counter, neighbour),
                )

    return []


# ---------------------------------------------------------------------------
# Smoke-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    path = a_star((0, 0), (3, 3), grid)
    print("Path:", path)
    assert path[0] == (0, 0) and path[-1] == (3, 3)
    print("Smoke-test passed.")
