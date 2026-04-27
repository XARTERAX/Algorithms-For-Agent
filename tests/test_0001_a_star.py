import importlib.util
import os

_impl_path = os.path.join(
    os.path.dirname(__file__), "..", "implementations", "python", "0001_a_star.py"
)
_spec = importlib.util.spec_from_file_location("a_star", _impl_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
find_path = _mod.find_path


def test_simple_path():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    path = find_path(grid, (0, 0), (2, 2))
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    assert len(path) == 5


def test_no_path():
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ]
    assert find_path(grid, (0, 0), (2, 2)) == []


def test_start_equals_goal():
    grid = [[0, 0], [0, 0]]
    assert find_path(grid, (0, 0), (0, 0)) == [(0, 0)]


def test_straight_path():
    grid = [[0, 0, 0, 0]]
    path = find_path(grid, (0, 0), (0, 3))
    assert path == [(0, 0), (0, 1), (0, 2), (0, 3)]


def test_wall_start_or_goal():
    grid = [[1, 0], [0, 0]]
    assert find_path(grid, (0, 0), (1, 1)) == []
    assert find_path(grid, (1, 0), (0, 0)) == []
