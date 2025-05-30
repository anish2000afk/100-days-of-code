import random

words = ["paper", "rock", "scissors"]
chosen_word = random.choice(words)
print(chosen_word)

guess = input("Enter a letter of the of the word ").lower()
for i in chosen_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
