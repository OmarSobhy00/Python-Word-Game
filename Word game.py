import random

# List of words for the game
word_list = ["apple", "python", "orange", "planet", "jumble", "keyboard", "banana", "giraffe", "bottle", "school"]

def scramble_word(word):
    """Scramble the letters of the word"""
    scrambled = list(word)
    while True:
        random.shuffle(scrambled)
        scrambled_word = ''.join(scrambled)
        if scrambled_word != word:
            return scrambled_word

def play_game():
    """Main logic for a single round of the game"""
    word = random.choice(word_list)
    scrambled = scramble_word(word)
    attempts = 3

    print("\nScrambled word:", scrambled)

    while attempts > 0:
        guess = input("Enter your guess: ").strip().lower()

        if guess == word:
            print("Congratulations! You've guessed the correct word!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess! You have {attempts} attempt{'s' if attempts > 1 else ''} left.")
            else:
                print(f"Out of attempts! The correct word was: '{word}'")

def main():
    """Entry point of the game"""
    print("Welcome to the Word Scramble Game!")
    print("Guess the word from the scrambled letters.")

    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Start the game
if __name__ == "__main__":
    main()