from testpackage.bookcode.test_case.calculator import Calculator
import unittest

class TestAdd(unittest.TestCase):
    """ add()方法测试"""
    def test_add_integer(self):
        c =  Calculator(3,5)
        self.assertEqual(c.add(),8)
    def test_add_decimal(self): 
        c = Calculator(3.2, 5.5)
        self.assertEqual(c.add(), 8)
    def test_add_string(self):
        c =  Calculator('7','9')
        self.assertEqual(c.add(),16)


class TestSub(unittest.TestCase):
    """ sub()方法测试"""
    def test_sub_integer(self):
        c =  Calculator(5,3)
        self.assertEqual(c.sub(),2)
    def test_sub_decimal(self):
        c = Calculator(3.2, 1.1)
        self.assertEqual(c.sub(), 2.1)


if __name__ == '__main__':
    unittest.main()