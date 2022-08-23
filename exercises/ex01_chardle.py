"""EX01 - Chordle - A cute step toward Wordle."""

__author__ = "730575620"

chordle_word = str(input("Enter a 5-character word: "))
if len(chordle_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chordle_letter = str(input("Enter a single character: "))
if len(chordle_word) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + chordle_letter + " in " + chordle_word)

number_matching = int(0)
for i in range(5):
    if chordle_word[i] == chordle_letter:
        number_matching = number_matching + 1
        print(chordle_letter + " found at index " + str(i))

if number_matching == 1:    
    print(str(number_matching) + " instance of " + chordle_letter + " found in " + chordle_word)
elif number_matching == 0:
        print("No instances of " + chordle_letter + " found in " + chordle_word)
else:
    print(str(number_matching) + " instances of " + chordle_letter + " found in " + chordle_word)
