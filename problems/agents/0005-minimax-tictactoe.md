---
title: "Minimax — Tic-Tac-Toe"
id: 0005
source: "game AI"
difficulty: "Medium"
topics: ["game-ai", "search", "recursion", "agent"]
languages: ["python"]
time_complexity: "O(b^d) — b=branching factor, d=depth"
space_complexity: "O(d)"
date: 2026-04-27
---

# Problem

Implement the **Minimax** algorithm to find the optimal move for the current player in a Tic-Tac-Toe game.

Board: 3×3 grid; cells are `'X'`, `'O'`, or `None`.  
`'X'` is the maximising player; `'O'` is the minimising player.

`best_move(board, player)` → `(row, col)` of the optimal move.

# Examples

```
Board (X to move):
  X | O | X
  O | X | O
  _ | _ | _

best_move(board, 'X') → (2, 1)   # centre-bottom wins for X

Board (empty, X to move):
best_move(board, 'X') → (1, 1)   # centre is optimal first move
```

# Brute Force

Enumerate all complete games from the current state — effectively what Minimax does, but without pruning.

# Optimized Idea (思路链)

1. **Model** — game tree: nodes are board states, children are legal moves.
2. **X** tries to maximise the score; **O** tries to minimise it.
3. **Terminal scores**: X wins → +1, O wins → -1, draw → 0.
4. **Invariant** — Minimax value of a state = best reachable outcome under optimal play.
5. **Pseudocode**:

```
def minimax(board, is_maximising):
    winner = check_winner(board)
    if winner == 'X': return +1
    if winner == 'O': return -1
    if board_full(board):  return 0
    if is_maximising:
        return max(minimax(move(board,'X'), False) for move in legal_moves(board))
    else:
        return min(minimax(move(board,'O'), True) for move in legal_moves(board))
```

# Implementation

See `implementations/python/0005_minimax.py`.

# Tests

- X can win in one move — best_move returns the winning cell.
- O can win in one move — best_move blocks (or O wins if O is playing).
- Empty board — returns (1,1) as optimal first move.
- Full board (draw) — minimax returns 0.

# Review (fill in after solving)

- **Key idea**: Recursive game-tree search assuming both players play optimally.
- **Complexity**: time O(9!) ≈ O(b^d) | space O(d) call stack
- **Improvement**: Alpha-Beta pruning reduces effective branching; MCTS scales to larger games.
