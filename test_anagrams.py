import unittest
import anagrams


class TestAnagrams(unittest.TestCase):

    def test_get_anagrams(self):
        self.assertEqual(anagrams.get_anagrams('ab'),['ab','ba'])
        self.assertEqual(anagrams.get_anagrams('abc'),['abc','acb','bac','bca','cab','cba'])

    def test_get_number_of_anagrams(self):
        self.assertEqual(anagrams.get_number_of_anagrams('ab'), 2)
        self.assertEqual(anagrams.get_number_of_anagrams('abc'), 6)
