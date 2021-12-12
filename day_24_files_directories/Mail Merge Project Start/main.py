# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
letter_path = './Input/Letters/starting_letter.txt'
names_path = './Input/Names/invited_names.txt'
letter_out_path = './Output/ReadyToSend/letter_for_'

with open(letter_path, 'r') as let:
    letter = let.read()

with open(names_path, 'r') as name_data:
    for name in name_data.readlines():
        name = name.strip()
        new_letter = letter.replace('[name]', name)

        with open(f'{letter_out_path}{name}.txt', 'w') as write_letter:
            write_letter.write(new_letter)
