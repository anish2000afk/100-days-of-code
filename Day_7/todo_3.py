import random

"""My code """
"""
# Choosing a word
words = ["paper", "rock", "scissors"]
chosen_word = random.choice(words)
print(chosen_word)
placeholder = ""
# Creating blanks
for i in range(len(chosen_word)):
    placeholder += "-"
print(placeholder)

# Creating the display1 function
# Play with the idea of another variable called display2.
display2 = ""
display1 = ""
while display2 != chosen_word:
    display2 = ""
    guess = input("\nEnter a letter of the word ").lower()
    for i in chosen_word:
        if i == guess:
            display2 += i
            display1 += i
        elif i in display1:
            display2 += i
        else:
            display2 += "-"
    print(display2)
print("You win !")"""

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
