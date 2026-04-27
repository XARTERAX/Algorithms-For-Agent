# Algorithms-For-Agent

A study and development workspace for algorithms focused on **Agent AI** and **game demos**, tailored to Digital Media Technology (DMT) students.

---

## Project Overview

This repository provides structured algorithm study materials with a focus on agent-based pathfinding, search, game AI, and decision-making algorithms. Each problem includes a problem description, brute-force analysis, optimized idea, pseudocode, Python implementation, and unit tests.

---

## Repository Structure

```
Algorithms-For-Agent/
├── README.md               # This file
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # MIT License
├── requirements.txt        # Python dependencies
├── .gitignore              # Python gitignore
├── .pre-commit-config.yaml # Pre-commit hooks (black, flake8)
│
├── templates/              # Problem & solution templates
│   ├── problem-template.md
│   └── solution-template.py
│
├── docs/                   # Algorithm concept notes
│   └── complexity.md       # O/Θ/Ω notation with examples
│
├── agent_tasks/            # Agent framework interfaces & backlog
│   └── README.md
│
├── problems/               # Algorithm problems by topic
│   ├── index.md            # Master problem index table
│   └── agents/             # Agent/pathfinding problems
│       ├── 0001-a_star.md
│       ├── 0002-bfs-grid.md
│       ├── 0003-dijkstra.md
│       ├── 0004-priority-queue.md
│       └── 0005-minimax-tictactoe.md
│
├── implementations/        # Python implementations
│   └── python/
│       ├── 0001_a_star.py
│       ├── 0002_bfs_grid.py
│       ├── 0003_dijkstra.py
│       ├── 0004_priority_queue.py
│       └── 0005_minimax.py
│
├── tests/                  # Pytest unit tests
│   ├── test_0001_a_star.py
│   ├── test_0002_bfs_grid.py
│   ├── test_0003_dijkstra.py
│   ├── test_0004_priority_queue.py
│   └── test_0005_minimax.py
│
└── algorithms/             # Legacy folder (user-authored notes & extras)
```

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/XARTERAX/Algorithms-For-Agent.git
cd Algorithms-For-Agent

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run all tests
pytest -q
```

---

## How to Run Tests

```bash
pytest -q                   # run all tests quietly
pytest tests/ -v            # verbose output
pytest tests/test_0001_a_star.py   # run a single test file
```

---

## Usage

1. Pick a topic in `problems/agents/` and read the `.md` for idea + pseudocode.
2. Study or run the corresponding implementation in `implementations/python/`.
3. Run the tests to verify correctness: `pytest tests/`.
4. Use `templates/problem-template.md` when adding new problems.

---

## Learning Plan Summary (Agent + DMT Focus)

| Week | Topic | Key Files |
|------|-------|-----------|
| 1 | Complexity, arrays, hash tables | `docs/complexity.md` |
| 2 | BFS / DFS on grids | `problems/agents/0002-bfs-grid.md` |
| 3 | Priority queues & heaps | `problems/agents/0004-priority-queue.md` |
| 4 | Dijkstra shortest path | `problems/agents/0003-dijkstra.md` |
| 5 | A* pathfinding | `problems/agents/0001-a_star.md` |
| 6 | Minimax & game AI | `problems/agents/0005-minimax-tictactoe.md` |
| 7–8 | DMT projects (image filters, convolution) | `algorithms/` |

---

## License

MIT — see [LICENSE](LICENSE).
