from conftest import load_impl

_m = load_impl("0002_bfs_grid.py")
bfs_grid = _m.bfs_grid


def test_simple_path():
    grid = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
    ]
    path = bfs_grid((0, 0), (2, 3), grid)
    assert path[0] == (0, 0)
    assert path[-1] == (2, 3)
    for r, c in path:
        assert grid[r][c] == 0
    for i in range(len(path) - 1):
        dr = abs(path[i + 1][0] - path[i][0])
        dc = abs(path[i + 1][1] - path[i][1])
        assert dr + dc == 1


def test_no_path():
    grid = [[0, 1], [1, 0]]
    assert bfs_grid((0, 0), (1, 1), grid) == []


def test_start_equals_goal():
    grid = [[0, 0], [0, 0]]
    assert bfs_grid((1, 1), (1, 1), grid) == [(1, 1)]


def test_shortest_path_length():
    # Open 3x3 grid: shortest path from (0,0) to (2,2) is 4 steps = 5 cells
    grid = [[0] * 3 for _ in range(3)]
    path = bfs_grid((0, 0), (2, 2), grid)
    assert len(path) == 5
