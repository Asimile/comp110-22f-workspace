"""Like ex01 but better!"""

__author__ = str("730575620")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_index: int = 0
wordle_result: str = ""
letter_exists: bool = False

secret = str("python")
guess = str(input(f"What is your {len(secret)}-letter guess? "))


while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

while guess_index < len(secret):
    letter_exists = False
    if guess[guess_index] == secret[guess_index]:
        wordle_result += GREEN_BOX
        letter_exists = True
    else:
        letter_exists = False
        secret_index = 0
        while letter_exists == False and secret_index < len(secret):
            if guess[guess_index] == secret[secret_index]:
                letter_exists = True
                wordle_result += YELLOW_BOX
            else:
                secret_index += 1
    if letter_exists == False:
        wordle_result += WHITE_BOX
    guess_index += 1

print(wordle_result)


if guess == secret:
    print("Woo! You got it!")
    exit()
else: 
    print("Not quite. Play again soon!")
    exit()