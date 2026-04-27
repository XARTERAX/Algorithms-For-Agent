"""Tests for Dijkstra shortest path (0003_dijkstra.py)."""

import importlib.util
import math
import os

import pytest

_IMPL_DIR = os.path.join(os.path.dirname(__file__), "..", "implementations", "python")
_spec = importlib.util.spec_from_file_location(
    "dijkstra", os.path.join(_IMPL_DIR, "0003_dijkstra.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
dijkstra = _mod.dijkstra


@pytest.fixture
def simple_graph():
    return {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }


def test_basic_distances(simple_graph):
    dist = dijkstra(simple_graph, "A")
    assert dist["A"] == 0
    assert dist["B"] == 1
    assert dist["C"] == 3   # A→B→C = 1+2
    assert dist["D"] == 4   # A→B→C→D = 1+2+1


def test_source_is_zero(simple_graph):
    dist = dijkstra(simple_graph, "D")
    assert dist["D"] == 0


def test_unreachable_node():
    graph = {"A": [], "B": []}
    dist = dijkstra(graph, "A")
    assert dist["A"] == 0
    assert dist["B"] == math.inf


def test_single_node():
    dist = dijkstra({"X": []}, "X")
    assert dist["X"] == 0


def test_direct_edge():
    graph = {"A": [("B", 7)], "B": []}
    dist = dijkstra(graph, "A")
    assert dist["B"] == 7
