import math
import unittest
from src.coordinate_conversion import cartesian_to_polar, polar_to_cartesian

class TestCoordinateConversion(unittest.TestCase):
    def test_cartesian_to_polar(self):
        r, theta = cartesian_to_polar(3, 4)
        self.assertAlmostEqual(r, 5.0, places=2)
        self.assertAlmostEqual(theta, math.atan2(4, 3), places=5)

    def test_polar_to_cartesian(self):
        x, y = polar_to_cartesian(5, math.atan2(4, 3))
        self.assertAlmostEqual(x, 3.0, places=2)
        self.assertAlmostEqual(y, 4.0, places=2)

if __name__ == "__main__":
    unittest.main()