import random

print('''
,------.              ,--.        ,------.                                   ,---.        ,--.                                    
|  .--. ' ,---.  ,---.|  |,-.     |  .--. ' ,--,--. ,---.  ,---. ,--.--.    '   .-'  ,---.`--' ,---.  ,---.  ,---. ,--.--. ,---.  
|  '--'.'| .-. || .--'|     /     |  '--' |' ,-.  || .-. || .-. :|  .--'    `.  `-. | .--',--.(  .-' (  .-' | .-. ||  .--'(  .-'  
|  |\  \ ' '-' '\ `--.|  \  \     |  | --' \ '-'  || '-' '\   --.|  |       .-'    |\ `--.|  |.-'  `).-'  `)' '-' '|  |   .-'  `) 
`--' '--' `---'  `---'`--'`--'    `--'      `--`--'|  |-'  `----'`--'       `-----'  `---'`--'`----' `----'  `---' `--'   `----'  
                                                   `--'                                                                           
''')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_choice = choices[int(
    input("Enter 0 for rock, 1 for paper and 2 for scissors: "))]
computer_choice = choices[random.randint(0, 2)]

print(user_choice)
print("Computer chose:")
print(computer_choice)


if user_choice == computer_choice:
    print("It's a draw.")

elif user_choice == rock and computer_choice == scissors or user_choice == paper and computer_choice == rock or user_choice == scissors and computer_choice == paper:
    print("You win!")

else:
    print("You lose.")
