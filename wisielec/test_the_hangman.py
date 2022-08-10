import unittest
import the_hangman as hm


class TestHangman(unittest.TestCase):

    def test_gain_words_from_text(self):
        # Test imported file
        edited_file = "text.txt"
        self.assertTrue(edited_file[-4:] == ".txt", msg=".txt file must be used")

        # Test results from function
        self.assertIsInstance(hm.gain_words_from_text(edited_file), list, msg="Returned value from func must be a list")
        for word in hm.gain_words_from_text(edited_file):
            self.assertIsInstance(word, str, msg="Value in list must be a string")
            self.assertTrue(word.isalpha(), msg="Value in list must be from alphabet")

    def test_draw_game_word_from_pool(self):
        # input data
        edited_file = "text.txt"
        pool_of_words = hm.gain_words_from_text(edited_file)
        game_word, word_letters = hm.draw_game_word_from_pool(pool_of_words)
        self.assertIsInstance(game_word, str, msg="Variable game_word must be a str")
        self.assertIsInstance(word_letters, list, msg="Variable word_letters must be a list")
        self.assertIn(game_word, pool_of_words, msg="Word must be from imported file")
        for letter in word_letters:
            self.assertIsInstance(letter, str, msg="Letter in word must be a str")
            self.assertTrue(letter.isalpha(), msg="Value in list must be from alphabet")
            self.assertEqual(len(letter), 1, msg="Every letter must be a single character")

