from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    return f"The {cipher_direction} text is: {end_text}."


to_continue = True
while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    answer = caesar(start_text = text, shift_amount=shift, cipher_direction=direction)
    print(answer)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        to_continue = False
        print("Goodbye")
