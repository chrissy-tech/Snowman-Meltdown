import random

from ascii_art import STAGES

# list of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "game",
         "codio", "play", "function", "code", "programming"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word,
                       guessed_letters, max_mistakes):
    """Display the snowman stage for the current number of mistakes."""
    print(
        "\n" + "=" * 50)  # clear screen (for better readability)

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("WORD: ", display_word, '\n')
    print(f"MISTAKES: {mistakes}/{max_mistakes}")

    """prints the choosen letter (if right or wrong) that user see what 
        he already guessed"""
    if guessed_letters:
        sorted_guesses = sorted(guessed_letters)
        print(f"GUESSED: {', '.join(sorted_guesses)}")
    else:
        print("GUESSED: No letters guessed yet")

    print("=" * 50)


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    #Welcome Text of the game
    print("🎯 Welcome to Snowman Meltdown! 🎯")
    print("Guess the word before the snowman melts! ❄️")

    print(STAGES[mistakes])

    # display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters,
                       max_mistakes)

    # main game loop
    while mistakes < max_mistakes:

        # get user input
        guess = input("Guess a letter: ").lower().strip()

        # input validation
        if not guess.isalpha():
            print("❌ You must enter a letter.")
            continue
        if len(guess) != 1:
            print("❌You must enter exactly 1 letter.")
            continue

        if guess in guessed_letters:  # was letter guessed already
            print("❌ You already guessed that letter!")
            continue

        guessed_letters.append(guess) # if letter is new- add to list
        print("You guessed:", guess)

        if guess not in secret_word:  # proof if letter right/wrong
            mistakes += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")
        else:
            print(f"✅ Correct! '{guess}' is in the word.")

        print(STAGES[mistakes])  # print stages after every guess

        # show recent status
        display_game_state(mistakes, secret_word, guessed_letters,
                           max_mistakes)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations, you saved the ☃️! 🎉")
            print(f"🏆 The word was: {secret_word.upper()}")
            break

        # Check lose condition
        if mistakes == max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters,
                               max_mistakes)
            print("❌---- GAME OVER ---- ❌")
            print("The snowman melted! ☃️💦")
            print(f"💡 The secret word was: {secret_word.upper()}")
            break

        # Play again question after win OR lose
    play_again = input(
        "\nDo you want to play again? \n"
        "Press 'Y' for YES and 'N' for NO.\n").lower().strip()

    if play_again == "y":
        print("\n" + "=" * 50)
        print("Starting new game...")
        print("=" * 50 + "\n")
        play_game()  # Start new game
    else:
        print("Thanks for playing! 👋")
        return  # Exit the game
