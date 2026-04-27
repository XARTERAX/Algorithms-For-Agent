"""Tests for 0004_priority_queue.py"""

import importlib.util
import os

import pytest

_spec = importlib.util.spec_from_file_location(
    "priority_queue",
    os.path.join(
        os.path.dirname(__file__), "..", "implementations", "python", "0004_priority_queue.py"
    ),
)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
MinPriorityQueue = _mod.MinPriorityQueue


def test_pop_order() -> None:
    """Items should be popped in ascending priority order."""
    pq = MinPriorityQueue()
    pq.push("A", 3)
    pq.push("B", 1)
    pq.push("C", 2)
    assert pq.pop() == "B"
    assert pq.pop() == "C"
    assert pq.pop() == "A"


def test_peek_does_not_remove() -> None:
    """peek() should not change the queue."""
    pq = MinPriorityQueue()
    pq.push("X", 5)
    assert pq.peek() == "X"
    assert len(pq) == 1


def test_is_empty() -> None:
    pq = MinPriorityQueue()
    assert pq.is_empty()
    pq.push("Y", 1)
    assert not pq.is_empty()
    pq.pop()
    assert pq.is_empty()


def test_pop_from_empty_raises() -> None:
    pq = MinPriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_from_empty_raises() -> None:
    pq = MinPriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()


def test_equal_priorities_fifo() -> None:
    """Items with the same priority should come out in insertion order."""
    pq = MinPriorityQueue()
    pq.push("first", 1)
    pq.push("second", 1)
    pq.push("third", 1)
    assert pq.pop() == "first"
    assert pq.pop() == "second"
    assert pq.pop() == "third"


def test_len() -> None:
    pq = MinPriorityQueue()
    assert len(pq) == 0
    pq.push("a", 1)
    pq.push("b", 2)
    assert len(pq) == 2
    pq.pop()
    assert len(pq) == 1
