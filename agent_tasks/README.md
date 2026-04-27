# Agent Tasks — Framework & Backlog

This directory documents the **Agent framework** used throughout this repository and tracks outstanding work items.

---

## Pathfinder Interface

All graph-search implementations expose the following interface so they can be swapped into any agent without changing the calling code.

```python
from typing import Protocol, Sequence, Tuple, TypeVar

State = TypeVar("State")
Cost  = float


class Pathfinder(Protocol[State]):
    """Minimal interface every pathfinder must implement."""

    def find_path(
        self,
        start: State,
        goal: State,
    ) -> Tuple[Sequence[State], Cost]:
        """Return (path, total_cost).

        *path* is a sequence of states from *start* to *goal* (inclusive).
        *total_cost* is the sum of edge weights along the path.
        If no path exists, return ([], float('inf')).
        """
        ...
```

### Implementations

| ID | Algorithm | File |
|----|-----------|------|
| 0001 | A\* | `implementations/python/0001_a_star.py` |
| 0002 | BFS on grid | `implementations/python/0002_bfs_grid.py` |
| 0003 | Dijkstra | `implementations/python/0003_dijkstra.py` |
| 0004 | Priority Queue (helper) | `implementations/python/0004_priority_queue.py` |
| 0005 | Minimax (Tic-Tac-Toe) | `implementations/python/0005_minimax.py` |

---

## MCP Integration Notes

**MCP (Model-Context-Protocol)** is a lightweight protocol for letting an LLM agent call tools and inspect state.

To wire a pathfinder into an MCP agent:

1. Expose the `find_path` method as an MCP **tool** with a JSON schema for `start` and `goal`.
2. Serialize the grid / graph as part of the MCP **context** (system message or resources).
3. The agent calls `find_path(start, goal)` and receives `(path, cost)` in the tool response.
4. The agent can then render the path, explain the steps, or invoke further tools.

Example tool schema (JSON):

```json
{
  "name": "find_path",
  "description": "Find shortest path from start to goal on a 2-D grid.",
  "parameters": {
    "type": "object",
    "properties": {
      "start": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
      "goal":  { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 }
    },
    "required": ["start", "goal"]
  }
}
```

---

## Tasks Backlog

### In progress

- [ ] A\* on 2-D grid with obstacle maps
- [ ] BFS for multi-source shortest paths
- [ ] Dijkstra with dynamic edge weights

### Planned

- [ ] Theta\* / Jump Point Search (JPS) for faster grid navigation
- [ ] Monte Carlo Tree Search (MCTS) for game agents
- [ ] Alpha-Beta pruning extension for Minimax
- [ ] Policy gradient stub for RL-based agents
- [ ] Pygame visualiser for grid pathfinders
- [ ] MCP tool wrapper for all pathfinders
- [ ] Benchmarking harness (time and node-expansion comparison)

### Done

- [x] Pathfinder interface defined (this file)
- [x] A\* implementation + tests
- [x] BFS grid implementation + tests
- [x] Dijkstra implementation + tests
- [x] Priority queue helper + tests
- [x] Minimax (Tic-Tac-Toe) + tests
