"""
0005 – Minimax for Tic-Tac-Toe
================================
Topic      : agents / game AI
Difficulty : Medium

Problem
-------
Use the Minimax algorithm to find the optimal score and best move for the
current player on a 3×3 Tic-Tac-Toe board.
  'X' is the maximising player (+1 wins).
  'O' is the minimising player (-1 wins).
  ''  is an empty cell.

Examples
--------
>>> board = [['X','O','X'],['O','X','O'],['','','']]
>>> best_move(board)
(2, 1)

Complexity
----------
Time : O(9!) worst case ≈ 362 880 — acceptable for 3×3
Space: O(9) call-stack depth
"""

import math
from typing import List, Optional, Tuple

Board = List[List[str]]


def _check_winner(board: Board) -> Optional[str]:
    """Return 'X', 'O', or None (no winner yet)."""
    lines = (
        # rows
        [board[r] for r in range(3)]
        # cols
        + [[board[r][c] for r in range(3)] for c in range(3)]
        # diagonals
        + [[board[0][0], board[1][1], board[2][2]]]
        + [[board[0][2], board[1][1], board[2][0]]]
    )
    for line in lines:
        if line[0] != "" and line[0] == line[1] == line[2]:
            return line[0]
    return None


def _is_full(board: Board) -> bool:
    return all(board[r][c] != "" for r in range(3) for c in range(3))


def minimax(board: Board, is_maximising: bool) -> int:
    """Return the minimax score for the current board position.

    Parameters
    ----------
    board : Board
        3×3 list of 'X', 'O', or ''.
    is_maximising : bool
        True if it is X's turn (maximiser), False for O (minimiser).

    Returns
    -------
    int
        +1 if X wins, -1 if O wins, 0 for draw — all with perfect play.
    """
    winner = _check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if _is_full(board):
        return 0

    if is_maximising:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "X"
                    best = max(best, minimax(board, False))
                    board[r][c] = ""
        return int(best)
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    best = min(best, minimax(board, True))
                    board[r][c] = ""
        return int(best)


def best_move(board: Board) -> Optional[Tuple[int, int]]:
    """Return the optimal (row, col) move for X (maximising player).

    Returns None if the board is already terminal.
    """
    if _check_winner(board) is not None or _is_full(board):
        return None

    best_score = -math.inf
    move: Optional[Tuple[int, int]] = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "X"
                score = minimax(board, False)
                board[r][c] = ""
                if score > best_score:
                    best_score = score
                    move = (r, c)
    return move


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    board: Board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["", "", ""],
    ]
    print("Best move for X:", best_move(board))  # (2, 1) — X wins

    empty: Board = [[""] * 3 for _ in range(3)]
    print("Score (empty board, perfect play):", minimax(empty, True))  # 0 (draw)
