import pandas


nato_alphabet_dict = {value.letter: value.code for (key, value) in
                      pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

word_in_nato = None

while word_in_nato is None:
    try:
        word_in_nato = [nato_alphabet_dict[letter] for letter in input("Please say your word: ").upper()]
    except KeyError:
        print("Sorry, only letter of the alphabet are allowed!")
    else:
        print(word_in_nato)
