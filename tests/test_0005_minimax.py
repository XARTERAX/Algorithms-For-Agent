"""Tests for 0005 – Minimax (Tic-Tac-Toe)."""

import importlib.util
import os

_HERE = os.path.dirname(__file__)
_IMPL = os.path.join(_HERE, "..", "implementations", "python", "0005_minimax.py")

spec = importlib.util.spec_from_file_location("_minimax", _IMPL)
_mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(_mod)  # type: ignore[union-attr]

best_move = _mod.best_move
_minimax = _mod._minimax
_check_winner = _mod._check_winner


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def _board(*rows: str):
    """Helper: create a 3x3 board from three 3-char strings."""
    return [[ch for ch in row] for row in rows]


def test_x_wins_in_one():
    """X should complete the top row."""
    b = _board("XX ", "OO ", "   ")
    move = best_move(b, "X")
    assert move == (0, 2)


def test_x_blocks_o():
    """X must block O from winning."""
    b = _board("OO ", "X  ", "   ")
    move = best_move(b, "X")
    assert move == (0, 2)


def test_o_wins_in_one():
    """O should complete the left column."""
    # O has (0,0) and (1,0); X has (0,2) and (1,2); no winner yet
    b = _board("O X", "O X", "   ")
    move = best_move(b, "O")
    assert move == (2, 0)


def test_draw_from_empty():
    """Perfect play from an empty board always leads to a draw."""
    empty = [[" "] * 3 for _ in range(3)]
    score, _ = _minimax(empty, True)
    assert score == 0


def test_terminal_x_win():
    """_minimax returns +1 when X has already won."""
    b = _board("XXX", "OO ", "   ")
    score, move = _minimax(b, False)
    assert score == 1
    assert move is None


def test_terminal_draw():
    """_minimax returns 0 on a full draw board."""
    b = _board("XOX", "XOO", "OXX")
    score, move = _minimax(b, True)
    assert score == 0
    assert move is None


def test_best_move_returns_none_on_terminal():
    """best_move returns None when the game is already over."""
    b = _board("XXX", "OO ", "   ")
    assert best_move(b, "O") is None


def test_check_winner_row():
    assert _check_winner(_board("XXX", "OO ", "   ")) == "X"


def test_check_winner_col():
    assert _check_winner(_board("O  ", "O  ", "O  ")) == "O"


def test_check_winner_diag():
    assert _check_winner(_board("X  ", " X ", "  X")) == "X"


def test_no_winner():
    assert _check_winner(_board("XO ", "OX ", "   ")) is None
