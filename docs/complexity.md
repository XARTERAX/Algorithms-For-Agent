# Algorithm Complexity Notes

> Reference card for **O / Θ / Ω** notation and common complexity classes used throughout this repo.

---

## 1. Asymptotic Notation

| Symbol | Name | Meaning |
|--------|------|---------|
| **O(f(n))** | Big-O (upper bound) | The algorithm runs in *at most* f(n) time for large n. Used to describe worst-case. |
| **Θ(f(n))** | Theta (tight bound) | The algorithm runs in *exactly* f(n) time for large n (both upper and lower bound). |
| **Ω(f(n))** | Omega (lower bound) | The algorithm runs in *at least* f(n) time for large n. Used to describe best-case. |

### Formal Definitions

Given functions f, g : ℕ → ℝ⁺:

- **O(g)** : ∃ c > 0, n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀
- **Ω(g)** : ∃ c > 0, n₀ such that f(n) ≥ c·g(n) for all n ≥ n₀
- **Θ(g)** : f ∈ O(g) AND f ∈ Ω(g)

---

## 2. Common Complexity Classes (fastest → slowest)

| Class | Name | Example algorithm |
|-------|------|-------------------|
| O(1) | Constant | Array index lookup, hash table get |
| O(log n) | Logarithmic | Binary search, heap push/pop |
| O(n) | Linear | Linear scan, BFS/DFS on a list |
| O(n log n) | Log-linear | Merge sort, heap sort |
| O(n²) | Quadratic | Bubble sort, brute-force 2-sum |
| O(n³) | Cubic | Floyd-Warshall (dense graph) |
| O(2ⁿ) | Exponential | Brute-force subsets, naive minimax |
| O(n!) | Factorial | Brute-force permutations (TSP) |

---

## 3. Recurrence Relations and the Master Theorem

For divide-and-conquer recurrences of the form **T(n) = a·T(n/b) + f(n)**:

- If f(n) = O(n^(log_b a − ε)) → **T(n) = Θ(n^(log_b a))**
- If f(n) = Θ(n^(log_b a)) → **T(n) = Θ(n^(log_b a) · log n)**
- If f(n) = Ω(n^(log_b a + ε)) → **T(n) = Θ(f(n))**

**Example — Merge Sort:** T(n) = 2·T(n/2) + O(n)  →  case 2 → **Θ(n log n)**

---

## 4. Worked Examples

### A* Search
- **Time:** O(E · log V) with a binary heap, where E = edges, V = vertices.
- **Space:** O(V) for the open/closed sets.

### BFS on a Grid (rows × cols)
- **Time:** O(rows · cols) — every cell visited at most once.
- **Space:** O(rows · cols) — queue and visited set.

### Dijkstra (with priority queue)
- **Time:** O((V + E) log V) using a min-heap.
- **Space:** O(V) for distance array + priority queue.

### Minimax (depth d, branching factor b)
- **Time:** O(bᵈ) brute force · O(b^(d/2)) with alpha-beta pruning.
- **Space:** O(d) call stack.

---

## 5. Tips for Estimating Complexity

1. **Count nested loops:** each loop over n elements multiplies by n.
2. **Identify divide-and-conquer:** apply the Master Theorem.
3. **Graph algorithms:** usually expressed in V (vertices) and E (edges).
4. **DP:** `states × transition cost` gives the time complexity.
5. **Logarithms appear** whenever you halve the problem (binary search, heaps).
