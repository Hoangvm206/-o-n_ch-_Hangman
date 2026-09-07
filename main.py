import random
from pathlib import Path

from game import HangmanGame


import random
from game import HangmanGame


def load_words():
    words = []
    with open("words.txt", "r", encoding="utf-8") as file:
        for line in file:
            cleaned_word = line.strip().lower()
            if cleaned_word:
                words.append(cleaned_word)

    if len(words) < 30:
        raise ValueError("File words.txt phải có ít nhất 30 từ")

    return words


def show_state(game):
    if game.guessed_letters:
        guessed = ", ".join(sorted(game.guessed_letters))
    else:
        guessed = "chưa có"

    if game.wrong_letters:
        wrong = ", ".join(sorted(game.wrong_letters))
    else:
        wrong = "chưa có"

    print(f"\nTừ bí mật: {game.word_state}")
    print(f"Các chữ đã đoán: {guessed}")
    print(f"Các chữ đoán sai: {wrong}")
    print(f"Số lượt còn lại: {game.remaining_turns}")


def play(words):
    game = HangmanGame(random.choice(words))

    while not game.is_over:
        show_state(game)
        user_input = input("Nhập một chữ cái: ")
        result = game.guess(user_input)

        if result == "invalid":
            print("Input không hợp lệ. Hãy nhập đúng một chữ cái.")
        elif result == "duplicate":
            print("Chữ này đã được đoán. Bạn không bị trừ lượt.")
        elif result == "correct":
            print("Đoán đúng!")
        else:
            print("Đoán sai! Bạn bị trừ 1 lượt.")

    show_state(game)
    if game.is_won:
        print(f"\nBạn thắng! Từ bí mật là: {game.secret_word}")
    else:
        print(f"\nBạn thua! Từ bí mật là: {game.secret_word}")


def main():
    words = load_words()
    print("=== TRÒ CHƠI ĐOÁN CHỮ ===")

    while True:
        play(words)
        again = input("\nBạn có muốn chơi lại không? (y/n): ").strip().lower()
        if again != "y":
            print("Cảm ơn bạn đã chơi!")
            break


if __name__ == "__main__":
    main()