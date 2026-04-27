"""Tests for 0004 – Priority Queue."""

import importlib.util
import os
import pytest

_HERE = os.path.dirname(__file__)
_IMPL = os.path.join(
    _HERE, "..", "implementations", "python", "0004_priority_queue.py"
)

spec = importlib.util.spec_from_file_location("_priority_queue", _IMPL)
_mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
spec.loader.exec_module(_mod)  # type: ignore[union-attr]

PriorityQueue = _mod.PriorityQueue


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_pop_order():
    """Items are returned in priority (ascending) order."""
    pq = PriorityQueue()
    pq.push("B", 5)
    pq.push("A", 1)
    pq.push("C", 3)
    assert pq.pop() == "A"
    assert pq.pop() == "C"
    assert pq.pop() == "B"


def test_peek_does_not_remove():
    """peek() returns the top item without removing it."""
    pq = PriorityQueue()
    pq.push("X", 10)
    assert pq.peek() == "X"
    assert len(pq) == 1


def test_len():
    pq = PriorityQueue()
    assert len(pq) == 0
    pq.push("a", 1)
    assert len(pq) == 1
    pq.pop()
    assert len(pq) == 0


def test_bool():
    pq = PriorityQueue()
    assert not pq
    pq.push("item", 0)
    assert pq


def test_pop_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()


def test_fifo_tie_breaking():
    """Equal priorities: earlier insertion comes out first."""
    pq = PriorityQueue()
    pq.push("first", 1)
    pq.push("second", 1)
    assert pq.pop() == "first"
    assert pq.pop() == "second"


def test_iteration():
    """Iterating the queue yields items in priority order."""
    pq = PriorityQueue()
    for priority, item in [(3, "c"), (1, "a"), (2, "b")]:
        pq.push(item, priority)
    assert list(pq) == ["a", "b", "c"]
