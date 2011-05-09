import unittest
from caesar_cipher import CaesarCipher
from nose.tools import assert_equals

class CaesarCipherTestCase(unittest.TestCase):
    def setUp(self):
        self.cipher = CaesarCipher()

    def test_should_get_fulswrjudild_to_criptografia_word(self):
        assert_equals(self.cipher.encrypt("criptografia"), "fulswrjudild")

    def test_should_get_criptografia_when_decoded_criptografia_word(self):
        encrypted = self.cipher.encrypt("criptografia")
        assert_equals(self.cipher.decrypt(encrypted), "criptografia")

    def test_should_get_zope_when_decoded_zope_word(self):
        encrypted = self.cipher.encrypt("zope")
        assert_equals(self.cipher.decrypt(encrypted), "zope")

    def test_should_get_warm_when_decoded_warm_word(self):
        encrypted = self.cipher.encrypt("warm")
        assert_equals(self.cipher.decrypt(encrypted), "warm")

    def test_should_get_xmen_when_decoded_xmen_word(self):
        encrypted = self.cipher.encrypt("xmen")
        assert_equals(self.cipher.decrypt(encrypted), "xmen")

    def test_should_get_livelongandprosper_when_decoded_livelongandprosper_word(self):
        encrypted = self.cipher.encrypt("livelongandprosper")
        assert_equals(self.cipher.decrypt(encrypted), "livelongandprosper")

    def test_should_get_zope_when_decoded_zope_word_with_a_7_key_value(self):
        cipher = CaesarCipher(7)
        encrypted = cipher.encrypt("zope")
        assert_equals(cipher.decrypt(encrypted), "zope")
