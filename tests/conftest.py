"""conftest.py — make the repo root importable and provide importlib helper."""
import importlib.util
import os
import sys

# Add repo root to path so `implementations` is importable as a package
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def load_impl(filename: str):
    """Load an implementation module by filename (handles numeric prefixes)."""
    path = os.path.join(ROOT, "implementations", "python", filename)
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
