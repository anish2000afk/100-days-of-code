"""Logic for winner of RPS"""

"""
import random
list = [rock ,paper, scissor] 
user_choice = input(User input)
print(user_choice)
computer_choice = random.choice(list)
print(computer_choice)

# Instances where you win
if user_choice == 0 and computer_choice == scissor:
elif user_choice == 1 and computer_choice == rock:
elif user_choice == 2 and computer_choice == paper:

# instances when you draw
if user_choice == computer_choice
print("You draw")

# instances where you lose
else:
print("You lose")
"""


import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
action = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. ")
)
if user_choice == 0 or user_choice == 1 or user_choice == 2:
    print(action[user_choice])
    computer_choice_integer = random.randint(0, 2)
    computer_choice = action[computer_choice_integer]
    print("Computer chose :\n", computer_choice)

    # Instances where you win
    if user_choice == 0 and computer_choice_integer == 2:
        print("You win")
    elif user_choice == 1 and computer_choice_integer == 0:
        print("You win")
    elif user_choice == 2 and computer_choice_integer == 1:
        print("You win")

    # instances when you draw
    elif user_choice == computer_choice_integer:
        print("You draw")

    # instances where you lose
    else:
        print("You lose")
else:
    print("Wrong input")
