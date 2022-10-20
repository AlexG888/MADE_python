import unittest
import solution_anagrams as sa


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertEqual(sa.find_anagrams("abcba", "abc"), [0, 2])
        self.assertEqual(sa.find_anagrams("aaa", "a"), [0, 1, 2])
        self.assertEqual(sa.find_anagrams("abc cba xabcd", "abc"), [0, 4, 9])
        self.assertEqual(sa.find_anagrams("abcba", ""), [])
        self.assertEqual(sa.find_anagrams("", "a"), [])
        self.assertEqual(sa.find_anagrams("", ""), [])
