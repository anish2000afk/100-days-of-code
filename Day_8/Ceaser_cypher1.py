alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_word = ""
    for i in text:
        new_index = alphabet.index(i) + shift
        if new_index >= 26:
            new_index = new_index % 26
            # Indexing for a list starts from 0.
            encrypted_word += alphabet[new_index]
        else:
            encrypted_word += alphabet[new_index]
    print(encrypted_word)


encrypt(text, shift)
