"""Fixture for testing the my_product() function."""

import pytest


@pytest.fixture
def six_by_nine():
    """Two numbers and their product.

    :return: The inputs to a product and its result.
    :rtype: dict(float).
    """
    return {'a': 6., 'b': 9., 'product': 42.}
