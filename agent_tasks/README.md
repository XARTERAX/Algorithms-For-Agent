# Agent Tasks

This directory describes the **Agent framework** used throughout this repo, defines interfaces that every algorithm implementation should follow, and tracks the integration task backlog.

---

## Pathfinder Interface

Every pathfinding implementation (A\*, BFS, Dijkstra, …) should expose the following callable signature so agents can swap strategies at runtime:

```python
from typing import Protocol, List, Tuple, Optional

GridPos = Tuple[int, int]

class Pathfinder(Protocol):
    """Minimal interface for a grid-based pathfinder."""

    def find_path(
        self,
        grid: List[List[int]],
        start: GridPos,
        goal: GridPos,
    ) -> Optional[List[GridPos]]:
        """Return an ordered list of (row, col) positions from start to goal,
        or None if no path exists.

        Parameters
        ----------
        grid : List[List[int]]
            2-D grid where 0 = passable, 1 = wall.
        start : (row, col)
            Starting position.
        goal : (row, col)
            Target position.

        Returns
        -------
        List[GridPos] | None
            Path including start and goal, or None if unreachable.
        """
        ...
```

All implementations in `implementations/python/` follow this interface.

---

## MCP (Model-Context-Protocol) Integration Notes

> MCP lets an LLM-based agent call tools defined in this repo as structured functions.

**Planned MCP tool definitions:**

| Tool name | Description | Implementation |
|-----------|-------------|----------------|
| `pathfind.astar` | Find shortest weighted path | `0001_a_star.py` |
| `pathfind.bfs` | Find shortest unweighted path on a grid | `0002_bfs_grid.py` |
| `pathfind.dijkstra` | Shortest path in weighted graph | `0003_dijkstra.py` |
| `game.minimax` | Best move in a Tic-Tac-Toe board | `0005_minimax.py` |

**Integration pattern (pseudo-code):**

```python
from mcp import MCPServer
from implementations.python import a_star, bfs_grid

server = MCPServer()

@server.tool("pathfind.astar")
def astar_tool(grid, start, goal):
    return a_star.AStarPathfinder().find_path(grid, start, goal)
```

---

## Task Backlog

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1 | Implement A\* pathfinder | ✅ Done | `0001_a_star.py` |
| 2 | Implement BFS grid pathfinder | ✅ Done | `0002_bfs_grid.py` |
| 3 | Implement Dijkstra | ✅ Done | `0003_dijkstra.py` |
| 4 | Priority Queue implementation | ✅ Done | `0004_priority_queue.py` |
| 5 | Minimax Tic-Tac-Toe | ✅ Done | `0005_minimax.py` |
| 6 | Alpha-Beta Pruning | ⬜ Planned | Extend `0005_minimax.py` |
| 7 | Flood Fill (island count) | ⬜ Planned | `0006_flood_fill.py` |
| 8 | MCTS (Monte Carlo Tree Search) | ⬜ Planned | Game agent |
| 9 | MCP server wrapper | ⬜ Planned | Expose tools via MCP |
| 10 | pygame demo (A\* visualizer) | ⬜ Planned | Requires pygame |
