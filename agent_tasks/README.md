# Agent Tasks — Framework Interfaces & Backlog

This document describes the Agent framework interfaces used in this repository,
message/MCP integration notes, and the current task backlog with priorities.

---

## Pathfinder Interface

All pathfinding implementations must expose the following function:

```python
def pathfind(
    start: tuple[int, int],
    goal: tuple[int, int],
    grid: list[list[int]],
    heuristic: callable = None,
) -> list[tuple[int, int]] | None:
    """
    Find a path from start to goal on a 2-D grid.

    Parameters
    ----------
    start : (row, col) of the starting cell.
    goal  : (row, col) of the target cell.
    grid  : 2-D list where 0 = passable, 1 = blocked.
    heuristic : optional callable h(a, b) -> float estimating distance.
                If None, the algorithm uses uniform cost (Dijkstra / BFS).

    Returns
    -------
    List of (row, col) tuples from start to goal (inclusive), or None if
    no path exists.
    """
```

Implementations:

| File | Algorithm | Heuristic |
|------|-----------|-----------|
| `implementations/python/0001_a_star.py` | A* | Manhattan distance |
| `implementations/python/0002_bfs_grid.py` | BFS | None (unweighted) |
| `implementations/python/0003_dijkstra.py` | Dijkstra | None (weighted) |

---

## Message / MCP Integration Notes

When integrating with an **MCP (Multi-agent Communication Protocol)** or
message-passing framework, agents should:

1. **Receive** a task message containing: `{start, goal, grid, heuristic_name}`.
2. **Invoke** the appropriate `pathfind()` function.
3. **Return** a response message: `{path: [...] | null, cost: float}`.

Example message schema (JSON):

```json
{
  "task": "pathfind",
  "start": [0, 0],
  "goal": [4, 4],
  "grid": [[0,0,0],[0,1,0],[0,0,0]],
  "heuristic": "manhattan"
}
```

Supported heuristic names: `"manhattan"`, `"euclidean"`, `"none"`.

---

## Tasks Backlog & Priorities

### High Priority

- [x] **0001** — A* pathfinding on grid (Manhattan heuristic)
- [x] **0002** — BFS grid shortest path
- [x] **0003** — Dijkstra weighted graph
- [x] **0004** — Priority queue wrapper (heapq)
- [x] **0005** — Minimax for tic-tac-toe (alpha-beta pruning)

### Medium Priority

- [ ] **0006** — Bellman-Ford (negative weights support)
- [ ] **0007** — Jump Point Search (JPS) optimization for A*
- [ ] **0008** — Monte Carlo Tree Search (MCTS) basics
- [ ] **0009** — Bidirectional BFS
- [ ] **0010** — Flow networks / max-flow (Ford-Fulkerson)

### Low Priority / Stretch Goals

- [ ] **0011** — Hierarchical pathfinding (HPA*)
- [ ] **0012** — Potential fields for agent navigation
- [ ] **0013** — Minimax with iterative deepening (IDDFS)
- [ ] **0014** — Reinforcement learning Q-table basics

---

## Adding a New Agent Task

1. Create `problems/agents/<id>-<slug>.md` following `templates/problem-template.md`.
2. Implement in `implementations/python/<id>_<slug>.py`.
3. Expose `pathfind(start, goal, grid, heuristic)` or a documented equivalent.
4. Add tests in `tests/test_<id>_<slug>.py`.
5. Update this backlog and `problems/index.md`.
