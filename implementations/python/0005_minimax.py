"""
Problem: Minimax Tic-Tac-Toe
ID: 0005
Difficulty: Medium
Topics: agent, game-ai, minimax

Minimax with alpha-beta pruning for optimal Tic-Tac-Toe play.

Board: 3x3 list of lists — 'X', 'O', or None.

Functions:
    best_move(board, player) -> (row, col)
"""

import math
from typing import List, Optional, Tuple

Board = List[List[Optional[str]]]
Move = Tuple[int, int]

_LINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def _winner(board: Board) -> Optional[str]:
    """Return 'X', 'O', or None."""
    for line in _LINES:
        values = [board[r][c] for r, c in line]
        if values[0] and values[0] == values[1] == values[2]:
            return values[0]
    return None


def _empty_cells(board: Board) -> List[Move]:
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]


def _minimax(
    board: Board,
    depth: int,
    is_maximising: bool,
    maximiser: str,
    minimiser: str,
    alpha: float,
    beta: float,
) -> int:
    """Return the minimax score of the board position."""
    winner = _winner(board)
    if winner == maximiser:
        return 10 - depth
    if winner == minimiser:
        return depth - 10
    empties = _empty_cells(board)
    if not empties:
        return 0

    if is_maximising:
        best = -math.inf
        for r, c in empties:
            board[r][c] = maximiser
            score = _minimax(board, depth + 1, False, maximiser, minimiser, alpha, beta)
            board[r][c] = None
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for r, c in empties:
            board[r][c] = minimiser
            score = _minimax(board, depth + 1, True, maximiser, minimiser, alpha, beta)
            board[r][c] = None
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def best_move(board: Board, player: str) -> Optional[Move]:
    """
    Return the optimal (row, col) move for player using Minimax + alpha-beta.

    Parameters
    ----------
    board  : 3x3 list; cells are 'X', 'O', or None.
    player : 'X' or 'O' — the player whose turn it is.

    Returns
    -------
    (row, col) of the best move, or None if the board is full.
    """
    opponent = "O" if player == "X" else "X"
    empties = _empty_cells(board)
    if not empties:
        return None

    best_score = -math.inf
    move: Optional[Move] = None

    for r, c in empties:
        board[r][c] = player
        score = _minimax(board, 0, False, player, opponent, -math.inf, math.inf)
        board[r][c] = None
        if score > best_score:
            best_score = score
            move = (r, c)

    return move
