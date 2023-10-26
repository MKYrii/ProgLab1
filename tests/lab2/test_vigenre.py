from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere
import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.decrypt_vigenere = decrypt_vigenere
        self.encrypt_vigenere = encrypt_vigenere

    def test_null(self):
        self.assertEqual(self.decrypt_vigenere('', 'qw'), '')
        self.assertEqual(self.encrypt_vigenere('', 'qw'), '')

    def test_word(self):
        self.assertEqual(self.decrypt_vigenere('qwertyADD', 'Home'), 'jisnmkOZW')
        self.assertEqual(self.encrypt_vigenere('qwertyADD', 'Home'), 'xkqvamMHK')

    def test_symbols(self):
        self.assertEqual(self.decrypt_vigenere('35P654/.sar1.+', 'gahf9-'), '35J654/.stm1.+')
        self.assertEqual(self.encrypt_vigenere('35P654/.sar1.+', 'gahf9-'), '35V654/.shw1.+')


if __name__ == "__main__":
    unittest.main()