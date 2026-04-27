# Learning Plan — Algorithms for Agent & DMT

> **Audience**: DMT student who knows Python but is new to algorithms.  
> **Goal**: Learn algorithms that directly power an Agent project + simple game demos.  
> **Schedule assumption**: ≈1.5 h/day on weekdays, more on weekends; 3 h/day in summer holiday.  
> **Exam break**: Final exam week (late June) — pause intensive algorithm study.

---

## Priority Order

1. Agent framework & MCP integration (ongoing May–June)
2. Algorithms that directly serve the Agent (pathfinding → search → decision)
3. Summer deep-dive: DP, minimax, MCTS, optimization
4. Connect every algorithm learned back to the Agent or a game demo

---

## Phase 1 — Foundation & Agent Essentials (May – June, before exams)

### Week 1 — Complexity + Arrays + Repo Setup
| Day | Task | Time |
|-----|------|------|
| 1 | Read `docs/complexity.md`; Big-O intuition | 1.5 h |
| 2 | Arrays: two-sum, sliding-window intro | 1.5 h |
| 3 | Implement & test `problems/agents/0001-a_star` | 1.5 h |
| 4 | Review A\*; integrate pathfinder stub into Agent | 1.5 h |
| 5 | Weekend — finish BFS grid (`0002`) + run demo map | 3–4 h |

**Repo actions**: Finalize README, templates, `problems/index.md`.  
**DMT mini-task**: Write a script to load an image and print per-channel mean/std.

### Week 2 — BFS / DFS / Priority Queue
| Focus | Problems |
|-------|----------|
| BFS on grids | `0002-bfs-grid` |
| Dijkstra (weighted graphs) | `0003-dijkstra` |
| Priority queue (heapq) | `0004-priority-queue` |

**Agent tie-in**: Wrap Dijkstra as `agent.pathfinder(start, goal, graph)` → path.

### Week 3 — Decision & Search
| Focus | Problems |
|-------|----------|
| Minimax + simple alpha-beta | `0005-minimax-tictactoe` |
| Finite State Machine pattern | `agent_tasks/` notes |
| Behavior tree concept | read + sketch implementation |

### Week 4 — Sorting / Divide & Conquer / Binary Search
| Focus | Notes |
|-------|-------|
| Merge sort, quick sort | Understand recursion tree |
| Binary search variants | Sorted search in maps/arrays |

### Week 5 — Greedy & Heap
| Focus | Notes |
|-------|-------|
| Greedy heuristics | Path cost estimation |
| Heap / priority queue | Already covered; reinforce |

### Week 6 — Dynamic Programming (intro)
| Focus | Problems |
|-------|----------|
| Fibonacci (memo vs tabulation) | Understand overlapping sub-problems |
| 0-1 Knapsack | State definition practice |
| Longest Increasing Subsequence | |

> **Late June (exam week)**: Pause algorithm work. Review course material only.

---

## Phase 2 — Summer Acceleration (July – August, ≈3 h/day)

### Week 7 — Advanced Search & Game AI
| Focus | Notes |
|-------|-------|
| Monte Carlo Tree Search (MCTS) basics | Apply to simple board game |
| Alpha-Beta pruning deeper | Connect to game demo NPC |
| Local search / hill-climbing | Parameter tuning |

### Week 8 — DMT Project 1 — Image Algorithms
| Task | Detail |
|------|--------|
| Spatial convolution (box, Gaussian, Sobel) | Implement from scratch |
| FFT-based convolution | Compare runtime with spatial |
| Write `DMT_projects/project1/README.md` | Complexity table + plots |

### Week 9 — DMT Project 2 — Compression & Retrieval
| Task | Detail |
|------|--------|
| Run-Length Encoding (RLE) | Simple, fast |
| Huffman coding | Build tree + encode grayscale image |
| Compare compression ratios | |

### Week 10 — Agent Framework v0.9
| Task | Detail |
|------|--------|
| Integrate pathfinder, decision module, task queue | |
| Benchmark: A\* vs BFS vs Dijkstra on game maps | |
| Plug-in architecture for swappable algorithms | |

---

## Key Algorithms by Priority (Agent & Game Focus)

| Priority | Algorithm | Applies To |
|----------|-----------|------------|
| ★★★ | Grid BFS / DFS | Map exploration, connectivity |
| ★★★ | A\* | Heuristic pathfinding |
| ★★★ | Dijkstra | Weighted graph shortest path |
| ★★★ | Priority Queue | Open-set management in search |
| ★★★ | Finite State Machine | NPC behaviour |
| ★★☆ | Minimax + Alpha-Beta | Turn-based game AI |
| ★★☆ | MCTS | High-branching-factor games |
| ★★☆ | Dynamic Programming | Optimal planning |
| ★☆☆ | Quadtree / KD-tree | Spatial partitioning, collision |
| ★☆☆ | Basic RL (Q-learning) | Agent learning (optional) |

---

## Daily Practice Template (30 min read + 60 min code)

1. **Read** the problem `.md` and draw 2 concrete examples (edge + typical).
2. **Write** brute-force pseudocode; analyze complexity.
3. **Identify** the bottleneck and choose a pattern (BFS / DP / Greedy …).
4. **Implement** in Python; run `pytest`.
5. **Integrate** into Agent or game demo if applicable.
6. **Write 3-line review** at the bottom of the problem `.md`:
   - Key idea | Complexity | Possible improvement

---

## Resources

| Topic | Resource |
|-------|----------|
| A\* & grid pathfinding | [Red Blob Games — A\* tutorial](https://www.redblobgames.com/pathfinding/a-star/introduction.html) |
| Minimax / MCTS | David Silver lecture notes; Wikipedia pseudocode |
| Python algorithms | *Python Algorithms* by Magnus Lie Hetland |
| RL basics | Sutton & Barto — *Reinforcement Learning* (free PDF) |
| Image algorithms | OpenCV docs + NumPy FFT tutorial |
| Game AI | *AI for Games* by Ian Millington |
