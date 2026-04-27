# Contributing Guide

Thank you for contributing to **Algorithms-For-Agent**!

## Workflow

1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feat/0006-your-algorithm
   ```
2. Follow the templates in `templates/` for new problems and solutions.
3. Add tests in `tests/` that cover at least the sample inputs in the problem `.md`.
4. Run the test suite locally before opening a PR:
   ```bash
   pip install -r requirements.txt
   pytest tests/ -v
   ```
5. Open a pull request against `main` with a descriptive title and description.

## File Naming Conventions

| Artefact | Pattern | Example |
|----------|---------|---------|
| Problem statement | `problems/<topic>/XXXX-short-title.md` | `problems/agents/0001-a_star.md` |
| Implementation | `implementations/python/XXXX_short_title.py` | `implementations/python/0001_a_star.py` |
| Tests | `tests/test_XXXX_short_title.py` | `tests/test_0001_a_star.py` |

## Code Style

- Python code is formatted with **black** and linted with **flake8**.
- Run pre-commit hooks before committing:
  ```bash
  pip install pre-commit
  pre-commit install
  pre-commit run --all-files
  ```

## Problem Template

Use `templates/problem-template.md`. Every problem `.md` must include:
- Front-matter (id, title, difficulty, topics, complexity)
- Problem statement
- Example inputs / outputs
- Brute-force approach
- Optimised approach with pseudocode
- 3-line recap (key idea / complexity / why correct)

## Code of Conduct

Be respectful, constructive, and collaborative.
