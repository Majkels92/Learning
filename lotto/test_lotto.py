import unittest
import lotto


class Test_lotto(unittest.TestCase):

    def test_duze_lotto(self):
        self.assertIsInstance(lotto.duze_lotto(), list, msg="Result is not a list")
        self.assertEqual(len(lotto.duze_lotto()), 6, msg="Result has not 6 numbers")

    def test_mini_lotto(self):
        self.assertIsInstance(lotto.mini_lotto(), list, msg="Result is not a list")
        self.assertEqual(len(lotto.mini_lotto()), 5, msg="Result has not 5 numbers")


if __name__ == '__main__':
    unittest.main()