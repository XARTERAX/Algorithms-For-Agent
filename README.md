# Algorithms-For-Agent

A personal study and development workspace for algorithms useful for Agent and game demos, tailored to Digital Media Technology (DMT) students.

## Project Overview

This repository collects algorithm problems, clean Python implementations, and minimal unit tests focused on the algorithms most relevant to building intelligent agents, game AI, and interactive media demos.

## Repository Structure

```
.
├── README.md                  # This file
├── LEARNING_PLAN.md           # Detailed weekly learning plan
├── CONTRIBUTING.md            # Contribution and commit style guide
├── requirements.txt           # Python dependencies
├── LICENSE                    # MIT License
├── .gitignore                 # Python gitignore
├── .pre-commit-config.yaml    # black + flake8 hooks
├── templates/
│   ├── problem-template.md    # Template for new problem write-ups
│   └── solution-template.py   # Template for new Python solutions
├── docs/
│   └── complexity.md          # Quick-reference complexity cheat-sheet
├── agent_tasks/
│   └── README.md              # Agent framework interfaces & task backlog
├── problems/
│   ├── index.md               # Master index of all problems
│   └── agents/                # Agent-focused algorithm problems
│       ├── 0001-a_star.md
│       ├── 0002-bfs-grid.md
│       ├── 0003-dijkstra.md
│       ├── 0004-priority-queue.md
│       └── 0005-minimax-tictactoe.md
├── implementations/
│   └── python/                # Python implementations
│       ├── 0001_a_star.py
│       ├── 0002_bfs_grid.py
│       ├── 0003_dijkstra.py
│       ├── 0004_priority_queue.py
│       └── 0005_minimax.py
├── tests/                     # pytest unit tests
│   ├── test_0001_a_star.py
│   ├── test_0002_bfs_grid.py
│   ├── test_0003_dijkstra.py
│   ├── test_0004_priority_queue.py
│   └── test_0005_minimax.py
└── algorithms/                # Legacy study notes and examples
```

## How to Run Tests

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -q

# Run a specific test file
pytest tests/test_0001_a_star.py -q
```

## Usage

1. Browse `problems/agents/` and read the `.md` file for the problem statement, examples, and approach.
2. Study or extend the matching implementation under `implementations/python/`.
3. Run the tests with `pytest` to verify correctness.
4. Use `templates/problem-template.md` and `templates/solution-template.py` when adding new problems.
5. See `LEARNING_PLAN.md` for the suggested weekly study schedule.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for commit style and contribution guidelines.