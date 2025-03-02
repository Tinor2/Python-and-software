import json
import os
import string

def load_json_data(): #loads and acceses database
    with open('/Users/ronitbhandari/Desktop/Projects/Software SCHOOL/Stream 2/Hangman Stream 2/Wordlist filtering/RawDictionary.json', 'r') as file:
        game_data = json.load(file)
    return game_data
json_words= dict(load_json_data())

filtered_data = {}
current_word_list = {}

current_initial ="a"
alphabet = list(string.ascii_lowercase)
print(current_initial)
# print(sorted((list(json_words.keys())))[:100])
for word in sorted((list(json_words.keys()))):
    if word[0] != current_initial or current_initial == alphabet[-1:]:
        print(f"{list(current_word_list.keys())[:10]} ... {list(current_word_list.keys())[-10:]}\n")
        filtered_data[current_initial] = current_word_list
        try:    
            current_initial = alphabet[alphabet.index(current_initial)+1] # update current inital to next letter
            print(current_initial)
        except IndexError:
            break 
        current_word_list = {}
    if len(word) == 1:
        continue   
    current_word_list[word] = 1 # placeholder value)
# print(filtered_data)

# def create_json_file():
#     # Sample data structure
#     data = {}
    
#     # Define the file path
#     file_path = "/Users/ronitbhandari/Desktop/Projects/Software SCHOOL/Stream 2/Hangman Stream 2/Wordlist filtering/filtered_words.json"
    
#     # Create directory if it doesn't exist
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
#     # Write the JSON file with proper formatting
#     with open(file_path, 'w') as json_file:
#         json.dump(data, json_file, indent=4)
        
#     print(f"JSON file created at: {file_path}")

# # Create the file
# create_json_file()