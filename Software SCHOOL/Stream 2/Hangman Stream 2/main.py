from formattingText import colors
class Hangman:
    def __init__(self, word, totalLives) -> None:
        self.word = word
        self.guesses = set()
        self.lives = totalLives
        self.progress = 0
    def checkForEnd(self):
        if self.lives <= 0:
            return True, "L" #loss
        elif list(self.guesses).sort() == list(self.word).sort: #note: Not scalable
            return True,"W"
        else:
            return False,"-"
    def processGuess(self, guess):
        if len(guess) == 1:
            if guess in self.guesses:
                self.lives -= 1
                return "Already used letter, loose a life"
            elif guess not in self.word:
                self.lives -= 1
                return "Wrong choice, loose a life"    
            self.guesses.add(guess)
        else:
            if self.word == guess:
                for letter in guess: self.guesses.add(guess)
                if self.checkForEnd() != (True,"W"):
                    self.lives -= 1
                    return "Wrong choice, loose a life"  
        return "Correct Choice!" #Before the next guess is called, checkForEnd() should be called again, and we should check if the game should end or not
    def renderWord(self, iterable):
        display = ""
        for char in iterable: # could be simplified to collection
            if char in self.guesses:
                display += f" % "%char
            else:
                display += " _ "
        return display
    
