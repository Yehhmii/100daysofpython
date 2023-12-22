alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(cipher_direction, start_text, shift_count):
    end_text = ""
    if cipher_direction == "decode":
            shift_count *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)    
            new_position = position + shift_count
            end_text += alphabet[new_position]   
        else:
             end_text += char     
    print(f"The {cipher_direction}d text is {end_text}")        

again = True
while again:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the number of shift you want: \n"))

    shift = shift % 26
    caesar(cipher_direction=direction, start_text=text, shift_count=shift)

    result = input("Type 'yes' if you want to go again, Otherwise type 'no'. \n ")
    if result == "no":
        again = False
        print("Goodbye")





# long method
# def encrypt(text_params, shift_params):
#     cipher_text = ""
#     for char in text_params:
#         position = alphabet.index(char)
#         new_position = position + shift_params
#         new_char = alphabet[new_position]
#         cipher_text += new_char
#     print(f"The encoded text is {cipher_text}")


# def decrypt(decrypt_text, shift_params):
#     normal_text = ""
#     for char in decrypt_text:
#         position = alphabet.index(char)
#         new_position = position - shift_params
#         new_char = alphabet[new_position]
#         normal_text += new_char
#     print(f"The decoded text is {normal_text}")


# if direction == "encode":
#     encrypt(text_params = text, shift_params = shift)
# elif direction == "decode":
#     decrypt(decrypt_text = text, shift_params = shift)

