# SAMPLE FILE: DO ANYTHING, leave any notes for later

def editEntry(path):
    with open(path, "r") as file:
        entries = file.readlines()
        # Remove \n from each entry if it ends with it
        entries = [entry.rstrip('\n') for entry in entries]
    return entries

allEntries = editEntry("Software SCHOOL/Stream 1/PT/Quickfire projects/To do lists Folder/Untitled To do list.txt")
for entry in allEntries:
    print(entry)


'''
#!! Creating duplicate files, by adding a number to the end of the file name if required
import os 
path = None
title = None
newFolderName = None
if path == None:
    path = os.path.dirname(__file__)
if title == None:
    title = "Untitled To do list"
if newFolderName == None:
    newFolderName = "To do lists Folder"
path += f"/{newFolderName}"
try:
    os.makedirs(path)
    print(f"Folder created at: {path}")
except FileExistsError:
    # print(f"Folder already exists at: {path}")
    if False:
        print("Error 1 - Folder already exists")
    else:
        pass
except Exception as e: 
    print("Error 2 - Misc error")
items = os.listdir(path)
files = [item for item in items if os.path.isfile(os.path.join(path, item))]
name = f"{title}.txt"
i = 1
while True:    
    if name in files:
        print("File already exists")
        name = f"{title} {i}.txt" # remove the initial title, insert new title with a number
        i += 1
    else:
        break
path = path + f"/{name}"
#!!
def indexDuplicate(iterable, substring):
    returnIndex = ()
    index = 0
    for char in iterable:
        if substring == char:
            returnIndex += (index,)
        index += 1
    return returnIndex
print(indexDuplicate(inSentence,"a"))
#!!
listOfTuples= [(0, 0), (5, 0), (7, 8), (8, 2), (2, 8), (2, 2), (2, 5), (5, 2), (0, 3), (4, 6), (0, 9), (9, 3), (9, 2), (8, 4), (7, 5), (7, 1), (3, 8), (9, 4), (5, 5), (4, 3), (7, 9), (5, 4), (6, 6), (3, 5), (7, 6), (3, 4), (6, 1), (8, 6), (6, 0), (5, 6), (3, 7), (8, 0), (3, 9), (6, 9), (3, 0), (0, 5), (1, 3), (7, 0), (4, 9), (4, 0), (1, 5), (2, 9), (9, 0), (5, 8), (9, 1), (1, 6), (1, 1), (4, 1), (3, 3), (0, 4)]
for Tuple in listOfTuples:
    if Tuple[0] == 9:
        print(Tuple) 
print()
otherList = [(0, 0), (0, 3), (0, 4), (0, 5), (0, 9), (1, 1), (1, 3), (1, 5), (1, 6), (2, 2), (2, 5), (2, 8), (2, 9), (3, 0), (3, 3), (3, 4), (3, 5), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 3), (4, 6), (4, 9), (5, 0), (5, 2), (5, 4), (5, 5), (5, 6), (5, 8), (6, 0), (6, 1), (6, 6), (6, 9), (7, 0), (7, 1), (7, 5), (7, 6), (7, 8), (7, 9), (8, 0), (8, 2), (8, 4), (8, 6), (9, 0), (9, 1), (9, 2), (9, 3)]
for Tuple in otherList:
    if Tuple[0] == 9:
        print(Tuple)
#!! Valid barckets (i.e. "([()])" is valid but "{]}" or "{([)]}" isnt)
s = "()"
openB = ["(","{","["]
closeB = [")","}","]"]
singleB = []
for bracket in s:
    if bracket in openB:
        singleB.append(bracket)
    if bracket in closeB:
        bracketType = closeB.index(bracket) #int
        if singleB[len(singleB)-1]== openB[bracketType] and len(singleB) != 0:
            singleB = singleB[:len(singleB)-1]
        else:
            print(False)
print(singleB)
print(True)
#!! Supposed to be a roman numeral calculator, but its a stupid method, not how roman numerals work
conversion = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} 
eachDigit = []
s = "MCMXCIV"
for digit in s: eachDigit.append(digit) #Turn string into list
for index in range(len(eachDigit)):
    eachDigit[index] = conversion[eachDigit[index]] #string into int
    
previousNum = eachDigit[0]
i=0
print(eachDigit)
for currentNum in eachDigit:
    print(f"{currentNum} vs {previousNum}")
    if currentNum > previousNum and i != len(eachDigit)-1:
        eachDigit.pop(i)
        eachDigit[i] -= previousNum
        print(sum(eachDigit))
    previousNum = currentNum
    i+=1
runningTotal = 0

for number in eachDigit:
    runningTotal += number
print(runningTotal)
#!!
for person in inDict.keys():
        choice = random.choice(optionNames)
        choiceList.append(choice)
        resultNames.update({person:choice})
    person = None
    return resultNames
#!!
def assigningResults(inDict):
    
    # IN: dictionary
    #     KEY: number respective to the applicant 
    #     VALUE: list where the index indicates which option, and the number indicates the order of preference
    # OUT: dictionary
    #     KEY: number respective to the applicant
    #     VALUE: Random choice of the options
    
    for person in inDict.keys():
        while True:
            choice = random.choice(optionNames)
            choiceIdentifier = optionNames.index(choice)
            if optionTracker[choiceIdentifier] + 1 <= optionLimit[choiceIdentifier]:
                optionTracker[choiceIdentifier] += 1
                break  
        choiceList.append(choice)
        resultNames.update({person:choice})

    person = None
    return resultNames
#!!
for person in inDict.keys():
        optionTracker = [0,0,0,0] #reset 
        choice = random.choice(optionNames)
        choiceList.append(choice)
        resultNames = {}    # Dictionary of {person# : assignedOptionName,...}
        final = {}          # Dictionary of {person# : assignedOptionIndex,...}
        resultNames.update({person:choice})
        for key,val  in resultNames.items():
            final.update({key:optionNames.index(val)+1}) #Converts the option names into numbers, (first option => 1, etc)
            optionTracker[optionNames.index(val)+1] += 1  
    person = None #Safe check if person variable is used later
    return results
#!! question for gemini 
I need a function that can take a list of preferences, that look like the following

{1 ': [4, 1, 2, 3], ' 2 ': [3, 4, 2, 1], ' 3 ': [2, 4, 1, 3], ' 4 ': [2, 4, 1, 3], ' 5 ': [2, 3, 4, 1], ' 6 ': [3, 2, 1, 4], ' 7 ': [1, 3, 2, 4], ' 8 ': [2, 4, 3, 1], ' 9 ': [3, 4, 2, 1], '10 ': [2, 4, 3, 1]}, where the key represents a person, 
and the lists represent a list of preferences. Within these lists, the index represents the option that each ranking is assigned to (i.e. [3, 4, 2, 1] shows option 4 to be ranked highest, option 3 to be second,
option 1 to be third, and option 2 to be last). 
I would like an algorithm that can take this dictionary, and return 



#!! Reverse a string, also loop through each letter in reverse
text = "abcdefg"
print(text[::-1]) # Starts: unspecified, so default to len(text) AKA the start, Ends: Unspecified, just until there is nothign left to loop through, Step: -1, moves backwards through the object
for index in range(len(text)):
    print(text[::-1][index])

#!! ??
import CSVfunc
import random
dictionary = {}
prefList = [1,2,3,4] 
random.shuffle(prefList)
def flushPrint(string):
    print(string, end='', flush=True)
def printDictionary(inDict):
    for key, value in inDict.items():
       print(" "+str(key)+": "+str(value)+" |")
    flushPrint("|")
    print()


# for i in range(30):
#     i+= 1
#     random.shuffle(prefList)
#     print(prefList)
#     dictionary.update({i:prefList})
#     prefList = [1,2,3,4]
# printDictionary(dictionary)

# CSVfunc.dictTcsv(dictionary,"samplePreferences")

dictionary = CSVfunc.csvTdict("samplePreferences.csv",5)
print(dictionary)
'''