'''
THE PROGRAM CAN CURRENTLY
-   Process some amount of options (currently is proccessing 4 options)
    -   probably can do any amount, have not tested tho
-   Read through a csv file, containing all of the preferences
-   Evaluate how happy each applicant is with the result
-   Checks whether the "peoplePerOption" list adds up to the correct length
-   Has a loading bar ig
-   Randomly assigns preferences to each applicant, evaluates happiness
    -   Can return a result of (at best) 70%-78% average happiness amongst applicants
THE PROGRAM IS YET TO 
-   Be able to actually use the "peoplePerOption" list: It does not actually do anything in the assignment of preferences.
'''
import random
import CSVfunc
import alive_progress
optionNames = ["A","B","C","D"]
optionLimit = [5,2,2,1]
optionTracker= [0,0,0,0]
preferences = {}
resultNames = {}    # Dictionary of {person# : assignedOptionName,...}
results = {}        # Dictionary of {person# : assignedOptionIndex,...}
resultTemp = {}     # Dictionary of {person# : how prefered is assigned option,...}

preferences = CSVfunc.csvTdict("samplePreferences.csv", 4,True)

iterationCount = 0
resolution = 10000
maxAverageTemp = 0
choiceList = []
def flushPrint(string):
    print(string, end='', flush=True)
def printDictionary(inDict):
    for key, value in inDict.items():
        flushPrint(" "+str(key)+": "+str(value)+" |")
    flushPrint("|")
    print()
def assigningResults(inDict):
    '''
    IN: dictionary
        KEY: number respective to the applicant 
        VALUE: list where the index indicates which option, and the number indicates the order of preference
    OUT: dictionary
        KEY: number respective to the applicant
        VALUE: Random choice of the options
    '''
    for person in inDict.keys():
        while True:
            choice = random.choice(optionNames)
            choiceIdentifier = optionNames.index(choice)
            if optionTracker[choiceIdentifier] + 1 <= optionLimit[choiceIdentifier]:
                print('fdsfds')
                optionTracker[choiceIdentifier] += 1
                break  
        choiceList.append(choice)
        resultNames.update({person:choice})
    return resultNames
with alive_progress.alive_bar(resolution) as bar: #Needed for progress bar, no affect to the logic
    while not (iterationCount>=resolution):
        optionTracker = [0,0,0,0]
        if iterationCount == 1: #first iteration
            if len(preferences) != sum(optionLimit):
                print("INVALID CONSTRAINTS") # make sure theres a valid amount of people
                break
        resultNames = assigningResults(preferences)
        for key,val  in resultNames.items():
            results.update({key:optionNames.index(val)+1}) #Converts the option names into numbers, (first option => 1, etc)
            
        for person in preferences.keys():
            outcome = results[person]
            preferenceList = preferences[person]
            temp = len(preferenceList)-(int(preferenceList.index(outcome)+1))
            temp /= len(preferenceList)
            resultTemp.update({person:temp})
        # print("____________________________")
        # printDictionary(resultTemp)
        averageTemp = 0
        i = 0
        for temperature in resultTemp.values():
            i += 1
            averageTemp += temperature
        averageTemp /= i
        if averageTemp > maxAverageTemp:    
            maxAverageTemp = averageTemp
            bestResults = results
            print(maxAverageTemp)
        iterationCount += 1
        bar()
if iterationCount == resolution:
    print(maxAverageTemp)
    print(results)
    print(results.values())

