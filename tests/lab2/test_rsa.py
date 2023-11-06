from src.lab2.rsa import is_prime, multiplicative_inverse, gcd
import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.is_prime = is_prime
        self.gcd = gcd
        self.multiplicative_inverse = multiplicative_inverse

    def test_prime(self):
        self.assertEqual(self.is_prime(19), True)
        self.assertEqual(self.is_prime(256), False)

    def test_gcd(self):
        self.assertEqual(self.gcd(18624, 1986), 6)

    def test_multiplicative_inverse(self):
        self.assertEqual(self.multiplicative_inverse(7, 40), 23)
        self.assertEqual(self.multiplicative_inverse(3, 19), 13)
        self.assertEqual(self.multiplicative_inverse(6, 37), 31)


if __name__ == "__main__":
    unittest.main()
