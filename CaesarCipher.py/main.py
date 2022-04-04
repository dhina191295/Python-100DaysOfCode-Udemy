from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    result_text = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    for letter in plain_text:
        if letter.isdigit() or letter == " ":
            result_text += letter
        else:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                position += shift_amount
                if position > 25:
                    position -= 26
            elif cipher_direction == "decode":
                position -= shift_amount
                if position < 0:
                    position += 26
            result_text += alphabet[position]

    if result_text != "":
        print(f"The {direction}d text is {result_text}")


print(logo)

exit_flag = False

while not exit_flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if (direction == "encode") or (direction == "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("Please enter only encode or decode. Check for spelling errors.")

    restart_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart_input == "no":
        exit_flag = True
        print("Good Bye")

# def encrypt(text,shift):
#     encrypted_text = ""
#     for char in text:
#         # print(char)
#         position = alphabet.index(char)
#         position += shift
#         if position > 25:
#             position -=  26
#             # print(position)
#         encrypted_text += alphabet[position]
#     print(f"The encoded text is {encrypted_text}")

# def decrypt(text,shift):
#     decrypted_text = ""
#     for char in text:
#         position = alphabet.index(char)
#         position -= shift
#         if position < 0:
#             position += 26
#         decrypted_text += alphabet[position]
#     print(f"The decoded text is {decrypted_text}")

# if direction == "encode":
#     encrypt(text,shift)
# elif direction == "decode":
#     decrypt(text,shift)
