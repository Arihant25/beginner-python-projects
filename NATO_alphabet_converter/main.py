import pandas

# Create a dictionary from the CSV file

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
code_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# Print the code for each letter in input if that letter exists in code_dict
while True:
    try:
        print([code_dict[letter] for letter in input("Enter a word:").upper()])
    except KeyError:
        print("Sorry, only letters are allowed.")
    else:
        break
