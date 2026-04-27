"""
0005 – Minimax — Tic-Tac-Toe
==============================
Problem: Return the best move for the current player using Minimax
         on a 3x3 Tic-Tac-Toe board.
Source:  custom
Difficulty: Medium
Topics: game-tree, minimax, adversarial-search

Time  complexity: O(9!) in the worst case (in practice much less due to pruning)
Space complexity: O(9) recursion depth
"""

from __future__ import annotations

from typing import List, Optional, Tuple

Board = List[List[str]]  # 3x3, cells: "X", "O", or " "


def _check_winner(board: Board) -> Optional[str]:
    """Return "X", "O", or None (no winner yet)."""
    lines = [
        # rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # cols
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for line in lines:
        vals = [board[r][c] for r, c in line]
        if vals[0] != " " and vals[0] == vals[1] == vals[2]:
            return vals[0]
    return None


def _is_full(board: Board) -> bool:
    return all(board[r][c] != " " for r in range(3) for c in range(3))


def _minimax(
    board: Board,
    is_maximising: bool,
) -> Tuple[int, Optional[Tuple[int, int]]]:
    """Return (score, best_move) for the current board state.

    X is the maximising player (+1), O is the minimising player (-1).
    Draw = 0.  best_move is None at terminal nodes.
    """
    winner = _check_winner(board)
    if winner == "X":
        return 1, None
    if winner == "O":
        return -1, None
    if _is_full(board):
        return 0, None

    best_move: Optional[Tuple[int, int]] = None

    if is_maximising:
        best_score = -2  # below possible minimum
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score, _ = _minimax(board, False)
                    board[r][c] = " "
                    if score > best_score:
                        best_score, best_move = score, (r, c)
    else:
        best_score = 2  # above possible maximum
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score, _ = _minimax(board, True)
                    board[r][c] = " "
                    if score < best_score:
                        best_score, best_move = score, (r, c)

    return best_score, best_move


def best_move(board: Board, player: str) -> Optional[Tuple[int, int]]:
    """Return the best (row, col) move for *player* on *board*.

    *player* must be "X" (maximising) or "O" (minimising).
    Returns None if the board is already terminal.

    Examples:
        >>> b = [["X","X"," "],["O","O"," "],[" "," "," "]]
        >>> best_move(b, "X")
        (0, 2)
    """
    is_max = player == "X"
    _, move = _minimax(board, is_max)
    return move


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # X can win in one move
    _board: Board = [
        ["X", "X", " "],
        ["O", "O", " "],
        [" ", " ", " "],
    ]
    move = best_move(_board, "X")
    print("Best move for X:", move)  # (0, 2)

    # Empty board — X picks a cell
    _empty: Board = [[" "] * 3 for _ in range(3)]
    print("First move for X:", best_move(_empty, "X"))
