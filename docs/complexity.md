# Algorithm Complexity Reference

## Big-O Intuition

| Notation | Name | Example algorithm |
|----------|------|-------------------|
| O(1) | Constant | Array index lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear scan |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Bubble sort, naïve A\* on dense grid |
| O(2ⁿ) | Exponential | Naïve minimax without pruning |
| O(n!) | Factorial | Brute-force permutations |

## Rules of Thumb

1. **Drop constants**: O(3n) → O(n).
2. **Keep the dominant term**: O(n² + n) → O(n²).
3. **Nested loops** → multiply: two nested loops over n → O(n²).
4. **Divide & Conquer** → T(n) = aT(n/b) + O(n^d); apply Master Theorem.
5. **Recursion depth** contributes to *space* complexity (call stack).

## Space Complexity

- Count extra memory allocated (excluding input).
- Recursion depth = O(depth) stack frames.
- BFS/A\* frontier = O(V) in the worst case.

## Complexity of Key Agent Algorithms

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| BFS (grid, V nodes) | O(V + E) | O(V) | E = edges = 4V for 4-connect grid |
| DFS | O(V + E) | O(V) | Stack depth = path length |
| Dijkstra (binary heap) | O((V + E) log V) | O(V) | Non-negative weights only |
| A\* | O(E log V) best case | O(V) | Depends on heuristic quality |
| Minimax (depth d, branching b) | O(b^d) | O(d) | Alpha-Beta prunes to O(b^(d/2)) |
| MCTS (n iterations) | O(n · depth) | O(n · branching) | Approximation |
| Heapq push/pop | O(log n) | O(n) | Python `heapq` module |

## Amortized Analysis (brief)

- **Dynamic array** (Python list): append is O(1) amortized — O(n) copy happens
  rarely enough that the average cost per append is still O(1).
- **Union-Find with path compression + rank**: near O(1) per operation.

## How to Reason About Complexity

1. Identify the input size(s): n = number of nodes, m = number of edges, etc.
2. Trace the dominant operation (the innermost loop or recursion branch).
3. Count how many times it runs as a function of the input size.
4. Express as O(f(n)) keeping only the largest term.
