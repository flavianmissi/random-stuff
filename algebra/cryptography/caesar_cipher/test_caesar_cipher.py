import unittest
from caesar_cipher import CaesarCipher
from nose.tools import assert_equals

class CaesarCipherTestCase(unittest.TestCase):
    def test_should_get_2_17_8_15_19_14_6_17_0_5_8_0_code_to_criptografia_word(self):
        cipher = CaesarCipher("criptografia")
        assert_equals(cipher.to_code(), [2,17,8,15,19,14,6,17,0,5,8,0])

    def test_should_get_fulswrjudild_to_criptografia_word(self):
        cipher = CaesarCipher("criptografia")
        assert_equals(cipher.encrypt(), "fulswrjudild")

    def test_should_get_criptografia_when_decoded_criptografia_word(self):
        cipher = CaesarCipher("criptografia")
        cipher.encrypt()
        assert_equals(cipher.decrypt(), "criptografia")

    def test_should_get_zope_when_decoded_zope_word(self):
        cipher = CaesarCipher("zope")
        cipher.encrypt()
        assert_equals(cipher.decrypt(), "zope")

    def test_should_get_warm_when_decoded_warm_word(self):
        cipher = CaesarCipher("warm")
        cipher.encrypt()
        assert_equals(cipher.decrypt(), "warm")

    def test_should_get_xmen_when_decoded_xmen_word(self):
        cipher = CaesarCipher("xmen")
        cipher.encrypt()
        assert_equals(cipher.decrypt(), "xmen")

    def test_should_get_livelongandprosper_when_decoded_livelongandprosper_word(self):
        cipher = CaesarCipher("livelongandprosper")
        cipher.encrypt()
        assert_equals(cipher.decrypt(), "livelongandprosper")

    def test_should_get_zope_when_decoded_zope_word_with_a_7_key_value(self):
        cipher = CaesarCipher("zope", 7)
        cipher.encrypt()
        assert_equals(cipher.decrypt(), "zope")
