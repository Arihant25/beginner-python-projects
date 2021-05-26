alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""

    if shift_amount > 26:
        shift_amount %= 26

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print("""           
                                                                                                             
                                                                                                             
    //   ) )                                                  //   ) )                                       
   //         ___      ___      ___      ___      __         //             ___     / __      ___      __    
  //        //   ) ) //___) ) ((   ) ) //   ) ) //  ) )     //   //   / / //   ) ) //   ) ) //___) ) //  ) ) 
 //        //   / / //         \ \    //   / / //          //   ((___/ / //___/ / //   / / //       //       
((____/ / ((___( ( ((____   //   ) ) ((___( ( //          ((____/ / / / //       //   / / ((____   //        

""")


restart = 'yes'

while restart == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.").lower()

print("Thank you for using Caesar Cypher 2!")
