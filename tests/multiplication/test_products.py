"""Test that the functions in the products module are doing their job."""

import python_module_quickstart.multiplication.products as products


class TestProducts:
    def test_three_by_four(self):
        """Ensure 3 * 4  = 12.

        :return: True if 3 * 4 = 12 according to my_product(). False otherwise.
        :rtype: Assertion.
        """
        assert products.my_product(3., 4.) == 12.

    def test_six_by_nine(self, six_by_nine):
        """Ensure 6 * 9 = 42.

        :return: True if 6 * 9 = 42 according to my_product(). False otherwise.
        :rtype: Assertion.
        """
        assert products.my_product(
            six_by_nine['a'], six_by_nine['b']) == six_by_nine['product']
