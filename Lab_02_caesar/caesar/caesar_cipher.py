# Trong folder "caesar" tạo file "caesar_cipher.py"
from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        encrypted_text = []
        text_upper = text.upper()

        for letter in text_upper:
            output_index = (self.alphabet.index(letter) + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)

        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        decrypted_text = []
        text_upper = text.upper()

        for letter in text_upper:
            output_index = (self.alphabet.index(letter) - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)

        return "".join(decrypted_text)
