"""Fixture for testing the my_sum() function."""

import pytest


@pytest.fixture
def two_plus_two():
    """Two numbers and their sum.

    :return: The inputs to a sum and its result.
    :rtype: dict(float).
    """
    return {'a': 2., 'b': 2., 'sum': 5.}
