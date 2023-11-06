import unittest
import main

class TestFunc(unittest.TestCase):
    def test_func(self):
        # value1 = 1 # 引数１
        # value2 = 2 # 引数２
        # ...
        # expected = 3 # 期待される値
        # actual = main.func(value1, value2 , ...)
        # self.assertEqual(expected, actual)

        expected = "hello world"
        actual = main.forTest()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()