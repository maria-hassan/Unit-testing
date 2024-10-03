from calculator import Calculator
import unittest


class Test_calculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 12), 22)
        self.assertEqual(self.calc.add(19, 1), 20)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(self.calc.sub(1, 9), -8)
        self.assertEqual(self.calc.sub(13, 2), 11)
        self.assertEqual(self.calc.sub(20, 2), 18)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 5), 10)
        self.assertEqual(self.calc.mul(13, 2), 26)
        self.assertEqual(self.calc.mul(1, 2), 2)

    def test_div(self):
        self.assertEqual(self.calc.div(2, 4), 0.5)
        self.assertEqual(self.calc.div(5, 10), 0.5)
        self.assertEqual(self.calc.div(40, 10), 4)


if __name__ == "__main__":
    unittest.main()
