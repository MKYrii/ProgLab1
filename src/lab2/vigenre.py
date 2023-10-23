def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = ''.join([i for i in keyword if ('A' <= i <= 'Z' or 'a' <= i <= 'z')])
    keyword = keyword.lower()
    post = 0
    for i in range(len(plaintext)):
        if 'A' <= plaintext[i] <= 'Z':
            ciphertext += chr(65 + (ord(plaintext[i]) - 65 + ord(keyword[(i - post) % len(keyword)]) - 97) % 26)
        elif 'a' <= plaintext[i] <= 'z':
            ciphertext += chr(97 + (ord(plaintext[i]) - 97 + ord(keyword[(i - post) % len(keyword)]) - 97) % 26)
        else:
            post += 1
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = ''.join([i for i in keyword if ('A' <= i <= 'Z' or 'a' <= i <= 'z')])
    keyword = keyword.lower()
    post = 0
    for i in range(len(ciphertext)):
        if 'A' <= ciphertext[i] <= 'Z':
            plaintext += chr(65 + (ord(ciphertext[i]) - 65 - ord(keyword[(i - post) % len(keyword)]) + 97) % 26)
        elif 'a' <= ciphertext[i] <= 'z':
            plaintext += chr(97 + (ord(ciphertext[i]) - ord(keyword[(i - post) % len(keyword)])) % 26)
        else:
            post += 1
            plaintext += ciphertext[i]
    return plaintext