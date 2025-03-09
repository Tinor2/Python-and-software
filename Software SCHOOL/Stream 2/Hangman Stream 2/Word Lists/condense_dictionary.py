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
    with open('Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/raw_dictionary.json', 'r') as file:
        game_data = json.load(file)
    return game_data
def condense_dictionary():
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
def transferData(in_path = None, out_path = None):
    if in_path == None:
        in_path = 'Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/main_dict.json'
    if out_path == None:
        out_path = 'Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/all_words_info.json'
    with open(in_path, "r") as raw_data:
        in_data = json.load(raw_data)
    with open(out_path, "r") as raw_data:
        sorting_info = json.load(raw_data)
    word_lengths = []
    difficulties = list(sorting_info["all_words"].keys())
    word_lists = [[] for _ in range(len(difficulties))] #making things scalable if more difficulties are added
    for key in difficulties:
        word_lengths.append(sorting_info["difficulties"][key]["word_length"][1])
    is_added = False
    word_list = [word for letter in in_data.values() for word in letter.keys()]

    for word in word_list:
        for index, difficulty in enumerate(word_lengths):
            if len(word)<word_lengths[index]: # Get the maxiumum word length for each difficulty from the all_words_info.json file
                word_lists[index].append(word)
                is_added = True
                break
        if not is_added:
            word_lists[-1:].append(word) 
    for index, difficulty in enumerate(difficulties):
        sorting_info["all_words"][difficulty] = word_lists[index]
    with open(out_path, "w") as new_word_lists:
        # overwrite the all_words_info.json file to be the sorting_info variable
        json.dump(sorting_info, new_word_lists, indent=4)


transferData()