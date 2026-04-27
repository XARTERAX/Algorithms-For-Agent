"""
Problem ID: 0005
Title: Minimax — Tic-Tac-Toe
Difficulty: Medium
Topics: game-ai, search, recursion, agent

Minimax algorithm for optimal play in Tic-Tac-Toe.
'X' is the maximising player; 'O' is the minimising player.
"""
from typing import Optional

Board = list[list[Optional[str]]]


def _check_winner(board: Board) -> Optional[str]:
    """Return 'X', 'O', or None (no winner yet)."""
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
        if vals[0] and vals[0] == vals[1] == vals[2]:
            return vals[0]
    return None


def _is_full(board: Board) -> bool:
    return all(board[r][c] is not None for r in range(3) for c in range(3))


def _minimax(board: Board, is_maximising: bool) -> int:
    winner = _check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if _is_full(board):
        return 0

    if is_maximising:
        best = -2
        for r in range(3):
            for c in range(3):
                if board[r][c] is None:
                    board[r][c] = "X"
                    best = max(best, _minimax(board, False))
                    board[r][c] = None
        return best
    else:
        best = 2
        for r in range(3):
            for c in range(3):
                if board[r][c] is None:
                    board[r][c] = "O"
                    best = min(best, _minimax(board, True))
                    board[r][c] = None
        return best


def best_move(board: Board, player: str) -> Optional[tuple[int, int]]:
    """
    Find the optimal move for *player* using Minimax.

    Args:
        board:  3×3 list; cells are 'X', 'O', or None.
        player: 'X' (maximiser) or 'O' (minimiser).

    Returns:
        (row, col) of the best move, or None if no moves available.

    Time:  O(9!) worst case  Space: O(9) call stack
    """
    is_maximising = player == "X"
    best_score = -2 if is_maximising else 2
    move: Optional[tuple[int, int]] = None

    for r in range(3):
        for c in range(3):
            if board[r][c] is None:
                board[r][c] = player
                score = _minimax(board, not is_maximising)
                board[r][c] = None
                if is_maximising and score > best_score:
                    best_score = score
                    move = (r, c)
                elif not is_maximising and score < best_score:
                    best_score = score
                    move = (r, c)
    return move


if __name__ == "__main__":
    # X can win by playing (2, 1)
    b: Board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        [None, None, None],
    ]
    print(best_move(b, "X"))  # (2, 1)
