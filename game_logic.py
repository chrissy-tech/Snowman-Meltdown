import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):

    """Display the snowman stage for the current number of mistakes."""
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word, '\n')
    print("\n")





def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    print(STAGES[mistakes])

    #display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt user for one guess (logic to be enhanced later)
    while mistakes < max_mistakes:
        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha():
            print("You must enter a letter.")
            continue
        if len(guess) != 1:
            print("You must enter exactly 1 letter.")
            continue

        if guess in guessed_letters: #was letter guessed already
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess) #if letter = new- add to list
        print("You guessed:", guess)

        if guess not in secret_word: #proof if letter right/wrong
            mistakes += 1

        print(STAGES[mistakes]) #print stages after every guess

            #show recent status
        display_game_state(mistakes, secret_word, guessed_letters)

        """checks if all letter were guessed"""
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations, you saved the ☃️! 🎉")
            break

        # check if Stages of mistake were
        if mistakes == max_mistakes:
            print("❌---- GAME OVER ---- ❌")
            print(f"The secret word was: {secret_word}")
            break


