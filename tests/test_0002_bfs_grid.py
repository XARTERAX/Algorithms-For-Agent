"""Tests for 0002_bfs_grid.py"""

import importlib.util
import os

_spec = importlib.util.spec_from_file_location(
    "bfs_grid",
    os.path.join(os.path.dirname(__file__), "..", "implementations", "python", "0002_bfs_grid.py"),
)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
BFSPathfinder = _mod.BFSPathfinder


def test_path_around_wall() -> None:
    """BFS should find shortest path around a wall."""
    grid = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0],
    ]
    pf = BFSPathfinder()
    path = pf.find_path(grid, (0, 0), (2, 2))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    # Every step is adjacent
    for i in range(len(path) - 1):
        dr = abs(path[i + 1][0] - path[i][0])
        dc = abs(path[i + 1][1] - path[i][1])
        assert dr + dc == 1


def test_no_path_returns_none() -> None:
    """Blocked grid should return None."""
    grid = [
        [0, 1],
        [1, 0],
    ]
    pf = BFSPathfinder()
    assert pf.find_path(grid, (0, 0), (1, 1)) is None


def test_start_equals_goal() -> None:
    """start == goal returns single-element path."""
    grid = [[0, 0], [0, 0]]
    pf = BFSPathfinder()
    path = pf.find_path(grid, (0, 0), (0, 0))
    assert path == [(0, 0)]


def test_start_wall_returns_none() -> None:
    grid = [[1, 0]]
    pf = BFSPathfinder()
    assert pf.find_path(grid, (0, 0), (0, 1)) is None


def test_goal_wall_returns_none() -> None:
    grid = [[0, 1]]
    pf = BFSPathfinder()
    assert pf.find_path(grid, (0, 0), (0, 1)) is None


def test_open_grid_path_length() -> None:
    """On a 4×4 open grid from (0,0) to (3,3) the path should have length 7."""
    grid = [[0] * 4 for _ in range(4)]
    pf = BFSPathfinder()
    path = pf.find_path(grid, (0, 0), (3, 3))
    assert path is not None
    assert len(path) == 7
