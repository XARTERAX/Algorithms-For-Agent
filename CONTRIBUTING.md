# Contributing Guide

Thank you for contributing to **Algorithms-For-Agent**!

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Adding a New Problem

1. Copy `templates/problem-template.md` → `problems/<topic>/<id>-<short-name>.md` and fill in all sections.
2. Copy `templates/solution-template.py` → `implementations/python/<id>_<short_name>.py` and implement.
3. Add a minimal pytest file under `tests/test_<id>_<short_name>.py`.
4. Add a row to `problems/index.md`.

## Commit Style

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short summary>

Types: feat | fix | docs | test | refactor | chore
```

Examples:
- `feat(agents): add 0006 iterative deepening`
- `fix(a_star): handle diagonal movement cost`
- `docs(complexity.md): add heap operations table`
- `test(dijkstra): add disconnected graph case`

## Code Style

- Python: formatted with **black** (line length 88), linted with **flake8**.
- Run `pre-commit run --all-files` before pushing.

## Pull Requests

- One problem or feature per PR.
- Ensure `pytest -q` passes with no errors before opening a PR.
- Add a brief description of the algorithm and why it is relevant to Agent/DMT demos.
