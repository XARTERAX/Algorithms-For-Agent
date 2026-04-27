# Algorithm Complexity Quick Reference

## Big-O Notation

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array scan |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Bubble sort, naive graph |
| O(2ⁿ) | Exponential | Brute-force subsets |
| O(n!) | Factorial | All permutations |

## Data Structures

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | O(1) avg | O(n) |
| Binary Heap | O(1) peek | O(n) | O(log n) | O(log n) | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

## Graph Algorithms (relevant to Agents)

| Algorithm | Time | Space | Use case |
|-----------|------|-------|----------|
| BFS | O(V + E) | O(V) | Shortest path (unweighted) |
| DFS | O(V + E) | O(V) | Connectivity, cycle detection |
| Dijkstra | O((V + E) log V) | O(V) | Shortest path (non-negative weights) |
| A\* | O(E log V) | O(V) | Heuristic shortest path (grids / games) |
| Bellman-Ford | O(VE) | O(V) | Shortest path (negative weights) |

## Sorting

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Tim sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

## Game Tree / Search

| Algorithm | Nodes explored | Space | Notes |
|-----------|---------------|-------|-------|
| Minimax | O(bᵈ) | O(bd) | b = branching, d = depth |
| Alpha-Beta | O(b^(d/2)) best | O(bd) | With good move ordering |
| MCTS | Configurable | O(simulations) | Works without evaluation fn |

## Heap Operations (Python `heapq`)

```python
import heapq

h = []
heapq.heappush(h, item)   # O(log n)
item = heapq.heappop(h)   # O(log n)  — pops smallest
item = h[0]               # O(1)      — peek smallest
heapq.heapify(list)       # O(n)
```
