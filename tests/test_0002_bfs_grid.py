"""Tests for 0002 – BFS on Grid."""

import importlib.util
import os

_HERE = os.path.dirname(__file__)
_IMPL = os.path.join(_HERE, "..", "implementations", "python", "0002_bfs_grid.py")

spec = importlib.util.spec_from_file_location("_bfs_grid", _IMPL)
_mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(_mod)  # type: ignore[union-attr]

bfs_grid = _mod.bfs_grid


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_basic_path():
    """Simple 3x3 grid with one obstacle."""
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert bfs_grid(grid, (0, 0), (2, 2)) == 4


def test_direct_path():
    """No obstacles, straight path."""
    grid = [[0, 0, 0]]
    assert bfs_grid(grid, (0, 0), (0, 2)) == 2


def test_blocked():
    """Goal completely surrounded by obstacles."""
    grid = [[0, 1], [1, 0]]
    assert bfs_grid(grid, (0, 0), (1, 1)) == -1


def test_start_equals_goal():
    """Distance from a cell to itself is 0."""
    grid = [[0, 0], [0, 0]]
    assert bfs_grid(grid, (1, 1), (1, 1)) == 0


def test_single_cell():
    """1x1 grid: start == goal."""
    grid = [[0]]
    assert bfs_grid(grid, (0, 0), (0, 0)) == 0


def test_larger_grid():
    """10x10 open grid: Manhattan distance = optimal."""
    size = 10
    grid = [[0] * size for _ in range(size)]
    assert bfs_grid(grid, (0, 0), (size - 1, size - 1)) == 2 * (size - 1)
