---
title: "Minimax – Tic-Tac-Toe"
id: 0005
source: "custom"
difficulty: "Medium"
topics: ["game-AI", "minimax", "recursion", "agents"]
languages: ["python"]
time_complexity: "O(b^d) brute; O(b^(d/2)) with alpha-beta"
space_complexity: "O(d)"
date: 2026-04-27
---

# Problem

Implement the **Minimax algorithm** to find the optimal move for the current player on a Tic-Tac-Toe board (3×3). The maximising player is `'X'`, the minimising player is `'O'`.

**Input:**
- `board`: `List[List[str]]` — 3×3 grid, cells are `'X'`, `'O'`, or `''` (empty).
- `is_maximising`: `bool` — True if it is X's turn.

**Output:** `int` — score from X's perspective: `+1` (X wins), `-1` (O wins), `0` (draw).  
Also expose `best_move(board) -> Tuple[int,int]` to return the optimal `(row, col)`.

# Examples

```
board = [
  ['X', 'O', 'X'],
  ['O', 'X', 'O'],
  ['', '', ''],
]
is_maximising = True (X's turn)

best_move → (2, 1)   # X wins by playing centre-bottom
```

# Brute Force

Try every possible sequence of moves using DFS and pick the best — already Minimax, O(b^d).

# Optimized Idea (思路链)

1. **Model** — Game tree: each node = board state, children = legal moves.
2. **Brute force recap** — With 9! ≈ 362,880 terminal states, brute force is acceptable; alpha-beta halves depth.
3. **Pattern** — Minimax: X maximises score, O minimises; recurse to terminal states (win/draw/lose).
4. **Key invariant** — At terminal nodes the score is exact. At interior nodes, the current player picks the move that optimises their score.
5. **Pseudocode**

```
minimax(board, is_maximising):
    if terminal(board): return evaluate(board)
    if is_maximising:
        best = -∞
        for move in legal_moves(board):
            make(move); best = max(best, minimax(board, False)); undo(move)
        return best
    else:
        best = +∞
        for move in legal_moves(board):
            make(move); best = min(best, minimax(board, True)); undo(move)
        return best
```

- Time: O(9!) worst case for Tic-Tac-Toe · Space: O(9) call stack depth

# Implementation (Python)

```python
# See implementations/python/0005_minimax.py
```

# Tests

| # | Input | Expected Output | Notes |
|---|-------|-----------------|-------|
| 1 | Empty board | score 0 (draw with perfect play) | both play optimally |
| 2 | One move from X win | best_move returns winning cell | X wins |
| 3 | Full board draw | score 0 | terminal draw |

# Recap (3 lines)

1. **Key idea:** Recursively explore all future moves; X picks the max score, O picks the min, producing the optimal strategy for both players.
2. **Why correct:** With perfect play on Tic-Tac-Toe both players draw; Minimax proves this by exhaustive search.
3. **Complexity:** O(b^d) time (≈ 9! for TTT), O(d) space on the call stack.
