import pandas

nato_alphabet_dict = {value.letter: value.code for (key, value) in
                      pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
word_in_nato = [nato_alphabet_dict[letter] for letter in input("Please say your word: ").upper()]

print(word_in_nato)
