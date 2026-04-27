"""Tests for 0005_minimax.py"""

import importlib.util
import os

_spec = importlib.util.spec_from_file_location(
    "minimax",
    os.path.join(os.path.dirname(__file__), "..", "implementations", "python", "0005_minimax.py"),
)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
minimax = _mod.minimax
best_move = _mod.best_move
_check_winner = _mod._check_winner


def _empty_board():
    return [[""] * 3 for _ in range(3)]


def test_empty_board_is_draw() -> None:
    """With perfect play, an empty board should result in a draw (score=0)."""
    board = _empty_board()
    assert minimax(board, is_maximising=True) == 0


def test_x_wins_immediately() -> None:
    """Board where X can win — best_move should pick the winning cell."""
    board = [
        ["X", "X", ""],
        ["O", "O", ""],
        ["", "", ""],
    ]
    # It is X's turn; X should win (completing the top row)
    move = best_move(board)
    assert move is not None
    r, c = move
    board[r][c] = "X"
    assert _check_winner(board) == "X"


def test_full_draw_board() -> None:
    """A full board with no winner should score 0."""
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    assert minimax(board, is_maximising=True) == 0


def test_o_wins() -> None:
    """A board where O already has three in a row scores -1."""
    board = [
        ["O", "O", "O"],
        ["X", "X", ""],
        ["", "", ""],
    ]
    assert minimax(board, is_maximising=True) == -1


def test_x_wins_score() -> None:
    """A board where X already has three in a row scores +1."""
    board = [
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""],
    ]
    assert minimax(board, is_maximising=False) == 1


def test_best_move_returns_none_on_terminal() -> None:
    """best_move on a finished board should return None."""
    board = [
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""],
    ]
    assert best_move(board) is None

