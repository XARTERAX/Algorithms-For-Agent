# Agent Tasks

This directory tracks the Agent framework's algorithm integration backlog, interface contracts, and MCP integration notes.

---

## Pathfinder Interface

Every pathfinding algorithm in `implementations/python/` should expose the following function signature so the Agent can swap algorithms without changing call sites:

```python
def find_path(
    grid: list[list[int]],   # 0 = passable, 1 = wall
    start: tuple[int, int],  # (row, col)
    goal:  tuple[int, int],
) -> list[tuple[int, int]]:  # ordered path from start to goal, [] if none
    ...
```

Registered implementations:

| ID | Algorithm | Module |
|----|-----------|--------|
| 0001 | A\* | `implementations/python/0001_a_star.py` |
| 0002 | BFS grid | `implementations/python/0002_bfs_grid.py` |
| 0003 | Dijkstra | `implementations/python/0003_dijkstra.py` |

---

## MCP Integration Notes

> **MCP** = Model Context Protocol — used to let the Agent communicate with tools and external systems.

Key integration points to implement:

- `agent.pathfinder` — wraps one of the registered algorithms; selectable at runtime.
- `agent.planner` — sequences tasks using a priority queue; uses `0004_priority_queue.py`.
- `agent.game_ai` — decision module for turn-based games; uses `0005_minimax.py`.

MCP message structure (sketch):

```json
{
  "type": "action",
  "payload": {
    "command": "find_path",
    "args": { "start": [0, 0], "goal": [5, 5] }
  }
}
```

---

## Tasks Backlog

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1 | Implement A\* pathfinder | ✅ done | `0001_a_star.py` |
| 2 | Implement BFS grid search | ✅ done | `0002_bfs_grid.py` |
| 3 | Implement Dijkstra | ✅ done | `0003_dijkstra.py` |
| 4 | Implement priority queue wrapper | ✅ done | `0004_priority_queue.py` |
| 5 | Implement Minimax for TicTacToe | ✅ done | `0005_minimax.py` |
| 6 | Plug pathfinder into Agent framework | 🔲 todo | Select via config |
| 7 | MCP message handler for `find_path` | 🔲 todo | JSON schema above |
| 8 | Benchmark A\* vs BFS vs Dijkstra | 🔲 todo | Use `timeit` |
| 9 | Alpha-Beta pruning for Minimax | 🔲 todo | Extend `0005_minimax.py` |
| 10 | MCTS stub | 🔲 todo | For high-branching games |

---

## How to Add an Algorithm to the Agent

1. Implement `find_path(grid, start, goal) -> list` in `implementations/python/<id>_<name>.py`.
2. Write tests in `tests/test_<id>_<name>.py`.
3. Register in the table above.
4. Update the Agent config to reference the new module by ID.
