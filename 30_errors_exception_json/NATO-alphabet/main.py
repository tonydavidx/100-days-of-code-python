from os import error
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data = {row.letter: row.code for (index, row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_words():
    words = input('enter a word to get phonetic code words: ').upper()
    try:
        code_words = [data[word] for word in words]
    except KeyError:
        print('Please enter a valid word')
        generate_words()
    else:
        print(code_words)


generate_words()
