import string

class CaesarCipher(object):
    def __init__(self, msg, key=3):
        self.letters = list(string.ascii_lowercase) # a to z
        self.key = key
        self.msg = msg

    def to_code(self):
        self.code = []
        for c in self.msg:
            self.code.append(self.letters.index(c))
        return self.code

    def to_str(self):
        for i in range(len(self.encrypted)):
            self.encrypted[i] = self.letters[self.encrypted[i]]
        self.encrypted = ''.join(self.encrypted)

    def encrypt(self):
        self.to_code()
        self.encrypted = []
        for i in self.code:
            index = i + self.key
            if index >= len(self.letters):
                index = index % len(self.letters)
            self.encrypted.append(index)
        self.to_str()
        return self.encrypted

    def decrypt(self):
        self.decrypted = []
        for i in self.encrypted:
            index = self.letters.index(i) - self.key
            self.decrypted.append(self.letters[index])
        self.decrypted = ''.join(self.decrypted)
        return self.decrypted
