'''
coding: utf-8
test infixToPostfix function
Created 2014-09-24
ZouJingLin <zjl_717@sina.com>
'''

import unittest
import conversion

class ConversionTestCase(unittest.TestCase):

    def test_value(self):
        self.assertEqual(conversion.infixToPostfix("A + B * C"), "A B C * +")
        self.assertEqual(conversion.infixToPostfix("( A + B ) * C"), "A B + C *")
        self.assertEqual(conversion.infixToPostfix("( a - B ) / ( C - d )"), "a B - C d - /")
        self.assertEqual(conversion.infixToPostfix("1 * 5 + 3 * 8"), "1 5 * 3 8 * +")


if __name__ == '__main__':
    unittest.main()
