import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print()
    print("Welcome to Snowman Meltdown!")
    print()
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    while True:
        guess = input("Guess a letter: ").lower().strip()
        print("You guessed:", guess)
        if guess == secret_word:
            print("Congratulations, you guessed the secret word!")
            break


def main():

    play_game()


if __name__ == "__main__":
    play_game()