from conftest import load_impl

_m = load_impl("0005_minimax.py")
best_move = _m.best_move
_check_winner = _m._check_winner


def _empty_board():
    return [["", "", ""], ["", "", ""], ["", "", ""]]


def test_x_wins_immediately():
    # X can complete a row at (1, 2)
    board = [
        ["X", "O", "X"],
        ["O", "O", ""],
        ["X", "", ""],
    ]
    assert best_move(board, "X") == (1, 2)


def test_o_blocks_x():
    # O must block X from winning at (0, 2)
    board = [
        ["X", "X", ""],
        ["O", "", ""],
        ["", "", ""],
    ]
    assert best_move(board, "O") == (0, 2)


def test_no_move_on_full_board():
    board = [
        ["X", "O", "X"],
        ["X", "X", "O"],
        ["O", "X", "O"],
    ]
    assert best_move(board, "X") is None


def test_draw_from_empty():
    # Both players play optimally from empty board — result must be a draw
    board = _empty_board()
    # Simulate both players playing optimally
    player = "X"
    for _ in range(9):
        winner = _check_winner(board)
        if winner or all(board[r][c] != "" for r in range(3) for c in range(3)):
            break
        mv = best_move(board, player)
        if mv is None:
            break
        board[mv[0]][mv[1]] = player
        player = "O" if player == "X" else "X"
    assert _check_winner(board) is None  # draw
