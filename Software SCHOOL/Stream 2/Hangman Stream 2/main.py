import json
import utils
import random
class Hangman:
    def __init__(self, word:str, totalPoints) -> None:
        self.word = word
        self.guesses = set()
        self.points = totalPoints
        self.progress = 0
        self.formatting = utils.Formatting()
    def checkForEnd(self): #uses self.word, self.guesses, self.points
        # print(f"word: {sorted(set(self.word))}, guesses used: {sorted(self.guesses)}")
        if self.points <= 0:
            return True, "L" #loss
        elif  set(sorted(self.word)) <= set(sorted(self.guesses)): #note: Not scalable
            return True,"W"
        else:
            return False,"-"
    def processGuess(self, guess:str): #uses guess, self.guesses, self.word, self.points
        if len(guess) == 1:
            if guess in self.guesses: # is a in {...}
                self.guesses.add(guess) 
                self.points -= 10
                print(f"Total points: {self.points}")
                return "Already used letter, loose a life"
            elif guess not in self.word:
                self.guesses.add(guess) 
                self.points -= 10
                print(f"Total points: {self.points}")
                return "Wrong choice, loose a life"    
            else:
                self.guesses.add(guess)
                self.points += 10
                print(f"Total points: {self.points}")
                return "Correct Choice!"
        else:
            if self.word == guess:
                for letter in guess: self.guesses.add(letter)
                self.points += 10
                return "Correct, Win condition"
            else:
                self.points -= 10
                print(f"Total lives left: {self.points}")
                return "Wrong choice, loose a life"
    def renderWord(self): # uses self.word, self.guesses
        display = ""
        for char in self.word: # could be simplified to collection
            if char in self.guesses:
                display += f" {char} "
            else:
                display += " _ "
        display = self.formatting.colors(display,"green")
        display += "\nletters guessed: "

        for used_letter in sorted(self.guesses):
            if used_letter in self.word:
                display += self.formatting.colors(used_letter,"cyan")
            else:
                display += self.formatting.colors(used_letter,"red") #sort guesses taken alpahbetically, convert into a string. Also render it in a different color
            display += " "       
        return display

def load_game_data(): #loads and acceses database
    with open('/Users/ronitbhandari/Desktop/Projects/Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/data.json', 'r') as file:
        game_data = json.load(file)
    words = game_data['all_words']
    difficulties = game_data['difficulties']
    return (words, difficulties)
def chooseDif(): # uses loaded data
    allWords, difficultyOptions= load_game_data()
    options = []
    for difficulty in difficultyOptions.values():
        options.extend(difficulty["shortcuts"])
    while True:
        userChoice = input("Choose a difficulty: ").lower()
        if userChoice in options:
            if userChoice in difficultyOptions["easy"]["shortcuts"]:
                finalDifficulty = "easy"
            elif userChoice in difficultyOptions["medium"]["shortcuts"]:
                finalDifficulty = "medium"
            elif userChoice in difficultyOptions["hard"]["shortcuts"]:
                finalDifficulty = "hard"
            else:
                print("Invalid Difficulty, try again. ")
                continue
            break
        else:
            print("Invalid Difficulty, try again. ")
    return (random.choice(allWords[finalDifficulty]), difficultyOptions[finalDifficulty]["points"])
def write_new_words(new_word = None):
    if new_word == "QUIT":
        print("Exiting edit list mode ")
        return True # Function ends in a way the user intends
    if new_word == None or not new_word.isalpha(): # If the input had symbols/digits, or if it was just nothing, then break the function
        print("Enter a valid value")
        return False # Indicates that the function was not succesful
    with open('Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/data.json','r') as word_file:
        word_file_info = json.load(word_file)
    difficulty_lengths = {}
    for difficulty in word_file_info["difficulties"].keys():
        difficulty_lengths[difficulty] = difficulty['word_length'][1] 

    valid_word = False
    if len(new_word)<word_file_info["difficulties"]['word_length']["easy"][0]: #break if the suggested word is too small
        print("Enter a word with the correct length")
        return False 
    
    for difficulty, length_of_word in difficulty_lengths.items():
        if len(new_word) < length_of_word:
            word_file_info['all_words'][difficulty].append(new_word)
            valid_word = True
            break
    if not valid_word: # length of word is out of bounds --> break the function
        print("Enter a word with the correct length")
        return False
    with open('Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/data.json','w') as overwrite_file:
        json.dump(word_file_info, overwrite_file, indent=4) #overwrite the file with the updated word list
    word_file_info = None
    return True # function is executed normally
while True:
    game_state = input("Start a new game, or update word list? ").lower()
    if game_state in ["start","update","s","u"]:
        if game_state in ['start','s']:
            break
        elif game_state in ["update", "u"]:
            while True:
                if write_new_words(input("Add a new word (type QUIT to exit edit mode): ")):
                    break # if the function breaks predictably, end normally
word, maxPoints = chooseDif()
currentGame = Hangman(word, maxPoints)
print(currentGame.renderWord())
while True:
    print(currentGame.processGuess(input("guess: ")))
    isEnd = currentGame.checkForEnd()
    print(currentGame.renderWord())
    if isEnd[0] == True:
        if isEnd[1] == "W":
            print("You won! ")
        elif isEnd[1] == "L":
            print("You Lost! ")
        # TODO: render the word at the very end
        break

