import unittest
import os

from src.disjoint import count_cross_pairs


class TestDisjointSet(unittest.TestCase):
    def test_count_cross_pairs(self):
        N = 3
        pairs = [
            [1, 2],
            [2, 4],
            [3, 5]
        ]
        result, possible_pairs = count_cross_pairs(N, pairs)
        expected_pairs = ['1/4', '3/2', '3/4']
        self.assertEqual(result, 3)
        self.assertCountEqual(sorted(possible_pairs), sorted(expected_pairs))

        N = 4
        pairs = [
            [1, 2],
            [2, 4],
            [3, 5],
            [6, 8]
        ]
        result, possible_pairs = count_cross_pairs(N, pairs)
        expected_pairs = ['1/8', '1/4', '3/8', '3/2', '3/4']
        self.assertEqual(result, 5)
        self.assertCountEqual(sorted(possible_pairs), sorted(expected_pairs))


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, "test_input.txt")

    with open(input_file_path, "w", encoding="utf-8") as file:
        file.write("3\n1 2\n2 4\n3 5\n")

    unittest.main()

    os.remove(input_file_path)
