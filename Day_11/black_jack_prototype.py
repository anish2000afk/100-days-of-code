# flowchart : https://app.diagrams.net/#G1jQQ_fucLSFHGWvjmGGGAXVzC4Uzcqn3u#%7B%22pageId%22%3A%22dRQzXWI49wG0U7cexfld%22%7D
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Build structure 1
answer = input("you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
human_deck = []
computer_deck = []
if answer == "y":
    print(logo)
    for i in range(0, 2):
        human_deck.append(random.choice(cards))
        computer_deck.append(random.choice(cards))
    print(f"Your cards: {human_deck}, current score : {sum(human_deck)} ")
    print(f"Computer's first card: {computer_deck[0]}")
    # print(computer_deck)

    while sum(human_deck) < 21:
        answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if answer == "y":
            random_human_choice = random.choice(cards)
            # Logic for ace
            if random_human_choice == 11:
                if sum(human_deck) > 11:
                    human_deck.append(1)
                else:
                    human_deck.append(random_human_choice)
            else:
                human_deck.append(random_human_choice)
            # print(f"Your hand {human_deck} and sum {sum(human_deck)}")
        else:
            break
    if sum(human_deck) < 21:
        while sum(computer_deck) < 21:
            random_computer_choice_numb = random.randint(1, 2)
            if random_computer_choice_numb == 2:
                random_computer_choice = random.choice(cards)
                # Logic for ace
                if random_computer_choice == 11:
                    if sum(computer_deck) > 11:
                        computer_deck.append(1)
                    else:
                        computer_deck.append(random_computer_choice)
                else:
                    computer_deck.append(random_computer_choice)
            else:
                break
    else:

        print("User went bust.You lose.")
    if sum(computer_deck) > 21:
        print("Computer went bust.You win")
    print(f"Your final hand {human_deck} and your final score : {sum(human_deck)}")
    print(
        f"Computer's final hand {computer_deck} and computer's final score : {sum(computer_deck)}"
    )
if sum(human_deck) and sum(computer_deck) < 21:
    if sum(human_deck) < sum(computer_deck):
        print("You lose")
    else:
        print("You win")
