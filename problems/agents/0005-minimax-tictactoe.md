---
title: "Minimax Tic-Tac-Toe"
id: 0005
source: "classic"
difficulty: "Medium"
topics: ["agent", "game-ai", "minimax"]
languages: ["python"]
time_complexity: "O(b^d) vanilla; O(b^(d/2)) with alpha-beta"
space_complexity: "O(d)"
date: 2026-04-27
---

# Problem

Implement **Minimax** (with optional alpha-beta pruning) to find the optimal
move for a player in a **Tic-Tac-Toe** game.

**Board representation:** 3×3 list of lists; `'X'`, `'O'`, or `None`.

**Function:** `best_move(board, player)` → `(row, col)` of the optimal move.

**Scoring:** `+1` if `player` wins, `-1` if opponent wins, `0` for draw.

# Examples

**Example 1 — winning move available:**
```
board = [['X', 'X', None],
         ['O', 'O', None],
         [None, None, None]]
player = 'X'
best_move(board, 'X')  # → (0, 2)  # completes top row for X
```

**Example 2 — must block opponent:**
```
board = [['O', 'O', None],
         ['X', None, None],
         [None, None, None]]
player = 'X'
best_move(board, 'X')  # → (0, 2)  # blocks O from winning
```

# Brute Force

Try every possible game tree with DFS — exponential O(9!) ≈ 362 880 for
tic-tac-toe; feasible here but not for complex games.

# Optimized Idea

1. **Model** — game tree: MAX player maximises score, MIN player minimises.
2. **Bottleneck** — exploring every leaf in a deep game tree is slow.
3. **Pattern** — **Alpha-beta pruning**: maintain `alpha` (best score for MAX)
   and `beta` (best score for MIN); prune branches that cannot affect result.
4. **Invariant** — the pruned branches never contain the optimal move.
5. **Complexity** — worst case O(b^d); with alpha-beta ≈ O(b^(d/2)).

# Pseudocode

```
minimax(board, depth, is_max, alpha=-inf, beta=+inf):
    score = evaluate(board)
    if score != 0 or no moves left: return score

    if is_max:
        best = -inf
        for each empty cell:
            place X, recurse minimising
            best = max(best, result)
            alpha = max(alpha, best)
            if beta <= alpha: break  # prune
        return best
    else:
        best = +inf
        for each empty cell:
            place O, recurse maximising
            best = min(best, result)
            beta = min(beta, best)
            if beta <= alpha: break  # prune
        return best
```

# Implementation

```python
# See implementations/python/0005_minimax.py
```

# Tests

```python
# See tests/test_0005_minimax.py
```

# Notes

> **Key idea:** Minimax exhaustively searches the game tree; alpha-beta pruning
> eliminates branches provably worse than already-found options, halving the
> effective depth.  
> **Complexity:** Time O(b^d) worst-case, O(b^(d/2)) with alpha-beta; Space
> O(d) call stack.  
> **Next improvements:** add move ordering (try winning moves first) to maximise
> pruning; extend to connect-four with iterative deepening.
