# Algorithms-For-Agent

A personal algorithm & data-structure study space tailored to Digital Media Technology (DMT) and Agent/game-demo development. All implementations are in Python.

## Structure

```
.
├── problems/          # Problem statements by topic
│   ├── agents/        # Agent-focused pathfinding & search problems
│   └── index.md       # Master index table (id, title, topic, difficulty, status)
├── implementations/   # Python implementations
│   └── python/
├── tests/             # pytest unit tests (one file per problem)
├── templates/         # Problem & solution templates
├── docs/              # Concise algorithm notes
├── agent_tasks/       # Agent framework interfaces, MCP notes, task backlog
├── algorithms/        # Existing study notes and prior work
├── LEARNING_PLAN.md   # Detailed 8-week learning plan (separate from this file)
├── requirements.txt
└── .github/workflows/ # CI (pytest on push/PR)
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                           # run all tests
```

## Workflow

1. Pick a problem in `problems/` and read the `.md` for context and pseudocode.
2. Implement or study the solution in `implementations/python/`.
3. Run `pytest tests/` to verify correctness.
4. After solving, add a 3-line review at the bottom of the problem `.md`:
   - Key idea, time/space complexity, possible improvements.

## Learning Plan

The detailed 8-week schedule (tailored to DMT + Agent development) lives in **[LEARNING_PLAN.md](LEARNING_PLAN.md)** — not in this file.

## License

[MIT](LICENSE)