import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("32_count_words")


def test_count_words_normal_sentence():
    assert module.count_words("Python is easy to learn") == 5


def test_count_words_extra_spaces():
    assert module.count_words("  Python   is   fun  ") == 3


def test_count_words_empty_sentence():
    assert module.count_words("") == 0