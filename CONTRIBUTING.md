# Contributing Guide

Thank you for contributing! Please follow the conventions below to keep the repo consistent.

## Adding a Problem

1. Copy `templates/problem-template.md` to `problems/<topic>/<id>-<slug>.md`.
2. Copy `templates/solution-template.py` to `implementations/python/<id>_<slug>.py`.
3. Add a corresponding test in `tests/test_<id>_<slug>.py`.
4. Register the problem in `problems/index.md`.

## Commit Style

Use short, descriptive commit messages in the imperative mood:

```
add: 0006 implement Bellman-Ford shortest path
fix: 0002 correct BFS queue initialization
docs: update complexity.md with amortized analysis note
test: add edge cases for A* with obstacles
```

Prefixes: `add`, `fix`, `docs`, `test`, `refactor`, `chore`.

## Code Style

- Python 3.10+.
- Format with **black** (`black implementations/ tests/`).
- Lint with **flake8** (max line length 99).
- Keep functions small and well-named; avoid magic numbers.

## Pull Request Checklist

- [ ] Problem `.md` uses the template and includes example I/O.
- [ ] Implementation passes `pytest tests/`.
- [ ] 3-line review written at the bottom of the problem `.md`.
- [ ] `problems/index.md` updated.
