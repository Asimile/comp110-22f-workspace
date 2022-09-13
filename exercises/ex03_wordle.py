"""The true wordle experience"""

__author__ = "730575620"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_guess: str, single_char: str) -> bool:
    """This function searches through a given word for a given single character"""
    assert len(single_char) == 1
    contains_it: bool = False
    i: int = 0
    while i < len(searched_guess):
        if searched_guess[i] == single_char:
            contains_it = True
        i += 1
    if contains_it == True:
        return True
    else:
        return False


def emojified(emoji_guess: str, emoji_secret: str) -> str:
    """For each character of the secret, checks it against the guess
    and converts that index of the guess and secret into the corresponding
    emoji"""
    assert len(emoji_guess) == len(emoji_secret)
    guess_index: int = 0
    wordle_result: str = ""
    while guess_index < len(emoji_secret):
        letter_exists = False
        if emoji_guess[guess_index] == emoji_secret[guess_index]:
            wordle_result += GREEN_BOX
            letter_exists = True
        elif contains_char(emoji_secret, emoji_guess[guess_index]) == True:
            wordle_result += YELLOW_BOX
        else:
            wordle_result += WHITE_BOX
        guess_index += 1
    return wordle_result


def input_guess(guess_length: int) -> str:
    """Asks the user to guess a word the same amount of letters
    as given"""
    guess: str = input(f"enter a {guess_length} character word: ")
    while len(guess) != guess_length:
        guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and the main game loop"""
    secret: str = "codes"
    turn: int = 1
    has_won: bool = False
    while turn < 7 and has_won == False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            has_won = True
        turn += 1
    if has_won == True:
        print(f"You won in {turn - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()