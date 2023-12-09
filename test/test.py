import unittest
from src.main import minEatingSpeed


class TestMinEatingSpeed(unittest.TestCase):
    def test_example1_minimum_speed(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(minEatingSpeed(piles, h), 4)

    def test_example2_hurry_up(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(minEatingSpeed(piles, h), 30)

    def test_example3_optimal_speed(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(minEatingSpeed(piles, h), 23)

    def test_custom1_high_speed(self):
        piles = [10, 20, 30, 40]
        h = 4
        self.assertEqual(minEatingSpeed(piles, h), 40)

    def test_custom2_less_time(self):
        piles = [15, 25, 35, 45]
        h = 3
        self.assertEqual(minEatingSpeed(piles, h), 45)

    def test_custom3_slow_eating(self):
        piles = [5, 8, 2, 1]
        h = 10
        self.assertEqual(minEatingSpeed(piles, h), 2)


if __name__ == '__main__':
    unittest.main()
