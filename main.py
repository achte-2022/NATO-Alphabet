# Importing Libraries
import pandas as pd

# Constants
NATO_PHONETIC_FILE = "nato_phonetic_alphabet.csv"


def print_nato_code(word, nato_code_dict):
    nato_code_list = []

    for letter in word:
        try:
            nato_code = nato_code_dict[letter.upper()]
            nato_code_list.append(nato_code)
        except:
            print("Error: Your word has number in it.")
            return
    print(nato_code_list)
    return


nato_df = pd.read_csv(NATO_PHONETIC_FILE)

nato_code_dict = {row["letter"]: row["code"] for (index, row) in nato_df.iterrows()}

user_input = input("Enter a word: ")

print_nato_code(user_input, nato_code_dict)
