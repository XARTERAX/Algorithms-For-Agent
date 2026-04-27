# Contributing

Welcome! This guide explains how to add new problems, implementations, and tests.

## Adding a New Problem

1. **Create the problem doc**
   ```
   cp templates/problem-template.md problems/<topic>/XXXX-short-name.md
   ```
   Fill in every section: Problem, Examples, Brute Force, Optimized Idea, Pseudocode, Implementation, Tests, Recap.

2. **Create the implementation**
   ```
   cp templates/solution-template.py implementations/python/XXXX_short_name.py
   ```
   Implement `solution(...)` and the `__main__` smoke test.

3. **Create the tests**
   Create `tests/test_XXXX_short_name.py` with at least:
   - One test for the basic/happy-path case.
   - One test for an edge case (empty input, single element, etc.).

4. **Register the problem**
   Add a row to `problems/index.md`:
   ```
   | XXXX | Short Name | topic | Easy/Medium/Hard | ✅ |
   ```

5. **Run tests locally**
   ```bash
   pip install -r requirements.txt
   pytest tests/ -v
   ```

## Code Style

- Python files follow [PEP 8](https://peps.python.org/pep-0008/).
- We use `black` for formatting and `flake8` for linting.
- Install pre-commit hooks: `pip install pre-commit && pre-commit install`.

## Commit Messages

Use the format: `[topic] short description`, e.g., `[agents] add 0006-flood-fill`.

## File Naming Convention

| File type | Format | Example |
|-----------|--------|---------|
| Problem doc | `XXXX-short-name.md` | `0001-a_star.md` |
| Implementation | `XXXX_short_name.py` | `0001_a_star.py` |
| Test file | `test_XXXX_short_name.py` | `test_0001_a_star.py` |
