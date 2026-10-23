import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25.0)

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_fractional_triangle(self):
        """Тест с дробными сторонами и высотой"""
        self.assertEqual(area(5.0, 2.0), 5.0)
        self.assertEqual(perimeter(3.5, 4.5, 5.0), 13.0)

    def test_zero_height_area(self):
        """Тест площади с нулевой высотой"""
        self.assertEqual(area(10, 0), 0.0)

    def test_large_triangle(self):
        """Тест с большими значениями сторон"""
        self.assertEqual(perimeter(100000, 200000, 300000), 600000)
        self.assertEqual(area(500, 100), 25000.0)

if __name__ == '__main__':
    unittest.main()