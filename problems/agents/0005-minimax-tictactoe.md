---
title: "Minimax for Tic-Tac-Toe"
id: 0005
source: ""
difficulty: "Medium"
topics: ["game-ai", "minimax", "recursion"]
languages: ["python"]
time_complexity: "O(b^d) — b = branching factor, d = depth"
space_complexity: "O(d)"
date: 2024-01-01
---

# Problem

Implement the **Minimax** algorithm to find the optimal move for a Tic-Tac-Toe player.

- Board is 3×3; cells are `"X"`, `"O"`, or `""` (empty).
- `"X"` is the **maximising** player (wants score +1).
- `"O"` is the **minimising** player (wants score -1).
- A draw scores 0.

Given a board state and whose turn it is, return the best move `(row, col)` for the current player.

## Examples

**Example 1 — X must block or win**
```
X O X
O O _
X _ _
```
- Input: `board` as above, `player="X"`
- Output: `(1, 2)` — X wins on the next move.

**Example 2 — empty board**
- `player="X"` on an empty board.
- Output: any corner or centre (all are optimal by symmetry).

## Constraints

- Board is always a valid, non-terminal Tic-Tac-Toe state.
- The function must return `None` if no moves are available.

# Approach

## Brute Force

Try all moves, evaluate the resulting board, pick the best — this *is* minimax, but without pruning.

## Optimized Idea

1. **Terminal test**: return +1 / -1 / 0 if the game is over.
2. **Maximiser (X)**: pick the move with the highest minimax value among children.
3. **Minimiser (O)**: pick the move with the lowest minimax value among children.

```
minimax(board, is_maximising):
    if terminal(board): return score(board)
    if is_maximising:
        best = -inf
        for move in empty_cells:
            apply move (X)
            best = max(best, minimax(board, False))
            undo move
        return best
    else:
        best = +inf
        for move in empty_cells:
            apply move (O)
            best = min(best, minimax(board, True))
            undo move
        return best
```

## Complexity Analysis

| | Time | Space |
|---|---|---|
| Minimax (3×3) | O(9!) ≈ O(362 880) | O(9) |
| Alpha-Beta | O(b^(d/2)) | O(d) |

For 3×3 Tic-Tac-Toe the tree is small enough that plain minimax finishes instantly.

# Implementation (Python)

```python
# See implementations/python/0005_minimax.py
```

# 3-Line Recap

1. **Key idea**: Recursively assign scores to game states and choose the move that maximises (or minimises) the score depending on whose turn it is.
2. **Why it works**: Tic-Tac-Toe is a finite, perfect-information, zero-sum game; minimax explores the complete game tree and returns the optimal strategy.
3. **Pitfalls / edge cases**: Always undo moves after recursion (or use board copies); return `None` from `best_move` when the board is already terminal.
