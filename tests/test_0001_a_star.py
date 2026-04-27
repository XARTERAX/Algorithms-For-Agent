"""Tests for 0001 – A* Pathfinding."""

import importlib.util
import os
import sys

_HERE = os.path.dirname(__file__)
_IMPL = os.path.join(_HERE, "..", "implementations", "python", "0001_a_star.py")

spec = importlib.util.spec_from_file_location("_a_star", _IMPL)
_mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(_mod)  # type: ignore[union-attr]

a_star = _mod.a_star


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_simple_open_grid():
    """Shortest path on a 3x3 open grid."""
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    path = a_star(grid, (0, 0), (2, 2))
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    assert len(path) - 1 == 4  # Manhattan distance


def test_path_with_obstacle():
    """Path must detour around a wall."""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    path = a_star(grid, (0, 0), (2, 2))
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    # No cell in the path should be an obstacle
    for r, c in path:
        assert grid[r][c] == 0


def test_no_path_blocked():
    """Return empty list when goal is unreachable."""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ]
    path = a_star(grid, (0, 0), (2, 2))
    assert path == []


def test_start_equals_goal():
    """Trivial case: start == goal → path of length 1."""
    grid = [[0, 0], [0, 0]]
    path = a_star(grid, (0, 0), (0, 0))
    assert path == [(0, 0)]


def test_large_grid_finds_path():
    """A* should work on larger grids."""
    size = 10
    grid = [[0] * size for _ in range(size)]
    path = a_star(grid, (0, 0), (size - 1, size - 1))
    assert path[0] == (0, 0)
    assert path[-1] == (size - 1, size - 1)
    assert len(path) - 1 == 2 * (size - 1)  # optimal = 2*(n-1)
