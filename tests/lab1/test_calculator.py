import unittest
from math import cos, log, pi, sin, sqrt, tan
from src.lab1.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_divide(self):
        self.assertEqual(self.calculator.main('10 // 2'), '5')

    def test_multiply(self):
        self.assertEqual(self.calculator.main('10 * 2'), '20')

    def test_error(self):
        self.assertEqual(self.calculator.main('a10 - 4'), 'Выражение введено неверно')

    def test_long(self):
        self.assertEqual(self.calculator.main('57 * (sin(0.5*pi)) - log(64,2)'), '51.0')


if __name__ == "__main__":
    unittest.main()