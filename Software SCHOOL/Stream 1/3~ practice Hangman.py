import random
import string
class invalidGuess(Exception): pass
def colors(text:str = "", color = "plain"): # Allow for changing the colors of a text. Takes an input of a certain string, and then a color. The default color is plain
    color = color.lower()
    startingEscape = "\033[" # Uses tags that indicate different colors to change the color
    endingEscape = "\033[0m"
    options = {"plain":"37m", # Linking different colors with their corrosponding tags
               "red":"31m", 
               "green":"32m",
               "yellow":"33m",
               "blue":"34m",
               "magenta":"35m", 
               "cyan":"36m"}
    if color in options:    
        colorToken = options[color] # find the tag based on the input 
    else: 
        colorToken = options["plain"] # If there is any misspellings, it will just show it to be plain
    text = startingEscape + colorToken + text + endingEscape # add in the tags
    return text
def renderGuesses(inList, color = "plain"):
    if inList == None or len(inList) == 0:
        return
    for guess in inList:
        print(colors(f" {guess} ",color), end = "")    
    print()

def intializeHangman():
    allWords = {0:["bat","cat","car","sit","bar"],1:["animal","vacuum","practice","loading","virtual"],2:["generations"]}#,"procedural","environment","xylophones"
    namedif = ["easy","medium","hard"]
    allLives = {0:6,1:6,2:4} #The easy ones are short words, with high lives, medium is a bit harder, so you need the lives, hard is just hard
    while True:    
        try:
            difResponse = input("What difficulty? (Awnswer with easy, medium or hard) ").lower()    
            if difResponse in namedif:
                dif = namedif.index(difResponse)
                break
            else:
                raise invalidGuess
        except invalidGuess:
            print("Invalid response, try again")
    info = (allWords[dif],dif)
    live = allLives[info[1]]
    word = random.choice(info[0])
    print()
    return (word, live)
def indexDuplicate(iterable, substring):
    returnIndex = ()
    index = 0
    for char in iterable:
        if substring == char:
            returnIndex += (index,)
        index += 1
    # print(returnIndex)
    return returnIndex

def takeGuesses(gameInfo:tuple):
    placeholder = "_"
    if type(gameInfo[0]) == str and type(gameInfo[1]) == int: #Make sure everything is the correct type
        targetWord = str(gameInfo[0])
        currentLives = gameInfo[1]
    else:    
        raise TypeError
    guessedChar = [placeholder]*len(targetWord)
    usedLetters = set()
    while True:
        try:
            renderGuesses(guessedChar)
            renderGuesses(sorted(usedLetters),"red")
            guess = input("guess: ").lower()
            if guess == "quit":
                break
            if 1 !=  len(guess) or guess not in string.ascii_lowercase:
                raise invalidGuess
            if guess in targetWord:
                results = indexDuplicate(targetWord,guess)
                for index in results:
                    guessedChar[index] = guess
            else:
                currentLives -= 1
                if currentLives <= 0:
                    print("Game over!")
                    break
                print(f"Wrong! You have {currentLives} lives left. ")
            usedLetters.add(guess)
            if indexDuplicate(guessedChar,placeholder) == ():
                renderGuesses(guessedChar)
                print("You Win! ")
                break
        except invalidGuess:
            print("    Invalid Guess, try again")
            
takeGuesses(intializeHangman())
