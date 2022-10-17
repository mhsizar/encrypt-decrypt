import art

print(art.logo)

print("Welcome to Caesar Cipher!\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

repeat=True
while repeat: 
    direction = input("Please type 'encode' to encrypt, or type 'decode' to decrypt:\n").lower()
    while direction!="encode" and direction!="decode":
        print('\nWrong input! Please enter "encode" or "decode"\n')
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input(f"Type the message you want to {direction}: \n").lower()
    try:
        shift = int(input("How many shifts in letters do you want? \n"))%26
    except ValueError:
        print('\nWrong input! Please enter a valid integer.\n')
        shift = int(input("How many shifts in letters do you want? \n"))%26
    def encode_decode(input_text, input_shift, input_direction):
        output_text=""
        if input_direction=="decode":
            input_shift*=-1
        for character in input_text:
            
            if character in alphabet:
                index=alphabet.index(character)
                new_index=index+input_shift
                output_text += alphabet[new_index]
            else:
                output_text+=character
                
        print(f"Here's the {input_direction}d result: {output_text}")
          
    encode_decode(input_text=text, input_shift=shift, input_direction=direction)
    
    repeat = input("\nDo you want to encode/decode something again? Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    if repeat!="yes":
        print("See you again!")
        repeat=False