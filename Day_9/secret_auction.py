from art import logo

print(logo)
member = {}


def bid_entry():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    member[name] = bid


should_continue = True
while should_continue:
    bid_entry()
    restart = input("Is there any bidder left. Answer in yes or no. ").lower()
    if restart == "no":
        should_continue = False
    elif restart == "yes":
        print("\n" * 100)

print(member)
z = 0
for i, k in member.items():
    if k > z:
        z = k

for i, k in member.items():
    if k == z:
        print(z)
        print(f"The winner of the bid is {i}")
