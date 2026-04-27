# Algorithm Complexity Notes

## Asymptotic Notation

| Symbol | Name | Meaning |
|--------|------|---------|
| O(f)   | Big-O (upper bound) | The algorithm runs in **at most** f(n) steps (ignoring constants). Used for worst-case guarantees. |
| Ω(f)   | Big-Omega (lower bound) | The algorithm takes **at least** f(n) steps. Used for proving no algorithm can do better. |
| Θ(f)   | Big-Theta (tight bound) | The algorithm runs in **exactly** f(n) steps up to constants — both O and Ω hold. |

---

## Common Complexities (ordered fastest → slowest)

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array index lookup, hash map get |
| O(log n) | Logarithmic | Binary search, heap push/pop |
| O(n) | Linear | Single-pass scan, BFS/DFS |
| O(n log n) | Linearithmic | Merge sort, heap sort, Dijkstra (binary heap) |
| O(n²) | Quadratic | Bubble sort, naive 2-loop search |
| O(n³) | Cubic | Floyd-Warshall all-pairs shortest path |
| O(2ⁿ) | Exponential | Brute-force subset enumeration |
| O(n!) | Factorial | Brute-force permutations (TSP) |

---

## Examples

### O(1) — Hash map lookup
```python
d = {"a": 1}
x = d["a"]   # O(1) average
```

### O(log n) — Binary search
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# Each iteration halves the search space → O(log n)
```

### O(n) — Linear scan
```python
def find_max(arr):
    m = arr[0]
    for x in arr:   # visits each element once → O(n)
        if x > m:
            m = x
    return m
```

### O(n log n) — Merge sort
```python
# Divide array in halves log(n) levels deep,
# merge takes O(n) per level → O(n log n) total.
```

### O(n²) — Bubble sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # outer O(n)
        for j in range(n - i - 1):  # inner O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

## Recurrence Relations (Divide & Conquer)

Use the **Master Theorem** for recurrences of the form `T(n) = a·T(n/b) + f(n)`:

| Case | Condition | Result |
|------|-----------|--------|
| 1 | f(n) = O(n^(log_b a - ε)) | T(n) = Θ(n^(log_b a)) |
| 2 | f(n) = Θ(n^(log_b a)) | T(n) = Θ(n^(log_b a) · log n) |
| 3 | f(n) = Ω(n^(log_b a + ε)) | T(n) = Θ(f(n)) |

**Merge sort:** T(n) = 2·T(n/2) + O(n) → Case 2 → Θ(n log n)  
**Binary search:** T(n) = T(n/2) + O(1) → Case 2 → Θ(log n)

---

## Space Complexity

- Count the **extra** memory used (not including input).
- Recursion depth counts: DFS on a graph of n nodes → O(n) stack space worst case.
- In-place algorithms: O(1) extra space (e.g., quicksort partition step).

---

## Tips for Estimating Complexity

1. Count the number of nested loops (each loop multiplies by its range).
2. For recursion, write the recurrence and apply Master Theorem or unroll.
3. For graph algorithms: `V` = vertices, `E` = edges.  
   BFS/DFS = O(V + E); Dijkstra (binary heap) = O((V + E) log V).
4. Hash operations are O(1) **average**, O(n) worst case.
