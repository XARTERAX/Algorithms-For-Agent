"""Tests for 0001_a_star.py"""

import importlib.util
import os

_spec = importlib.util.spec_from_file_location(
    "a_star",
    os.path.join(os.path.dirname(__file__), "..", "implementations", "python", "0001_a_star.py"),
)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
AStarPathfinder = _mod.AStarPathfinder


def test_path_around_wall() -> None:
    """A* should find a path around a wall row."""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    pf = AStarPathfinder()
    path = pf.find_path(grid, (0, 0), (2, 2))
    assert path is not None
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    # Every step must be adjacent
    for i in range(len(path) - 1):
        dr = abs(path[i + 1][0] - path[i][0])
        dc = abs(path[i + 1][1] - path[i][1])
        assert dr + dc == 1


def test_start_is_wall_returns_none() -> None:
    """If start is a wall, return None."""
    grid = [[1]]
    pf = AStarPathfinder()
    assert pf.find_path(grid, (0, 0), (0, 0)) is None


def test_goal_is_wall_returns_none() -> None:
    """If goal is a wall, return None."""
    grid = [[0, 1]]
    pf = AStarPathfinder()
    assert pf.find_path(grid, (0, 0), (0, 1)) is None


def test_start_equals_goal() -> None:
    """When start == goal the path should contain only that cell."""
    grid = [[0, 0], [0, 0]]
    pf = AStarPathfinder()
    path = pf.find_path(grid, (1, 1), (1, 1))
    assert path == [(1, 1)]


def test_no_path_returns_none() -> None:
    """Completely blocked grid should return None."""
    grid = [
        [0, 1],
        [1, 0],
    ]
    pf = AStarPathfinder()
    assert pf.find_path(grid, (0, 0), (1, 1)) is None


def test_open_grid_shortest_path() -> None:
    """On a fully open grid the shortest Manhattan path length is returned."""
    grid = [[0] * 5 for _ in range(5)]
    pf = AStarPathfinder()
    path = pf.find_path(grid, (0, 0), (4, 4))
    assert path is not None
    # Manhattan distance from (0,0) to (4,4) is 8; path has 9 cells
    assert len(path) == 9
