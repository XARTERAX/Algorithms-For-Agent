from conftest import load_impl

_m = load_impl("0001_a_star.py")
a_star = _m.a_star


def test_simple_path():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    path = a_star((0, 0), (3, 3), grid)
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)
    for r, c in path:
        assert grid[r][c] == 0
    for i in range(len(path) - 1):
        dr = abs(path[i + 1][0] - path[i][0])
        dc = abs(path[i + 1][1] - path[i][1])
        assert dr + dc == 1


def test_no_path():
    grid = [[0, 1], [1, 0]]
    assert a_star((0, 0), (1, 1), grid) == []


def test_start_equals_goal():
    grid = [[0, 0], [0, 0]]
    path = a_star((0, 0), (0, 0), grid)
    assert path == [(0, 0)]


def test_single_cell_grid():
    grid = [[0]]
    assert a_star((0, 0), (0, 0), grid) == [(0, 0)]


def test_custom_heuristic():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    path = a_star((0, 0), (2, 2), grid, heuristic=lambda a, b: 0)
    assert path[0] == (0, 0) and path[-1] == (2, 2)
