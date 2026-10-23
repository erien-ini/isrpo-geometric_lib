import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(3)
        self.assertEqual(res, math.pi * 9)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 2 * math.pi * 3)

    def test_fractional_radius(self):
        """Тест с дробным радиусом"""
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)

    def test_large_radius(self):
        """Тест с большим радиусом"""
        self.assertAlmostEqual(area(1000), math.pi * 1000000)
        self.assertAlmostEqual(perimeter(1000), 2 * math.pi * 1000)

    def test_negative_radius(self):
        """Тест с отрицательным радиусом (проверка поведения функции)"""
        self.assertAlmostEqual(area(-5), math.pi * 25)

if __name__ == '__main__':
    unittest.main()