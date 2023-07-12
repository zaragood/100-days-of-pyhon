alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)


#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. 
def encrypt(para_text, para_shift):
    encryted_text = ""
    for letter in para_text:
        if letter in para_text:
            index_position = alphabet.index(letter)
            new_position = index_position + para_shift
            encryted_letter = alphabet[new_position]
            encryted_text += encryted_letter
        else:
            encryted_text += letter
    print(f"the encoded text is {encryted_text}")    


#Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(dec_text, dec_shift):
    decrypted_text = ""
    for letter in dec_text:
        if letter in dec_text:
            index_postion = alphabet.index(letter)
            new_position = index_postion - dec_shift
            decrypted_letter = alphabet[new_position]
            decrypted_text += decrypted_letter
        else:
            decrypted_text += letter
    print(f"the decoded text is {decrypted_text}")
    
continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    #Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
    #Then call the correct function based on that 'drection' variable


    if direction == "encode":
        encrypt(para_text=text, para_shift=shift)
        
    elif direction == "decode":
        decrypt(dec_text=text, dec_shift=shift)
    else:
        print("Ivalide choice try again")
    
    choice = input("Type 'Yes' if You want to go agian, Otherwise type 'No'. ").lower()
    if choice == "yes":
        continue_game = True
        print("lets try again")
        
    else:
        continue_game = False
        print("Good bye")
        