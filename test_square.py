import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_fractional_side(self):
        """Тест со стороной-дробью"""
        self.assertEqual(area(1.5), 2.25)
        self.assertEqual(perimeter(1.5), 6.0)

    def test_large_side(self):
        """Тест с большой стороной"""
        self.assertEqual(area(10000), 100000000)
        self.assertEqual(perimeter(10000), 40000)

    def test_negative_side(self):
        """Тест с отрицательным числом (проверка математической логики умножения)"""
        self.assertEqual(area(-3), 9)
        self.assertEqual(perimeter(-3), -12)


if __name__ == '__main__':
    unittest.main()