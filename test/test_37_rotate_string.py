import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string_normal():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_string_one_position():
    assert module.rotate_string("hello", 1) == "ohell"


def test_rotate_string_zero_positions():
    assert module.rotate_string("hello", 0) == "hello"


def test_rotate_string_large_k():
    assert module.rotate_string("abc", 5) == "bca"


def test_rotate_string_empty():
    assert module.rotate_string("", 2) == ""