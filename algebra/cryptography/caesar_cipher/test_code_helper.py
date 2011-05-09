import unittest
from code_helper import CodeHelper
from nose.tools import assert_equals

class CodeHelperTestCase(unittest.TestCase):
    def setUp(self):
        self.code_helper = CodeHelper()

    def test_should_get_2_17_8_15_19_14_6_17_0_5_8_0_code_to_criptografia_word(self):
        assert_equals(self.code_helper.to_code("criptografia"), [2,17,8,15,19,14,6,17,0,5,8,0])
