import utils
class Hangman:
    def __init__(self, word:str, totalLives) -> None:
        self.word = word
        self.guesses = set()
        self.lives = totalLives
        self.progress = 0
    def checkForEnd(self):
        print(f"word: {sorted(set(self.word))}, guesses used: {sorted(self.guesses)}")
        if self.lives <= 0:
            return True, "L" #loss
        elif  set(sorted(self.word)) <= set(sorted(self.guesses)): #note: Not scalable
            print("Win cond")
            return True,"W"
        else:
            return False,"-"
    def processGuess(self, guess:str):
        if len(guess) == 1:
            self.guesses.add(guess)
            if guess in self.guesses:
                self.lives -= 1
                print(f"Total lives left: {self.lives}")
                return "Already used letter, loose a life"
            elif guess not in self.word:
                self.lives -= 1
                print(f"Total lives left: {self.lives}")
                return "Wrong choice, loose a life"    
        else:
            if self.word == guess:
                for letter in guess: self.guesses.add(letter)
                return "Correct, Win condition"
            else:
                self.lives -= 1
                print(f"Total lives left: {self.lives}")
                return "Wrong choice, loose a life" 
        return "Correct Choice!" #Before the next guess is called, checkForEnd() should be called again, and we should check if the game should end or not
    def renderWord(self):
        display = ""
        for char in self.word: # could be simplified to collection
            if char in self.guesses:
                display += f" {char} "
            else:
                display += " _ "
        return display

currentGame = Hangman("car", 5)
while True:
    print(currentGame.processGuess(input("guess: ")))
    isEnd = currentGame.checkForEnd()
    print(isEnd)
    if isEnd[0] == True:
        if isEnd[1] == "W":
            print("You won! ")
        elif isEnd[1] == "L":
            print("You Lost! ")
        break
    print(currentGame.renderWord())
'''
Current Bugs:
currentGame.checkForEnd() does not remotely work
typing in "aa" for the target word "car" makes the game think tat
'''
