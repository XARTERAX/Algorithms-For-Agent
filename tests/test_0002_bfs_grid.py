"""Tests for BFS grid shortest path (0002_bfs_grid.py)."""

import importlib.util
import os

import pytest

_IMPL_DIR = os.path.join(os.path.dirname(__file__), "..", "implementations", "python")
_spec = importlib.util.spec_from_file_location(
    "bfs_grid", os.path.join(_IMPL_DIR, "0002_bfs_grid.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
find_path = _mod.find_path
pathfind = _mod.pathfind


@pytest.fixture
def open_grid():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_same_start_and_goal(open_grid):
    path = find_path(open_grid, (1, 1), (1, 1))
    assert path == [(1, 1)]


def test_shortest_path(open_grid):
    path = find_path(open_grid, (0, 0), (0, 2))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (0, 2)
    assert len(path) == 3


def test_path_around_wall():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    path = find_path(grid, (0, 0), (0, 2))
    assert path is not None
    assert path[-1] == (0, 2)
    # shortest detour: down 2, right 2, up 2 = 6 steps → 7 cells
    assert len(path) == 7


def test_no_path():
    grid = [[0, 1], [1, 0]]
    assert find_path(grid, (0, 0), (1, 1)) is None


def test_blocked_start():
    grid = [[1, 0], [0, 0]]
    assert find_path(grid, (0, 0), (1, 1)) is None


def test_pathfind_interface(open_grid):
    path = pathfind((0, 0), (2, 2), open_grid)
    assert path is not None
    assert path[-1] == (2, 2)
