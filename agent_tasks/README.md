# Agent Tasks

This directory documents the Agent framework interfaces, MCP integration notes, and the task backlog for algorithm-powered Agent demos.

---

## Pathfinding Interface

All pathfinding algorithms in this repository expose a common interface so that an Agent can swap solvers without changing its call site.

```python
def pathfind(
    start: tuple[int, int],
    goal: tuple[int, int],
    grid: list[list[int]],
    heuristic: callable = None,
) -> list[tuple[int, int]]:
    """
    Find a path from start to goal on a 2-D grid.

    Args:
        start     : (row, col) of the starting cell.
        goal      : (row, col) of the target cell.
        grid      : 2-D list where 0 = passable, 1 = obstacle.
        heuristic : Optional callable (node, goal) -> float.
                    Pass None to use BFS / Dijkstra (no heuristic).

    Returns:
        List of (row, col) tuples from start to goal (inclusive),
        or an empty list if no path exists.
    """
```

### Concrete implementations

| Module | Algorithm | Heuristic support |
|--------|-----------|-------------------|
| `implementations/python/0001_a_star.py` | A\* | Yes (Manhattan default) |
| `implementations/python/0002_bfs_grid.py` | BFS | No |
| `implementations/python/0003_dijkstra.py` | Dijkstra | No |

---

## MCP Integration Notes

> **MCP** (Model Context Protocol) lets you expose Python functions as tools that an LLM-based Agent can call at runtime.

### Exposing `pathfind` as an MCP tool

```python
# agent_tasks/mcp_pathfind.py  (sketch)
from mcp.server import MCPServer
from implementations.python.0001_a_star import a_star

server = MCPServer()

@server.tool()
def pathfind(start: list, goal: list, grid: list) -> list:
    """Return the shortest path from start to goal on a passable grid."""
    return a_star(tuple(start), tuple(goal), grid)

if __name__ == "__main__":
    server.run()
```

Key points:
- Keep tool signatures serialisable (lists / dicts, not tuples).
- Return an empty list `[]` — not `None` — when no path exists.
- Document the grid encoding (0 = free, 1 = wall) in the tool docstring.

---

## Task Backlog

| # | Task | Algorithm | Status |
|---|------|-----------|--------|
| 1 | Grid pathfinding demo | A\* | todo |
| 2 | BFS flood-fill area detection | BFS | todo |
| 3 | Weighted map navigation | Dijkstra | todo |
| 4 | Game AI for Tic-Tac-Toe | Minimax | todo |
| 5 | Priority-based event scheduler | Priority Queue | todo |
| 6 | Expose pathfinder via MCP | A\* + MCP | todo |
| 7 | Agent perception from image | OpenCV + BFS | todo |
| 8 | Q-learning grid world | RL | todo |
