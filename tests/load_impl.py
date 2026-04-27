"""Shared import helper for test files.

Usage in test files:
    from tests.load_impl import load_impl
    module = load_impl("0001_a_star")
    find_path = module.find_path
"""
import importlib.util
import os

_IMPL_DIR = os.path.join(os.path.dirname(__file__), "..", "implementations", "python")


def load_impl(module_filename: str):
    """Load an implementation module by filename (without .py extension)."""
    path = os.path.join(_IMPL_DIR, module_filename + ".py")
    spec = importlib.util.spec_from_file_location(module_filename, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
