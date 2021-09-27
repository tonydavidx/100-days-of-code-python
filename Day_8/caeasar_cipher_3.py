alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(input_text, key, mode):
    output = ''
    for letter in input_text:
        if mode == 'encode':
            position = alphabet.index(letter) + key
        else:
            position = alphabet.index(letter) - key
        output += alphabet[position]
    print(f'The {mode}d text is {output}')

    # def encrypt():
    #     cipher_text = ""
    #     for letter in text:
    #         position = alphabet.index(letter)
    #         new_position = position + key
    #         cipher_text += alphabet[new_position]
    #     print(f"The encoded text is {cipher_text}")

    # def decrypt():
    #     plain_text = ""
    #     for letter in text:
    #         position = alphabet.index(letter)
    #         new_position = position - key
    #         plain_text += alphabet[new_position]
    #     print(f"The decoded text is {plain_text}")


caesar(input_text=text, key=shift, mode=direction)
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
