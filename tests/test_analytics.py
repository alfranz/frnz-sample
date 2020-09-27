from frnz.data import cities
from frnz.analytics import count_missing
import pytest


def test_counting_nas_return_correct_count():
    result = count_missing(cities)
    expected = {"city": 0, "country": 1, "population": 1}
    assert len(result) == len(expected)
    assert result["country"] == expected["country"]