"""
Problem ID: 0002
Title: BFS Grid Search
Difficulty: Easy
Topics: graph, bfs, agent

Shortest path on a 2-D grid using Breadth-First Search.
"""
from collections import deque
from typing import Optional


def find_path(
    grid: list[list[int]],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> list[tuple[int, int]]:
    """
    BFS shortest path on a 2-D grid.

    Args:
        grid:  2-D list; 0 = passable, 1 = wall.
        start: (row, col) starting cell.
        goal:  (row, col) target cell.

    Returns:
        Ordered list of (row, col) from start to goal, or [] if unreachable.

    Time:  O(V + E)  where V = rows*cols, E ≈ 4V
    Space: O(V)
    """
    rows, cols = len(grid), len(grid[0])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < rows and 0 <= c < cols

    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return []

    if start == goal:
        return [start]

    visited: set[tuple[int, int]] = {start}
    parent: dict[tuple[int, int], Optional[tuple[int, int]]] = {start: None}
    queue: deque[tuple[int, int]] = deque([start])

    while queue:
        current = queue.popleft()
        r, c = current
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            neighbour = (nr, nc)
            if neighbour in visited:
                continue
            visited.add(neighbour)
            parent[neighbour] = current
            if neighbour == goal:
                path: list[tuple[int, int]] = []
                node: Optional[tuple[int, int]] = goal
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                return path
            queue.append(neighbour)

    return []


if __name__ == "__main__":
    demo_grid = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0],
    ]
    print(find_path(demo_grid, (0, 0), (2, 2)))
