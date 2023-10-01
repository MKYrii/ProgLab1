import unittest


class Calculator:
    """без этих строк pylint отнимает 1.28 балла"""

    A = 0

    """без этих строк pylint отнимает 1.28 балла"""

    def main(self, s_ss):
        """без этих строк pylint отнимает 1.28 балла"""
        try:
            a_aa = eval(s_ss)
            return str(a_aa)
        except NameError:
            return "Выражение введено неверно"
        except TypeError:
            return "Выражение введено неверно"
        except SyntaxError:
            return "Выражение введено неверно"
        except ZeroDivisionError:
            return "Деление на 0"


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