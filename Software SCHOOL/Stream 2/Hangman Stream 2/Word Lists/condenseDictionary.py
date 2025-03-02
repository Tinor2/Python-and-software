'''
- Filter out any words above and below min/max lengths
- Filter out all unnecesary information points
- Sort out different initials into differnt objects
    i.e., the only terms that are useful are:
        word
        href
        examples
'''
import string
import json
def load_json_data(): #loads and acceses database
    with open('Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/RawDictionary.json', 'r') as file:
        game_data = json.load(file)
    return game_data
data = load_json_data()
condensed_words = {}

for wordInfo in data:
    word = wordInfo["value"]["word"]
    if len(wordInfo["value"]["examples"]) > 4:  examples = wordInfo["value"]["examples"][:4]
    else:   examples = wordInfo["value"]["examples"][:4]
    useful_info = {"href":wordInfo["value"]["href"],"examples":examples}
    condensed_words[word.lower()] = useful_info

filtered_data = {}
temp_word_list = {}
word_len_bounds = (3,11)

current_initial ="a"
alphabet = list(string.ascii_lowercase)
sortedWords = sorted(list(condensed_words.keys()))
for word in sortedWords:
    if word[0] != current_initial:
        filtered_data[current_initial] = temp_word_list
        if word == alphabet[-1]:
            break
        temp_word_list = {}
        current_initial = alphabet[alphabet.index(current_initial)+1]
    if word_len_bounds[0] > len(word) or len(word) > word_len_bounds[1]:
        continue # ignore words that are either too long or too short
    if "-" in word:
        continue
    temp_word_list[word] = condensed_words[word]

output_path = 'Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/condensedDictionary.json'
with open(output_path, 'w') as json_file:
    json.dump(filtered_data, json_file, indent=4)

print(f"Dictionary exported to {output_path}")