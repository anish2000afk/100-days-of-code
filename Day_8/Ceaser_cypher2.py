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


direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(direction, text, shift):

    def encrypt(text, shift):
        encrypted_word = ""
        for i in text:
            new_index = alphabet.index(i) + shift
            if new_index >= 26:
                new_index %= 26
                # Indexing for a list starts from 0.
                encrypted_word += alphabet[new_index]
            else:
                encrypted_word += alphabet[new_index]
            # Alternatively  new_index %= len(alphabet)
        print(encrypted_word)

    def decrypt(text, shift):
        encrypted_word = ""
        for i in text:
            new_index = alphabet.index(i) - shift
            new_index %= len(alphabet)
            encrypted_word += alphabet[new_index]
        print(encrypted_word)

    if direction == "encode":
        encrypt(text, shift)
    if direction == "decode":
        decrypt(text, shift)


ceaser(direction, text, shift)

# Much cleaner version
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:
#
# # The only thing that is changing is the shift being negative.
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
#
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
