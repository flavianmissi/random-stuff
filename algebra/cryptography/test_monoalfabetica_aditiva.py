import string

class MonoalfabeticaAditiva(object):
    def __init__(self, msg, key=3):
        self.letters = list(string.ascii_lowercase) # a to z
        self.key = key
        self.msg = msg

    def to_code(self):
        self.code = []
        for c in self.msg:
            self.code.append(self.letters.index(c))
        return self.code

    def encrypt(self):
        self.to_code()
        self.encrypted = []
        for i in self.code:
            index = i
            if i >= len(self.letters):
                index = i % len(self.letters)
            print i, index
            self.encrypted.append(self.letters[index + self.key])
        self.encrypted = ''.join(self.encrypted)
        return self.encrypted

    def decrypt_msg(self):
        self.decrypted_msg = []
        for i in self.encrypted:
            self.decrypted_msg.append(self.letters[self.letters.index(i) - self.key])
        self.decrypted_msg = ''.join(self.decrypted_msg)
        return self.decrypted_msg
