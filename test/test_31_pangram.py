
import sys
from pathlib import Path

# Add the code folder to Python's search path
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("31_pangram")


def test_pangram_true():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False

