import string

class MonoalfabeticaAditiva(object):
    def __init__(self, msg, key=3):
        self.letters = list(string.ascii_lowercase) # a to z
        self.key = key
        self.msg = msg
        self.encode()
        self.encrypt()

    def encode(self):
        self.code = []
        for c in self.msg:
            self.code.append(self.letters.index(c))
        return self.code

    def encrypt(self):
        self.encrypted = []
        for i in self.code:
            self.encrypted.append(i + self.key)
        return self.encrypted

    def decrypt_code(self):
        self.decrypted_code = []
        for i in self.encrypted:
            self.decrypted_code.append(i - self.key)


