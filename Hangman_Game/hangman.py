import random

# List of words
words = ["apple", "python", "mango", "laptop", "mobile"]

# Select a random word
secret_word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0

# Welcome Message
print("=" * 40)
print("         HANGMAN GAME")
print("=" * 40)

while True:

    # Display current word
    word_display = ""

    print("\nWord:")
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
            word_display += letter
        else:
            print("_", end=" ")
            word_display += "_"

    print("\n")

    # Win Condition
    if "_" not in word_display:
        print("Congratulations! You Won!")
        print("The word was:", secret_word)
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Check duplicate guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Save guess
    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses)
        print("Remaining chances:", 6 - wrong_guesses)

    # Lose Condition
    if wrong_guesses == 6:
        print("\nGame Over!")
        print("The word was:", secret_word)
        break

    # Show guessed letters
    print("Guessed letters:", guessed_letters)