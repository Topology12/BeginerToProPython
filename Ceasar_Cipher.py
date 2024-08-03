alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift_amount):
    encrypt_text = ''
    for letter in text:
        idx = alphabet.index(letter)
        encrypt_text += alphabet[idx + shift_amount]
    print(encrypt_text)


def decrypt(text, shift_amount):
    decrypt_text = ''
    for letter in text:
        idx = alphabet.index(letter)
        decrypt_text += alphabet[idx + 26 - shift_amount]
    print(decrypt_text)


def caesar(direction, text, shift):
    process_text = ''
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_position = index + shift
            process_text += alphabet[new_position]
        else:
            process_text += char
    print(process_text)


stop = True
while stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('Type your message:\n')
    shift = int(input('Type the shift number:\n'))
    shift %= 26
    caesar(direction, text, shift)
    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if cont == "no":
        stop = False
