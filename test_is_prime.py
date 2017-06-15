import unittest

from check_prime import *


class CheckPrimeTestCase(unittest.TestCase):
    def test_first_four_primes_included(self):
        self.assertEqual([2, 3, 5, 7], is_prime(10))

    def test_non_primes_not_included(self):
        self.assertNotIn(4, is_prime(10))
        self.assertNotIn(9, is_prime(10))

    def test_function_raises_exception_for_non_integer_params(self):
        with self.assertRaises(TypeError) as context:
            is_prime('10')
            self.assertEqual(
                'Argument must be an integer',
                context.exception.message, "Invalid input"
                )

    def test_is_prime_returns_list(self):
        self.assertEqual(type(is_prime(10)), list, 'Function should return list')

    def test_is_prime_returns_list_of_integers(self):
        self.assertTrue(all (isinstance (n, int) for n in is_prime(10)), 'Function returns list of none integers')
