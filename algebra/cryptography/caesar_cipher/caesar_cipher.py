import string
from code_helper import CodeHelper

class CaesarCipher(object):
    def __init__(self, key=3):
        self.key = key
        self.letters = list(string.ascii_lowercase) # a to z
        self.helper = CodeHelper()

    def encrypt(self, msg):
        code = self.helper.to_code(msg)
        encrypted = []
        for i in code:
            index = i + self.key
            if index >= len(self.letters):
                index = index % len(self.letters)
            encrypted.append(index)
        encrypted = self.helper.to_str(encrypted)
        return encrypted

    def decrypt(self, msg):
        decrypted = []
        for i in msg:
            index = self.letters.index(i) - self.key
            decrypted.append(index)
        decrypted = self.helper.to_str(decrypted)
        return decrypted
