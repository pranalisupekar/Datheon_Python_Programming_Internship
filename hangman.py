
import random

print("Welcome to the Hangman Game!")

# Hangman drawings for 0 to 6 wrong guesses
stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

with open("words.txt", "r") as file:
    words = [
        word.strip().upper()
        for word in file
        if word.strip().isalpha()
        and 4 <= len(word.strip()) <= 10
    ]

secret_word = random.choice(words).upper()

display_word = ["_"] * len(secret_word)
guessed_letters = set()
attempts = 6

while "_" in display_word and attempts > 0:

    print(stages[6 - attempts])
    print("Word:", " ".join(display_word))
    print("Attempts remaining:", attempts)
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))

    guess = input("Enter a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in display_word:
    print("\nCongratulations! You guessed the word!")
else:
    print(stages[6])
    print("\nGame Over!")
    print("The secret word was:", secret_word)

print("Final word:", " ".join(display_word))
