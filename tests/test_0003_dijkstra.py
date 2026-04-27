"""Tests for 0003_dijkstra.py"""

import importlib.util
import math
import os

_spec = importlib.util.spec_from_file_location(
    "dijkstra",
    os.path.join(os.path.dirname(__file__), "..", "implementations", "python", "0003_dijkstra.py"),
)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
dijkstra = _mod.dijkstra


def test_example_graph() -> None:
    """Distances on the example graph should match [0, 3, 1, 4]."""
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    result = dijkstra(graph, source=0, num_nodes=4)
    assert result == [0, 3, 1, 4]


def test_single_node() -> None:
    """A graph with only the source node has distance [0]."""
    graph = {0: []}
    result = dijkstra(graph, source=0, num_nodes=1)
    assert result == [0]


def test_disconnected_graph() -> None:
    """Unreachable node should have infinite distance."""
    graph = {0: [(1, 5)], 1: [], 2: []}
    result = dijkstra(graph, source=0, num_nodes=3)
    assert result[0] == 0
    assert result[1] == 5
    assert result[2] == math.inf


def test_direct_edge() -> None:
    """Source directly connected to goal — should return edge weight."""
    graph = {0: [(1, 7)], 1: []}
    result = dijkstra(graph, source=0, num_nodes=2)
    assert result[1] == 7


def test_multiple_paths_shortest_chosen() -> None:
    """Dijkstra should pick the shortest path among alternatives."""
    # 0→1 directly costs 10, 0→2→1 costs 1+2=3
    graph = {0: [(1, 10), (2, 1)], 1: [], 2: [(1, 2)]}
    result = dijkstra(graph, source=0, num_nodes=3)
    assert result[1] == 3
