"""Test that the functions in the sums module are doing their job."""

import python_module_quickstart.addition.sums as sums


class TestSums:
    def test_one_plus_one(self):
        """Ensure 1 + 1 = 2.

        :return: True if 1 + 1 = 2 according to my_sum(). False otherwise.
        :rtype: Assertion.
        """
        assert sums.my_sum(1., 1.) == 2.

    def test_two_plus_two(self, two_plus_two):
        """Ensure 2 + 2 = 5.

        :return: True if 2 + 2 = 5 according to my_sum(). False otherwise.
        :rtype: Assertion.
        """
        assert sums.my_sum(
            two_plus_two['a'], two_plus_two['b']) == two_plus_two['sum']
