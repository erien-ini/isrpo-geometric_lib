import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_fractional_sides(self):
        """Тест с дробными сторонами"""
        self.assertEqual(area(2.5, 4.0), 10.0)
        self.assertEqual(perimeter(2.5, 4.0), 13.0)

    def test_large_numbers(self):
        """Тест с очень большими числами"""
        self.assertEqual(area(1000000, 2000000), 2000000000000)
        self.assertEqual(perimeter(1000000, 2000000), 6000000)

    def test_zero_perimeter(self):
        """Тест периметра с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 0), 0)

if __name__ == '__main__':
    unittest.main()