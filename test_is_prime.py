import unittest

from check_prime import *


class CheckPrimeTestCase(unittest.TestCase):
    def test_first_four_primes_included(self):
        self.assertEqual([2, 3, 5, 7], is_prime(10))