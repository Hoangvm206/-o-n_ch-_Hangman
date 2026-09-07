class HangmanGame:
    """Phần luật chơi Hangman, không input hoặc print."""

    max_wrong = 6
    auto_char = {" ", "-"}

    def __init__(self, secret_word):
        word = secret_word.strip().lower()
        if not word or not all(
            ch.isalpha() or ch in self.auto_char for ch in word
            ):
            raise ValueError(
                "Từ bí mật chỉ được chứa chữ cái, khoảng trắng hoặc dấu gạch ngang"
            )

        self.secret_word = word
        self.guessed_letters = set()
        self.wrong_letters = set()

    @property
    def remaining_turns(self):
        return self.max_wrong - len(self.wrong_letters)

    @property
    def word_state(self):
        result = []
        for letter in self.secret_word:
            if letter in self.guessed_letters or letter in self.auto_char:
                result.append(letter)
            else:
                result.append("_")

        return " ".join(result)

    @property
    def is_won(self):
        for letter in self.secret_word:
            if letter in self.auto_char:
                continue
            if letter not in self.guessed_letters:
                return False
        return True

    @property
    def is_lost(self):
        return self.remaining_turns == 0 and not self.is_won

    @property
    def is_over(self):
        return self.is_won or self.is_lost

    def guess(self, value):
        """Đoán một chữ và trả về trạng thái của lượt đoán."""

        if self.is_over:
            return "game_over"

        letter = value.strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            return "invalid"
        if letter in self.guessed_letters:
            return "duplicate"

        self.guessed_letters.add(letter)
        if letter in self.secret_word:
            return "correct"

        self.wrong_letters.add(letter)
        return "wrong"