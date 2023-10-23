from src.lab3.sudoku import group
import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.group = group

    def test_group(self):
        self.assertEqual(self.group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


if __name__ == "__main__":
    unittest.main()