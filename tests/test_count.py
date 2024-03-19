import pytest
from pathlib import Path
import sys

here = Path(__file__).parent
sys.path.append((here / ".." / "code").as_posix())
from count import count_words

def test_count_words():
    text = "This is a test. This is only a test."
    expected = {
        "This": 2,
        "is": 2,
        "a": 2,
        "test": 2,
        "only": 1,
    }
    assert count_words(text) == expected

