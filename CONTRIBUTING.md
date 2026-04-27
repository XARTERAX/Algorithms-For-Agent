# Contributing Guide

Thank you for contributing to **Algorithms-For-Agent**!

---

## How to Add a New Problem

1. Copy `templates/problem-template.md` → `problems/<topic>/<id>-<slug>.md` and fill in all sections.
2. Copy `templates/solution-template.py` → `implementations/python/<id>_<slug>.py` and implement the solution.
3. Add a test file at `tests/test_<id>_<slug>.py` with at least 2 test cases.
4. Add a row to `problems/index.md`.

## Commit Style

Use short, descriptive commit messages in imperative mood:

```
feat: add 0006 bellman-ford implementation
fix: correct off-by-one in bfs grid boundary check
docs: update complexity.md with amortized analysis
test: add edge-case for empty grid in a_star
```

Prefixes: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.

## Code Style

- Python 3.9+.
- Format with **black** (`black .`).
- Lint with **flake8** (`flake8 .`).
- Type hints encouraged but not required.

## Pull Request Checklist

- [ ] New `.md` follows `templates/problem-template.md`.
- [ ] Implementation exports the documented function signature.
- [ ] Tests pass locally (`pytest -q`).
- [ ] `problems/index.md` updated.
