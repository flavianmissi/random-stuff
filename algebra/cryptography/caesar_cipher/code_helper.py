import string

class CodeHelper(object):
    def __init__(self):
        self.letters = list(string.ascii_lowercase) # a to z

    def to_code(self, msg):
        code = []
        for c in msg:
            code.append(self.letters.index(c))
        return code

    def to_str(self, code):
        msg = []
        for i in range(len(code)):
            msg.append(self.letters[code[i]])
        return ''.join(msg)
