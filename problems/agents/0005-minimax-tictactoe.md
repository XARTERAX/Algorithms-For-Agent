---
title: "Minimax — Tic-Tac-Toe"
id: 0005
source: "custom"
difficulty: "Medium"
topics: ["game-tree", "minimax", "adversarial-search"]
languages: ["python"]
time_complexity: "O(b^d) where b=branching factor, d=depth"
space_complexity: "O(d)"
date: 2026-04-27
---

# Problem

Implement the **Minimax** algorithm for a 3×3 Tic-Tac-Toe board.  
Given a board state and whose turn it is, return the **best move** (row, col) for the current player assuming both players play optimally.

`X` is the maximising player (score +1 for X win), `O` is the minimising player (score -1 for O win), draw = 0.

## Examples

```
Input (X to move, one move from winning):
  board = [["X", "X", " "],
           ["O", "O", " "],
           [" ", " ", " "]]

Output: (0, 2)   # X plays top-right to win immediately
```

## Constraints

- Board is always a valid 3×3 Tic-Tac-Toe position.
- The function is called only when there are empty cells and no winner yet.

---

# Brute Force

Enumerate all possible continuations recursively — which is exactly what Minimax does.  
Since the board has at most 9! ≈ 362 880 terminal paths, exhaustive search is feasible without pruning.

---

# Optimised Idea (思路链)

1. **Model:** The game is a finite, two-player, zero-sum game → game tree where each node is a board state.
2. **Players:** MAX (X) wants to maximise score; MIN (O) wants to minimise score.
3. **Pattern:** Minimax recursively evaluates all moves:
   - At MAX nodes: choose the child with the highest value.
   - At MIN nodes: choose the child with the lowest value.
4. **Base cases:** Terminal positions (win / lose / draw) have known scores.
5. **Key invariant:** The value backed up to each node is the score achievable with optimal play from both sides.

### Pseudocode

```
minimax(board, is_maximising):
    if terminal(board):
        return score(board), None

    if is_maximising:
        best_score = -∞
        for each empty cell (r, c):
            place X at (r, c)
            score, _ = minimax(board, False)
            undo move
            if score > best_score:
                best_score, best_move = score, (r, c)
        return best_score, best_move
    else:
        best_score = +∞
        for each empty cell (r, c):
            place O at (r, c)
            score, _ = minimax(board, True)
            undo move
            if score < best_score:
                best_score, best_move = score, (r, c)
        return best_score, best_move
```

---

# Implementation

```python
# See implementations/python/0005_minimax.py
```

---

# Tests

```python
# See tests/test_0005_minimax.py
```

---

# 3-Line Recap

1. **Key idea:** Minimax exhaustively explores the game tree, alternating between maximising and minimising players, backing up the optimal value to each node.
2. **Complexity:** O(b^d) time, O(d) stack space; for 3×3 Tic-Tac-Toe b≤9, d≤9, so ≤362 880 nodes — trivially fast.
3. **Why correct:** Under the assumption of optimal play by both sides, the backed-up value at the root equals the game-theoretic value of the position.
