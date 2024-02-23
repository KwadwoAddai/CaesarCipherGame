from art import logo, alphabet


print(logo)
def caesar(text,shift,direction):
    result = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_pos = position+shift
            elif direction == 'decode':
                new_pos = position-shift
            else:
                print("Invalid response")
            new_char = alphabet[new_pos]
            result += new_char
        else:
            result += char
    print(f"The {direction}d text {text} became {result}")

while True:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26

    caesar(text,shift,direction)
    play = input("ANOTHER MESSAGE (yes/no)?: ").lower()
    if play == 'yes':
        print("WE GO AGAIN")
    else:
        print("ANOTHER TIME")
        break


