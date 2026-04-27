# Algorithmic Complexity — Quick Reference

## Asymptotic Notation

| Symbol | Meaning | Informal reading |
|--------|---------|------------------|
| **O(f(n))** | Upper bound | "at most f(n) steps" |
| **Ω(f(n))** | Lower bound | "at least f(n) steps" |
| **Θ(f(n))** | Tight bound | "exactly f(n) steps (up to a constant)" |
| **o(f(n))** | Strict upper | "grows strictly slower than f(n)" |
| **ω(f(n))** | Strict lower | "grows strictly faster than f(n)" |

> **Rule of thumb:** when we say an algorithm is "O(n log n)" we mean its
> running time is bounded above by c · n log n for some constant c and all
> sufficiently large n.

---

## Common Complexity Classes (fastest → slowest)

| Class | Example algorithm | n = 10⁶ (approx ops) |
|-------|-------------------|----------------------|
| O(1) | Hash-table lookup | 1 |
| O(log n) | Binary search | 20 |
| O(n) | Linear scan | 10⁶ |
| O(n log n) | Merge sort | 2 × 10⁷ |
| O(n²) | Bubble sort | 10¹² |
| O(2ⁿ) | Naive subset enumeration | astronomical |

---

## How to Derive Complexity

### Loops

```python
for i in range(n):          # O(n)
    for j in range(n):      # O(n²) total
        ...
```

### Divide and Conquer — Master Theorem

Given T(n) = a·T(n/b) + f(n):

- If f(n) = O(n^(log_b a − ε))  →  T(n) = Θ(n^(log_b a))
- If f(n) = Θ(n^(log_b a))      →  T(n) = Θ(n^(log_b a) · log n)
- If f(n) = Ω(n^(log_b a + ε))  →  T(n) = Θ(f(n))

**Merge sort:** a=2, b=2, f(n)=O(n)  →  T(n) = O(n log n)

### Recursion Tree

Draw the recursion tree: sum work at each level, multiply by number of levels.

---

## Graph Algorithm Complexity (V = vertices, E = edges)

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| BFS / DFS | O(V + E) | O(V) | Adjacency list |
| Dijkstra (min-heap) | O((V + E) log V) | O(V) | Non-negative weights |
| Bellman-Ford | O(V · E) | O(V) | Handles negative weights |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| A\* | O(E log V) | O(V) | With admissible heuristic |

---

## Space Complexity

Count the **extra** memory your algorithm allocates (input storage is free unless you copy it).

- Recursive DFS: O(depth) stack frames.
- BFS: O(width) for the frontier queue.
- DP table: O(states).

---

## Amortised Analysis

When a single operation is occasionally expensive but cheap on average:

- **Dynamic array doubling:** O(1) amortised push despite O(n) occasional resize.
- **Union-Find (path compression + union by rank):** O(α(n)) ≈ O(1) per operation.
