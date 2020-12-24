import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter the word you want to search : ")

def meaning(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead ?\nPress 'y' for yes 'n' for no" %get_close_matches(word, data.keys())[0])
        choice = input()
        if choice == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == 'n':
            return "Sorry! word not found. Please try again"
        else:
            return "Invalid input!  Please try again"
    else:
        return "Sorry! word not found"

output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
