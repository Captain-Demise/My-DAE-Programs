# Imports the necesary modules
import random
import sys

# Imports the dictionary
from english_words import get_english_words_set
word_list = get_english_words_set(['web2'])
words = list(word_list)
wordle_words= []

# Filters the dictionary for 5 letter words
for word in words:
    if len(word) == 5:
        wordle_words.append(word)

# Generates the word
selected = random.choice(wordle_words)

# Starts the Game
print("Welcome to Wordle but harder.")

# Defines the Guess Number
gnum =0

# Defines Game over as ending the game on a loss
def Game_Over():
     print("The word was",selected,".")
     print("Game over. Try again.")
     sys.exit()

# Allows user to guess the word if they are under 12 guesses
while gnum < 12:
    guess = input("Enter a guess: ")

# Ends the game if the user wins
    if guess == selected:
        print("Congrats, you win!")
        sys.exit()

# Adds to the counter of incorrect guesses
    elif guess != selected:
        if len(guess) == len(selected):
             gnum +=1
             print("Guess #",gnum,":")

# Shows what letters are in the correct spots
             for index, (secret_char, guess_char) in enumerate(zip(selected, guess)):
                 if secret_char == guess_char:
                     print(f"Match found! '{guess_char}' at space {index + 1}")

# Ivalidates words that exceed or understeps 5 letters
        elif len(guess) != len(selected):
                     print("That guess is invalid. Try again.")

# Ends the game if the user runs out of guesses
if gnum >= 12:
     Game_Over()