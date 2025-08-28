import pytest
from src.util.detector import detect_duplicates
# from src.util.parser import parser, Article
# develop your test cases here

@pytest.mark.unit
# TC04 Empty list input
def test_empty_list():
    with pytest.raises(ValueError):
        detect_duplicates("")
    