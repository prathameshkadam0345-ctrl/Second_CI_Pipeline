import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_normal():
    assert module.first_non_repeating_char("swiss") == "w"


def test_first_non_repeating_first_character():
    assert module.first_non_repeating_char("hello") == "h"


def test_first_non_repeating_none():
    assert module.first_non_repeating_char("aabbcc") is None