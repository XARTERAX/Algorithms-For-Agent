"""
Problem ID: 0001
Title: A* Pathfinding
Difficulty: Medium
Topics: graph, heuristic-search, agent

Find the shortest path on a 2-D grid using A* with Manhattan distance.
"""
import heapq
from typing import Optional


def find_path(
    grid: list[list[int]],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> list[tuple[int, int]]:
    """
    A* shortest path on a 2-D grid.

    Args:
        grid:  2-D list; 0 = passable, 1 = wall.
        start: (row, col) starting cell.
        goal:  (row, col) target cell.

    Returns:
        Ordered list of (row, col) from start to goal, or [] if unreachable.

    Time:  O(E log V)  where V = rows*cols, E ≈ 4V
    Space: O(V)
    """
    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    def h(node: tuple[int, int]) -> int:
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return []

    g_score: dict[tuple[int, int], int] = {start: 0}
    parent: dict[tuple[int, int], Optional[tuple[int, int]]] = {start: None}
    heap: list[tuple[int, tuple[int, int]]] = [(h(start), start)]

    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            path: list[tuple[int, int]] = []
            node: Optional[tuple[int, int]] = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path

        r, c = current
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            neighbour = (nr, nc)
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbour, float("inf")):
                g_score[neighbour] = tentative_g
                parent[neighbour] = current
                heapq.heappush(heap, (tentative_g + h(neighbour), neighbour))

    return []


if __name__ == "__main__":
    demo_grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    print(find_path(demo_grid, (0, 0), (2, 2)))
    # Expected: [(0,0),(0,1),(0,2),(1,2),(2,2)]
