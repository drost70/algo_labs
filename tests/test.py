import unittest

from src.longest_word import longest_word, is_one_letter_less


class TestLongestChain(unittest.TestCase):

    def test_longest_chain_basic(self):
        words = ["abc", "ab", "a", "abcd", "abcde"]
        self.assertEqual(longest_word(words), 5)

    def test_longest_chain_empty(self):
        words = []
        self.assertEqual(longest_word(words), 0)

    def test_longest_chain_multiple_chains(self):
        words = ["abc", "ab", "a", "xyz", "123", "def", "abcd", "abcde"]
        self.assertEqual(longest_word(words), 5)

    def test_is_one_letter_less_true(self):
        self.assertTrue(is_one_letter_less("abc", "ab"))

    def test_is_one_letter_less_false(self):
        self.assertFalse(is_one_letter_less("abc", "abcd"))


if __name__ == "__main__":
    unittest.main()
