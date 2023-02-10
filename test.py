from main import add, sub, multi, divide
import unittest

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        result1 = add(2, 2)
        self.assertEqual(result1, 4)
        result2 = add(35, -10)
        self.assertEqual(result2, 25)
        result3 = add(-1, 0)
        self.assertEqual(result3, -1)

    def test_sub(self):
        result1 = sub(2, 2)
        self.assertEqual(result1, 0)
        self.assertEqual(sub(-2, 2), -4)
        self.assertEqual(sub(5, 0), 5)

    def test_multi(self):
        self.assertEqual(multi(2, 2), 4)
        self.assertEqual(multi(20, 10), 200)
        self.assertEqual(multi(200, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 2), 1)
        self.assertEqual(divide(1000, 10), 100)
        self.assertEqual(divide(0, 2000), 0)

        self.assertRaises(ZeroDivisionError, divide, 9, 0)

unittest.main()

