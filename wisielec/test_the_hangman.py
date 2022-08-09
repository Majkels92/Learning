import unittest
import the_hangman as hm


class TestHangman(unittest.TestCase):

    def test_gain_words_from_text(self):
        n = 0

        # Test imported file
        edited_file = "text.txt"
        self.assertTrue(edited_file[-4:] == ".txt", msg=".txt file must be used")

        # Test results from function
        self.assertIsInstance(hm.gain_words_from_text(edited_file), list, msg="Returned value from func must be a list")
        for word in hm.gain_words_from_text(edited_file):
            print(word)
            self.assertIsInstance(word, str, msg="Value in list must be a string")
            self.assertTrue(word.isalpha(), msg="Value in list must be from alphabet")
