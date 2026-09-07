import unittest

from game import HangmanGame


class TestHangmanGame(unittest.TestCase):
    def test_correct_guess(self):
        game = HangmanGame("apple")

        result = game.guess("p")

        self.assertEqual(result, "correct")
        self.assertEqual(game.word_state, "_ p p _ _")
        self.assertEqual(game.remaining_turns, 6)

    def test_wrong_guess(self):
        game = HangmanGame("apple")

        result = game.guess("z")

        self.assertEqual(result, "wrong")
        self.assertEqual(game.remaining_turns, 5)
        self.assertIn("z", game.wrong_letters)

    def test_duplicate_guess(self):
        game = HangmanGame("apple")
        game.guess("z")

        result = game.guess("Z")

        self.assertEqual(result, "duplicate")
        self.assertEqual(game.remaining_turns, 5)

    def test_win(self):
        game = HangmanGame("cat")

        for letter in "cat":
            game.guess(letter)

        self.assertTrue(game.is_won)
        self.assertTrue(game.is_over)

    def test_lose(self):
        game = HangmanGame("cat")

        for letter in "bdefgh":
            game.guess(letter)

        self.assertTrue(game.is_lost)
        self.assertEqual(game.remaining_turns, 0)

    def test_invalid_input_does_not_remove_turn(self):
        game = HangmanGame("apple")

        for value in ("", "ab", "1", "!"):
            self.assertEqual(game.guess(value), "invalid")

        self.assertEqual(game.remaining_turns, 6)
        self.assertEqual(game.guessed_letters, set())

    def test_case_insensitive(self):
        game = HangmanGame("Apple")

        self.assertEqual(game.guess("A"), "correct")
        self.assertEqual(game.word_state, "a _ _ _ _")

    def test_hyphen_and_space_displayed_automatically(self):
        """Dấu '-' và khoảng trắng tự động hiển thị, không bị che thành '_'."""
        game = HangmanGame("t-shirt box")

        self.assertEqual(game.word_state, "_ - _ _ _ _ _   _ _ _")

    def test_win_without_guessing_hyphen(self):
        """Thắng từ có dấu '-' chỉ bằng cách đoán các chữ cái."""
        game = HangmanGame("t-shirt")

        for letter in "tshir":
            game.guess(letter)

        self.assertEqual(game.word_state, "t - s h i r t")
        self.assertTrue(game.is_won)
        self.assertFalse(game.is_lost)

    def test_guess_hyphen_is_invalid(self):
        """Người chơi nhập dấu '-' bị tính là không hợp lệ và không mất lượt."""
        game = HangmanGame("t-shirt")

        self.assertEqual(game.guess("-"), "invalid")
        self.assertEqual(game.remaining_turns, 6)


if __name__ == "__main__":
    unittest.main()