# Algorithms-For-Agent

A study and development workspace for algorithms focused on **Agent** and game demos.  
All implementations are in Python; problems are organised by topic under `problems/`.

---

## Repository Structure

```
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── .pre-commit-config.yaml
│
├── templates/                  # Reusable templates for new problems and solutions
│   ├── problem-template.md
│   └── solution-template.py
│
├── docs/                       # Concept notes (complexity, patterns, …)
│   └── complexity.md
│
├── agent_tasks/                # Agent framework interfaces and task backlog
│   └── README.md
│
├── problems/                   # Problem statements organised by topic
│   ├── index.md                # Master index of all problems
│   └── agents/                 # Agent-specific algorithms
│       ├── 0001-a_star.md
│       ├── 0002-bfs-grid.md
│       ├── 0003-dijkstra.md
│       ├── 0004-priority-queue.md
│       └── 0005-minimax-tictactoe.md
│
├── implementations/            # Runnable implementations
│   └── python/
│       ├── 0001_a_star.py
│       ├── 0002_bfs_grid.py
│       ├── 0003_dijkstra.py
│       ├── 0004_priority_queue.py
│       └── 0005_minimax.py
│
├── tests/                      # pytest test suite
│   ├── test_0001_a_star.py
│   ├── test_0002_bfs_grid.py
│   ├── test_0003_dijkstra.py
│   ├── test_0004_priority_queue.py
│   └── test_0005_minimax.py
│
└── algorithms/                 # Legacy study notes (DMT-focused, pre-existing)
    ├── README.md
    ├── Docs/
    ├── Problems/
    └── Template/
```

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/XARTERAX/Algorithms-For-Agent.git
cd Algorithms-For-Agent

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run all tests
pytest tests/ -v
```

---

## How to Add a New Problem

1. Copy `templates/problem-template.md` to `problems/<topic>/XXXX-short-title.md` and fill in every section.  
2. Copy `templates/solution-template.py` to `implementations/python/XXXX_short_title.py` and implement the solution.  
3. Add a test file `tests/test_XXXX_short_title.py` with at least the sample cases.  
4. Register the problem in `problems/index.md`.

---

## Agent Framework Integration

See `agent_tasks/README.md` for:
- The **Pathfinder** interface used by all graph-search algorithms.
- Notes on **MCP (Model-Context-Protocol)** integration.
- The current tasks backlog.

---

## Learning Plan Summary

| Phase | Topics | Key Files |
|-------|--------|-----------|
| 1 – Foundations | Complexity, Arrays, Hash | `docs/complexity.md` |
| 2 – Graph Search | BFS, Dijkstra, A\* | `problems/agents/` |
| 3 – Adversarial | Minimax, α-β pruning | `problems/agents/0005-minimax-tictactoe.md` |
| 4 – Agent Demos | Full pathfinder demos | `agent_tasks/` |

---

## Running Tests

```bash
pytest tests/ -v --tb=short
```

Individual test:

```bash
pytest tests/test_0001_a_star.py -v
```

---

## License

MIT – see [LICENSE](LICENSE).
