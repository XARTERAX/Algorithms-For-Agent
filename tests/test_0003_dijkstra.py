"""Tests for 0003 – Dijkstra Shortest Path."""

import importlib.util
import os
import math

_HERE = os.path.dirname(__file__)
_IMPL = os.path.join(_HERE, "..", "implementations", "python", "0003_dijkstra.py")

spec = importlib.util.spec_from_file_location("_dijkstra", _IMPL)
_mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(_mod)  # type: ignore[union-attr]

dijkstra = _mod.dijkstra


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_example_graph():
    """Graph from the problem statement."""
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 3
    assert dist[2] == 1
    assert dist[3] == 4


def test_single_node():
    """Graph with one node."""
    dist = dijkstra({0: []}, 0)
    assert dist == {0: 0}


def test_disconnected_node():
    """Unreachable node should not appear in result."""
    graph = {0: [(1, 1)], 1: [], 2: []}
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 1
    assert 2 not in dist  # node 2 is unreachable


def test_zero_weight_edge():
    """Zero-weight edges are allowed."""
    graph = {0: [(1, 0), (2, 5)], 1: [(2, 0)], 2: []}
    dist = dijkstra(graph, 0)
    assert dist[2] == 0


def test_linear_chain():
    """A → B → C → D with equal weights."""
    graph = {0: [(1, 1)], 1: [(2, 1)], 2: [(3, 1)], 3: []}
    dist = dijkstra(graph, 0)
    assert dist == {0: 0, 1: 1, 2: 2, 3: 3}
