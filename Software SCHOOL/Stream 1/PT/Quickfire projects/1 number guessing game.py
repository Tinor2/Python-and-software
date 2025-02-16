import random
roll = lambda max :  random.choice(range(1,max))
target = roll(max)
numGuesses = 0
def difficultyChooser(difficulty:str):
    differentOptions =["e",'m',"h","cheats"]
    if difficulty in differentOptions:
        if difficulty == differentOptions[0]:
            return 20
        elif difficulty == differentOptions[1]:
            return 10
        elif difficulty == differentOptions[2]:
            return 5
        else:
            return 10000
    else:
        return -1 # Error
while True:
    totalGuessesAllowed = difficultyChooser(input("Choose a difficulty! "))
    if totalGuessesAllowed < 0:
        print("Invalid difficult, try agin")
    else:
        break
    


while True:
    try:
        guess = int(input("What is your guess? "))
        numGuesses += 1
        if numGuesses >= totalGuessesAllowed:
            break
        if guess > target:
            print("Too High! ")
        elif guess < target:
            print("Too Low! ")
        else: 
            break
    except:
        print("Try again, invalid input")
if numGuesses >= totalGuessesAllowed:
    print(f"YOU LOST! With a grand total of \n   {numGuesses} guesses!")    
else:    
    print(f"YOU WON! with a grand total of \n   {numGuesses} guesses!")