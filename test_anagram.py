import unittest
from anagram import Anagram


class AnagramsTest(unittest.TestCase):
    def test_check_if_anagram(self):
        # check the words that are anagrams
        self.assertTrue(Anagram.checkIfAnagram("", ""), "Both empty string, they are anagrams")
        self.assertTrue(Anagram.checkIfAnagram("wolf", "flow"), "They are anagrams")
        self.assertTrue(Anagram.checkIfAnagram("WoLf", "FlOw"), "Case insensitive test, they are anagrams")
        self.assertTrue(Anagram.checkIfAnagram("restful", "fluster"), "They are anagrams")
        self.assertTrue(Anagram.checkIfAnagram("loooooooooooooooogword", "wordloooooooooooooooog"), "They are anagrams")
        self.assertTrue(Anagram.checkIfAnagram("TomMarvoloRiddle", "IamLordVoldemort"), "They are anagrams")
        # check the words that are not anagrams
        self.assertFalse(Anagram.checkIfAnagram(None, None), "None should just return false")
        self.assertFalse(Anagram.checkIfAnagram("abc", "test"), "They are NOT anagrams")
        self.assertFalse(Anagram.checkIfAnagram("grove", "groove"), "They are NOT anagrams")

    def test_insert_request(self):
        anagram = Anagram()
        anagram.insertRequest("abc", "bca")
        anagram.insertRequest("abc", "bca")
        anagram.insertRequest("bca", "abc")
        anagram.insertRequest("tyyy", "yyyt")
        anagram.insertRequest("yyyt", "tyyy")
        # insert other 2 other requests
        anagram.insertRequest("kuk", "kku")
        anagram.insertRequest("rrr", "rrr")
        self.assertEqual(len(anagram.requests.values()), 4, "Should have 4 different requests")

    def test_get_top_ten_requests(self):
        anagram = Anagram()
        anagram.insertRequest("abc", "bca")
        anagram.insertRequest("abc", "bca")
        anagram.insertRequest("bca", "abc")
        anagram.insertRequest("tyyy", "yyyt")
        anagram.insertRequest("yyyt", "tyyy")
        self.assertTrue(len(anagram.getTopTenRequests()), 2)
        anagram.insertRequest("a", "a")
        anagram.insertRequest("kkk", "kkk")
        anagram.insertRequest("iu", "ui")
        anagram.insertRequest("yyzz", "zzyy")
        anagram.insertRequest("rtc", "ctr")
        anagram.insertRequest("io", "oi")
        anagram.insertRequest("erpet", "peter")
        anagram.insertRequest("hi", "ih")
        self.assertTrue(len(anagram.getTopTenRequests()), 10)
        anagram.insertRequest("hi", "ih")
        anagram.insertRequest("hi", "ih")
        anagram.insertRequest("oy", "yo")
        self.assertTrue(len(anagram.getTopTenRequests()), 11)


