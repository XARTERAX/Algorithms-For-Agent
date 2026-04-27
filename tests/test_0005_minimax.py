"""Tests for Minimax Tic-Tac-Toe (0005_minimax.py)."""

import importlib.util
import os

import pytest

_IMPL_DIR = os.path.join(os.path.dirname(__file__), "..", "implementations", "python")
_spec = importlib.util.spec_from_file_location(
    "minimax", os.path.join(_IMPL_DIR, "0005_minimax.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
best_move = _mod.best_move
_winner = _mod._winner


def _board(*rows):
    """Helper: create a 3x3 board from three strings, e.g. 'XO '."""
    mapping = {"X": "X", "O": "O", " ": None}
    return [[mapping[ch] for ch in row] for row in rows]


def test_take_winning_move():
    # X can win by completing the top row
    board = _board("XX ", "O  ", "   ")
    move = best_move(board, "X")
    assert move == (0, 2)


def test_block_opponent_win():
    # O is about to win top row; X must block (0,2)
    board = _board("OO ", "X  ", "   ")
    move = best_move(board, "X")
    assert move == (0, 2)


def test_full_board_returns_none():
    board = _board("XOX", "OXO", "OXO")
    assert best_move(board, "X") is None


def test_winner_detection_row():
    board = _board("XXX", "OO ", "   ")
    assert _winner(board) == "X"


def test_winner_detection_col():
    board = _board("XO ", "XO ", "X  ")
    assert _winner(board) == "X"


def test_winner_detection_diag():
    board = _board("X  ", " X ", "  X")
    assert _winner(board) == "X"


def test_no_winner():
    board = _board("XO ", "OX ", "   ")
    assert _winner(board) is None


def test_optimal_play_draw():
    """From an empty board, minimax should never lose — result is draw."""
    board = _board("   ", "   ", "   ")
    # Simulate game with both players playing optimally
    current = "X"
    for _ in range(9):
        mv = best_move(board, current)
        if mv is None:
            break
        board[mv[0]][mv[1]] = current
        w = _winner(board)
        if w is not None:
            # Optimal play from both sides means no one wins from start
            assert False, f"{w} won but optimal play should draw"
        current = "O" if current == "X" else "X"
