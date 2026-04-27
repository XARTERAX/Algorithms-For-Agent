"""Tests for A* pathfinding (0001_a_star.py)."""

import importlib.util
import os
import sys

import pytest

# Load module with digit-prefixed filename
_IMPL_DIR = os.path.join(os.path.dirname(__file__), "..", "implementations", "python")
_spec = importlib.util.spec_from_file_location(
    "a_star", os.path.join(_IMPL_DIR, "0001_a_star.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
find_path = _mod.find_path
pathfind = _mod.pathfind


@pytest.fixture
def open_grid():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


@pytest.fixture
def wall_grid():
    # Wall in the middle column
    return [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]


def test_same_start_and_goal(open_grid):
    path = find_path(open_grid, (0, 0), (0, 0))
    assert path == [(0, 0)]


def test_direct_path(open_grid):
    path = find_path(open_grid, (0, 0), (0, 2))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (0, 2)
    assert len(path) == 3  # shortest: (0,0)→(0,1)→(0,2)


def test_path_around_wall(wall_grid):
    path = find_path(wall_grid, (0, 0), (0, 2))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (0, 2)
    # Must go around the wall via row 2: 6 steps → 7 cells
    assert len(path) == 7


def test_no_path_blocked():
    grid = [
        [0, 1],
        [1, 0],
    ]
    assert find_path(grid, (0, 0), (1, 1)) is None


def test_blocked_start():
    grid = [[1, 0], [0, 0]]
    assert find_path(grid, (0, 0), (1, 1)) is None


def test_blocked_goal():
    grid = [[0, 0], [0, 1]]
    assert find_path(grid, (0, 0), (1, 1)) is None


def test_pathfind_interface(open_grid):
    """Agent framework interface should also work."""
    path = pathfind((0, 0), (2, 2), open_grid)
    assert path is not None
    assert path[-1] == (2, 2)
