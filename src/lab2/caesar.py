def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if 'A' <= i <= 'Z':
            ciphertext += chr(65 + (ord(i) - 65 + shift) % 26)
        elif 'a' <= i <= 'z':
            ciphertext += chr(97 + (ord(i) - 97 + shift) % 26)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if 'A' <= i <= 'Z':
            plaintext += chr(65 + (ord(i) - 65 - shift) % 26)
        elif 'a' <= i <= 'z':
            plaintext += chr(97 + (ord(i) - 97 - shift) % 26)
        else:
            plaintext += i
    return plaintext
