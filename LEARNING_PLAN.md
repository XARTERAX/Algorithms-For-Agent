# Learning Plan — Algorithms for Agent & DMT

A structured 8-week schedule combining algorithm fundamentals with Agent integration and Digital Media Technology applications.

---

## Goals

- Master the core algorithms needed to build intelligent, game-ready Agents.
- Connect each algorithm to a concrete Agent or DMT demo.
- Keep implementation time focused: one algorithm per session, tests first.

---

## Weekly Schedule

### Week 1 — Graph Search Foundations
| Day | Topic | Task |
|-----|-------|------|
| Mon | A\* search | Study `problems/agents/0001-a_star.md`, run tests |
| Tue | BFS on grid | Study `problems/agents/0002-bfs-grid.md`, run tests |
| Wed | Dijkstra | Study `problems/agents/0003-dijkstra.md`, run tests |
| Thu | Priority Queue | Study `problems/agents/0004-priority-queue.md` |
| Fri | Review & refactor | Clean up implementations, add edge-case tests |

### Week 2 — Game AI Basics
| Day | Topic | Task |
|-----|-------|------|
| Mon | Minimax | Study `problems/agents/0005-minimax-tictactoe.md` |
| Tue | Alpha-Beta pruning | Extend minimax with pruning |
| Wed | Monte Carlo Tree Search (MCTS) intro | Read reference, sketch interface |
| Thu | Apply to a game demo | Hook A\* or minimax into a simple pygame demo |
| Fri | Review & document | Update `problems/index.md`, write 3-line recap |

### Week 3 — Dynamic Programming for Agents
- Memoisation patterns, state compression
- DP on grids (shortest path with obstacles)
- DP for game states

### Week 4 — Agent Framework Integration
- Implement `pathfind(start, goal, grid, heuristic)` interface (see `agent_tasks/README.md`)
- MCP integration: expose pathfinder as an MCP tool
- Write integration tests

### Week 5 — Computer Vision Foundations (DMT)
- Image convolution with numpy / opencv-python
- Edge detection (Sobel, Canny)
- Apply to agent perception: obstacles from image input

### Week 6 — Reinforcement Learning Basics
- Q-learning on a grid world
- Epsilon-greedy exploration
- Connect to the Agent pathfinder interface

### Week 7 — Project Sprint
- Build a small pygame demo that combines: Agent pathfinding + vision input + simple game rules
- Write a demo README with screenshots

### Week 8 — Review, Polish & Retrospective
- Audit `problems/index.md` — fill all status fields
- Write a retrospective in `docs/retrospective.md`
- Open issues for next iteration

---

## Recommended Resources

| Topic | Resource |
|-------|----------|
| A\*, Dijkstra | *Red Blob Games* — redblobgames.com/pathfinding |
| Minimax / Alpha-Beta | *CS50 AI* — cs50.harvard.edu/ai |
| DP patterns | *NeetCode* YouTube + LeetCode |
| OpenCV basics | Official docs — docs.opencv.org |
| pygame | pygame.org/docs |
| MCP integration | MCP spec in `agent_tasks/README.md` |

---

## Progress Tracking

Update the `status` column in `problems/index.md` as you finish each problem:
- `todo` → `in-progress` → `done`
