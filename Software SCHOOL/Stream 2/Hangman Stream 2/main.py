import utils
class Hangman:
    def __init__(self, word:str, totalLives) -> None:
        self.word = word
        self.guesses = set()
        self.lives = totalLives
        self.progress = 0
    def checkForEnd(self):
        if self.lives <= 0:
            return True, "L" #loss
        elif  set(sorted(self.word)) <= set(sorted(self.guesses)): #note: Not scalable
            return True,"W"
        else:
            return False,"-"
    def processGuess(self, guess:str):
        if len(guess) == 1:
            if guess in self.guesses: # is a in {...}
                self.guesses.add(guess) 
                self.lives -= 1
                print(f"Total lives left: {self.lives}")
                return "Already used letter, loose a life"
            elif guess not in self.word:
                self.guesses.add(guess) 
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
        self.guesses.add(guess) 
        return "Correct Choice!" #Before the next guess is called, checkForEnd() should be called again, and we should check if the game should end or not
    def renderWord(self):
        display = ""
        for char in self.word: # could be simplified to collection
            if char in self.guesses:
                display += f" {char} "
            else:
                display += " _ "
        display += "\n"
        display += f"guesses used: {sorted(self.guesses)}"
        return display

currentGame = Hangman("car", 10)
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

