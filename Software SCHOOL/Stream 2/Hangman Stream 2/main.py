import json
import utils
import random
class Hangman:
    def __init__(self, word:str, totalPoints) -> None:
        self.word = word
        self.guesses = set()
        self.points = totalPoints
        self.progress = 0
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
        display += "\n"
        display += f"guesses used: {' '.join(map(str, sorted(self.guesses)))}"
        return display

def load_game_data(): #loads and acceses database
    with open('/Users/ronitbhandari/Desktop/Projects/Software SCHOOL/Stream 2/Hangman Stream 2/Word Lists/data.json', 'r') as file:
        game_data = json.load(file)
    words = game_data['words']
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

word, maxPoints = chooseDif()
currentGame = Hangman(word, maxPoints)
while True:
    print(currentGame.processGuess(input("guess: ")))
    isEnd = currentGame.checkForEnd()
    if isEnd[0] == True:
        if isEnd[1] == "W":
            print("You won! ")
        elif isEnd[1] == "L":
            print("You Lost! ")
        break
    print(currentGame.renderWord())

