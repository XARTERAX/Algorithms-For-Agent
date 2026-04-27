"""
Problem ID : 0005
Title      : Minimax for Tic-Tac-Toe
Difficulty : Medium
Topics     : game-ai, minimax, recursion
Date       : 2024-01-01
"""

from typing import List, Optional, Tuple

Board = List[List[str]]  # 3×3 grid; cells are "X", "O", or ""


def _check_winner(board: Board) -> Optional[str]:
    """Return "X", "O", or None."""
    lines = (
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
    )
    for line in lines:
        values = [board[r][c] for r, c in line]
        if values[0] and values[0] == values[1] == values[2]:
            return values[0]
    return None


def _is_full(board: Board) -> bool:
    return all(board[r][c] != "" for r in range(3) for c in range(3))


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
                if board[r][c] == "":
                    board[r][c] = "X"
                    score = _minimax(board, False)
                    board[r][c] = ""
                    best = max(best, score)
        return best
    else:
        best = 2
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    score = _minimax(board, True)
                    board[r][c] = ""
                    best = min(best, score)
        return best


def best_move(board: Board, player: str) -> Optional[Tuple[int, int]]:
    """
    Return the optimal (row, col) move for *player* on *board*.

    Args:
        board  : 3×3 list of lists; cells are "X", "O", or "".
        player : "X" (maximiser) or "O" (minimiser).

    Returns:
        (row, col) of the best move, or None if no move is available.

    Time:  O(9!) in the worst case (first move on an empty board)
    Space: O(9)  recursion depth
    """
    is_maximising = player == "X"
    best_score = -2 if is_maximising else 2
    move: Optional[Tuple[int, int]] = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = player
                score = _minimax(board, not is_maximising)
                board[r][c] = ""
                if is_maximising and score > best_score:
                    best_score, move = score, (r, c)
                elif not is_maximising and score < best_score:
                    best_score, move = score, (r, c)

    return move


# ---------------------------------------------------------------------------
# Smoke-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # X can win immediately at (1,2)
    board = [
        ["X", "O", "X"],
        ["O", "O", ""],
        ["X", "", ""],
    ]
    mv = best_move(board, "X")
    print("Best move for X:", mv)
    assert mv == (1, 2), f"Expected (1,2) but got {mv}"
    print("Smoke-test passed.")
