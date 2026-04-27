import importlib.util
import os

_impl_path = os.path.join(
    os.path.dirname(__file__), "..", "implementations", "python", "0005_minimax.py"
)
_spec = importlib.util.spec_from_file_location("minimax", _impl_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
best_move = _mod.best_move


def _board(rows):
    """Helper: build a 3×3 board from a list of row strings ('X','O','.')."""
    mapping = {"X": "X", "O": "O", ".": None}
    return [[mapping[ch] for ch in row] for row in rows]


def test_x_wins_in_one():
    board = _board(["XOX", "OXO", "..."])
    move = best_move(board, "X")
    # X has two diagonals available: (2,0) completes (0,2)-(1,1)-(2,0),
    # (2,2) completes (0,0)-(1,1)-(2,2). Both are winning moves.
    assert move in {(2, 0), (2, 2)}


def test_x_blocks_o_win():
    # O would win at (2,2); X must block
    board = _board(["XO.", ".O.", "..."])
    move = best_move(board, "X")
    assert move == (2, 1)  # block O's column


def test_empty_board_x_picks_valid_move():
    # On an empty board all moves are draws under perfect play;
    # verify that best_move returns some valid cell.
    board = _board(["...", "...", "..."])
    move = best_move(board, "X")
    assert move is not None
    r, c = move
    assert 0 <= r <= 2 and 0 <= c <= 2


def test_no_moves_returns_none():
    board = _board(["XOX", "OXO", "OXO"])
    move = best_move(board, "X")
    assert move is None


def test_o_wins_in_one():
    # O can win at (2,0)
    board = _board(["XOX", "XO.", ".X."])
    move = best_move(board, "O")
    assert move == (2, 0)
