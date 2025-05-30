"""Prints out a random item from a list"""

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel", "Mike"]
random_integer = random.randint(0, len(friends) - 1)
print(friends[random_integer])

# Alternatively Option 1
# random.choice() function
print(len(friends))
