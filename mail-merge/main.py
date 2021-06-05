with open('./Input/Letters/starting_letter.txt') as file:
    starting_letter = file.read()

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

# For each name in invited_names.txt
for name in names:
    name = str(name).strip()
    # Replace the [name] placeholder with the actual name.
    new_letter = starting_letter.replace('[name]', name)
    # Save the letters in the folder "ReadyToSend".
    with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as file:
        file.write(new_letter)






