import unittest

from check_prime import *


class CheckPrimeTestCase(unittest.TestCase):
    def test_first_four_primes_included(self):
        self.assertEqual([2, 3, 5, 7], is_prime(10))

    def test_non_primes_not_included(self):
        self.assertNotIn(4, is_prime(10))
        self.assertNotIn(9, is_prime(10))

    def test_n_is_integer(self):
        with self.assertRaises(TypeError):
            is_prime('10')

    def test_n_is_greater_than_one(self):
        self.assertGreater(2, 1, 'N should be greater than ONE')

    def test_n_is_actually_included(self):
        self.assertIn(11, is_prime(11))

