
import unittest

from src.main import find_shortest_path


class TestShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        matrix = [
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 0],
        ]
        start = (0, 0)
        end = (3, 4)
        self.assertEqual(find_shortest_path(matrix, start, end), 8)

        start = (0, 0)
        end = (2, 2)
        self.assertEqual(find_shortest_path(matrix, start, end), 4)

        matrix = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        start = (0, 0)
        end = (2, 2)
        self.assertEqual(find_shortest_path(matrix, start, end), 4)

        matrix = [
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
        ]
        start = (0, 0)
        end = (2, 2)
        self.assertEqual(find_shortest_path(matrix, start, end), -1)

        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        start = (0, 0)
        end = (2, 2)
        self.assertEqual(find_shortest_path(matrix, start, end), 6)


if __name__ == '__main__':
    unittest.main()
