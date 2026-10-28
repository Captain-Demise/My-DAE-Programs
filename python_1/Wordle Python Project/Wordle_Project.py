# Setup and word import
import random
import sys
from english_words import get_english_words_set
word_list = get_english_words_set(['web2'])
words = list(word_list)
wordle_words= []
for word in words:
    if len(word) == 5:
        wordle_words.append(word)

# Generating the word
selected = random.choice(wordle_words)
print("Welcome to Wordle but harder.")
gnum =0
def Game_Over():
     print("The word was",selected,".")
     print("Game over. Try again.")
# Inputting guesses
while gnum < 12:
    guess = input("Enter a guess: ")
    if guess == selected:
        print("Congrats, you win!")
        sys.exit()
    elif guess != selected:
        if len(guess) == len(selected):
             gnum +=1
             print("Guess #",gnum,":")
             for index, (secret_char, guess_char) in enumerate(zip(selected, guess)):
                 if secret_char == guess_char:
                     print(f"Match found! '{guess_char}' at space {index + 1}")
        elif len(guess) != len(selected):
                     print("That guess is invalid. Try again.")

# Ending the game on a loss
if gnum >= 12:
     Game_Over()