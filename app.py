import json
from difflib import get_close_matches

data = json.load(open('data.json'))

word = input('Enter the word : ')

def process_input(word:str):
    word = word.strip().lower()
    return word


def get_result_meaning(word):
    if word in data:
        return data[word]
    possible_words = get_close_matches(word, data.keys())
    if len(possible_words) != 0:
        print(word, "is not found in database. Did you mean \'" + possible_words[0] + "\'?")
        response = input("Press y for YES, or any other key for NO --> ")
        if response.lower()[0] == "y":
            return data[possible_words[0]]
    return "Sorry, the word does not exist in database. Please double-check it."


def show_meaning(word):
    word = process_input(word)
    result = get_result_meaning(word)
    if type(result) == str:
        print(result)
    else:
        print()
        for meaning in result:
            print(meaning)
        print()

show_meaning(word)

