from testpackage.bookcode.test_case.calculator import Calculator
import unittest
class TestCalculator(unittest.TestCase):
    def setUp(self):
        print('开始测试')
    def tearDown(self):
        print('测试结束')
    def test_add(self):
        c = Calculator(3,5)
        result = c.add()
        self.assertEqual(result,8)
    def test_sub(self):
        c = Calculator(7,2)
        result = c.sub()
        self.assertEqual(result,5)
    def test_mul(self):
        c = Calculator(3,3)
        result = c.mul()
        self.assertEqual(result,10)
    def test_div(self):
        c = Calculator(6,2)
        result = c.div()
        self.assertEqual(result,3)

if __name__ == '__main__':

    #创建testsuit套件
    suit = unittest.TestSuite()

    #添加测试用例
    suit.addTest(TestCalculator('test_add'))
    suit.addTest(TestCalculator('test_sub'))
    suit.addTest(TestCalculator('test_mul'))
    suit.addTest(TestCalculator('test_div'))

    #创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # unittest.main()