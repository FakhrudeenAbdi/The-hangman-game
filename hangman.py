import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "developer", "computer", "software", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '-' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word correctly.")
    print(display_word(word, guessed_letters))

    while wrong_attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong_attempts += 1
            print(f"Wrong guess! You have {max_attempts - wrong_attempts} attempts left.")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if '-' not in current_display:
            print("Congratulations! You guessed the word correctly.")
            break
    else:
        print(f"You lost! The word was: {word}")

if __name__ == "__main__":
    hangman()
