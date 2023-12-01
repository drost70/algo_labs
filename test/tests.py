import unittest

from src.search import search


class TestNeedleSearch(unittest.TestCase):

    def test_basic_search(self):
        haystack = "abababababab"
        needle = "aba"
        result_position, comparison_count = search(haystack, needle)
        self.assertEqual(result_position, 8)
        self.assertEqual(comparison_count, 30)

    def test_no_match(self):
        haystack = "abcdefg"
        needle = "xyz"
        result_position, comparison_count = search(haystack, needle)
        self.assertEqual(result_position, -1)
        self.assertEqual(comparison_count, 15)

    def test_empty_needle(self):
        haystack = "abcdefgh"
        needle = ""
        result_position, comparison_count = search(haystack, needle)
        self.assertEqual(result_position, len(haystack))
        self.assertEqual(comparison_count, 0)

    def test_empty_haystack(self):
        haystack = ""
        needle = "xyz"
        result_position, comparison_count = search(haystack, needle)
        self.assertEqual(result_position, -1)
        self.assertEqual(comparison_count, 0)

    def test_same_needle_and_haystack(self):
        haystack = "abc"
        needle = "abc"
        result_position, comparison_count = search(haystack, needle)
        self.assertEqual(result_position, 0)
        self.assertEqual(comparison_count, 3)


if __name__ == '__main__':
    unittest.main()
