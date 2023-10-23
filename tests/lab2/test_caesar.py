from src.lab2.caesar import decrypt_caesar, encrypt_caesar
import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.decrypt_caesar = decrypt_caesar
        self.encrypt_caesar = encrypt_caesar

    def test_null(self):
        self.assertEqual(self.decrypt_caesar('', 3), '')
        self.assertEqual(self.encrypt_caesar('', 3), '')

    def test_word(self):
        self.assertEqual(self.decrypt_caesar('qwertyADD', 5), 'lrzmotVYY')
        self.assertEqual(self.encrypt_caesar('qwertyADD', 5), 'vbjwydFII')

    def test_symbols(self):
        self.assertEqual(self.decrypt_caesar('35P654/.sar1.+', 7), '35I654/.ltk1.+')
        self.assertEqual(self.encrypt_caesar('35P654/.sar1.+', 7), '35W654/.zhy1.+')


if __name__ == "__main__":
    unittest.main()
