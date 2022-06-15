# Importing Libraries
import pandas as pd

# Constants
NATO_PHONETIC_FILE = "nato_phonetic_alphabet.csv"


nato_df = pd.read_csv(NATO_PHONETIC_FILE)

nato_code_dict = {row["letter"]: row["code"] for (index, row) in nato_df.iterrows()}

user_input = input("Enter a word: ")

nato_code_list = [nato_code_dict[letter.upper()] for letter in user_input]

print(nato_code_list)
