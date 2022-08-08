import unittest
import lotto


class TestLotto(unittest.TestCase):

    def test_duze_lotto(self):
        self.assertIsInstance(lotto.duze_lotto(), list, msg="Result is not a list")
        self.assertEqual(len(lotto.duze_lotto()), 6, msg="Result has not 6 numbers")
        result = lotto.duze_lotto()
        for i in result:
            self.assertTrue(1 <= i <= 49, msg="Numbers in result are not in array 1-49")

    def test_mini_lotto(self):
        self.assertIsInstance(lotto.mini_lotto(), list, msg="Result is not a list")
        self.assertEqual(len(lotto.mini_lotto()), 5, msg="Result has not 5 numbers")
        bet = lotto.mini_lotto()
        for number in bet:
            self.assertTrue(1 <= number <= 42, msg="Numbers in result are not in array 1-42")

    def test_system_4_mini(self):
        self.assertIsInstance(lotto.system_4_mini(), list, msg="Result is not a list")
        self.assertEqual(len(lotto.system_4_mini()), 8, msg="Result has not 8 lists")

        # validating bets and drawn numbers
        bets = lotto.system_4_mini()
        for bet in bets:
            self.assertIsInstance(bet, list, msg="Result is not a list")
            self.assertEqual(len(lotto.mini_lotto()), 5, msg="Bet has not 5 numbers")
            for number in bet:
                self.assertTrue(1 <= number <= 42, msg="Numbers in result are not in array 1-42")


if __name__ == '__main__':
    unittest.main()
