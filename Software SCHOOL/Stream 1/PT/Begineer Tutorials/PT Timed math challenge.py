import random
import time
operations =['+','-','*','/']
Total_Problems = 10
def generateProblem(minN, maxN):
    operation = random.choice(operations)
    num1 = random.randint(minN, maxN)
    while True:    # to avoid division by zero
        num2 = random.randint(minN, maxN)
        if operation == '/' and num2 == 0:
            continue
        if operation == '/' and num1 % num2 != 0: # make sure the division is doable
            continue
        break
    problem = f"{num1} {operation} {num2}"
    awnser = int(eval(problem))
    return problem, awnser
incorrectGuesses = 0

input("Enter to start the game: ")
print("_"*100)
start = time.time()
for problemNum in range(Total_Problems):
    problem, correctResponse = generateProblem(1, 10)
    while True:    
        print("Problem #"+ str(problemNum+1), end=": ")    
        guess = input(f"{problem} = ")
        if guess == str(correctResponse):
            print("Correct!")
            break
        elif guess == "q":
            print("You have quit the game.")
            break
        else:
            incorrectGuesses += 1
            print("Incorrect. Re-attempt.")
    if guess == "q":
        break
if guess != "q":
    print("_"*100)
    end = time.time()
    # end timer
    print("FINISHED. You had an accuracy rate of: ",end="")
    print(100-(incorrectGuesses/Total_Problems)*100, "%")
    print(f"Time taken: {end-start:0.2f} seconds")