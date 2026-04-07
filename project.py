import random
import math
import sys

# Function to load only 100 words from the file (or select a subset if more than 100)
def load_words(file_path):
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    # Ensure that we have exactly 100 words (randomly selected if more than 100)
    if len(words) > 100:
        words = random.sample(words, 100)  # Select 100 random words from the list
    return words

# Function to get a random word and its placeholder hint (can be customized)
def get_word_and_hint(words_list):
    random_word = random.choice(words_list)

    # Placeholder hint: in this case, just use the word length as a hint
    hint = f"The word has {len(random_word)} letters"

    return random_word.upper(), hint

# Function to check if input is valid (alphabetic and single character)
def is_valid_input(input_char):
    return len(input_char) == 1 and input_char.isalpha()

# Main function where game logic resides
def play_game(difficulty):
    words_list = load_words("words_alpha.txt")  # Load 100 words from the file
    word_to_guess, hint = get_word_and_hint(words_list)
    guessed_letters = []
    attempts_remaining = int(math.ceil(len(word_to_guess) / 1.25 + (5 - difficulty)))  # Difficulty-based attempts
    display_word = ['_' for _ in range(len(word_to_guess))]

    print(f"Attempts available: {attempts_remaining}")

    while attempts_remaining > 0:
        print(f"Hint: {hint}")
        print(' '.join(display_word))
        guess = input("Guess a letter: ").upper()

        try:
            if not is_valid_input(guess):
                raise ValueError("Please enter a single alphabetic character.")
            if guess in guessed_letters:
                raise ValueError("You have already guessed that letter.")
            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Correct!")
                # Update display_word with correct guesses
                for index, letter in enumerate(word_to_guess):
                    if letter == guess:
                        display_word[index] = guess
                # Check if player has won (no more '_' in display_word)
                if '_' not in display_word:
                    print(f"Congratulations! You've guessed the word: {word_to_guess}")
                    sys.exit("Thanks for playing!")
                    break
            else:
                print("Incorrect!")
                attempts_remaining -= 1
            print(f"Attempts remaining: {attempts_remaining}")

        except ValueError as e:
            print(e)

    if attempts_remaining == 0:
        print(f"Game Over! The word was: {word_to_guess}")

# Start the game
def main():
    print("Welcome to Word Guessing Game!")
    while True:
        try:
            difficulty = input("Please select a difficulty (1-5): ")
            difficulty = int(difficulty)
            if difficulty < 1 or difficulty > 5:
                raise ValueError("Please select a difficulty between 1 and 5.")
            input("<<< Press enter to start >>>")
            play_game(difficulty)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
