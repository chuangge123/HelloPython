import unittest
class TestMethod(unittest.TestCase):
    #加入类方法让每一个测试方法都有 setup  terDown
    @classmethod
    def setUpClass(cls):
        print('类执行前的方法')
    @classmethod
    def tearDownClass(cls):
        print('类执行后的方法')
    #每次方法 之前执行
    def setUp(self):
        print('test_setup')
    #每次方法 之后执行
    def tearDown(self) -> None:
        print('test--tearDown')
    #每条测试方法必须要以test开头。
    def test_01(self):
        print('我是测试方法')
    def test_02(self):
        print('我是第二个测试方法')
if __name__ == '__main__':
    unittest.main()
