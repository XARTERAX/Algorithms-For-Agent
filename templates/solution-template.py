"""
XXXX – Short Title
==================
Problem: <one-line description>
Source:  <LeetCode / custom / …>
Difficulty: Easy / Medium / Hard
Topics: graph, search, …

Time  complexity: O(?)
Space complexity: O(?)
"""

from __future__ import annotations
from typing import Any


# ---------------------------------------------------------------------------
# Implementation
# ---------------------------------------------------------------------------


def solve(input_data: Any) -> Any:
    """Return the answer for *input_data*.

    Args:
        input_data: describe the argument.

    Returns:
        describe the return value.

    Examples:
        >>> solve(...)
        ...
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Quick self-test (run: python implementations/python/XXXX_short_title.py)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Sample cases – mirrors the problem .md examples
    test_cases = [
        # (input, expected_output)
    ]
    for inp, expected in test_cases:
        result = solve(inp)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] solve({inp!r}) = {result!r}  (expected {expected!r})")
