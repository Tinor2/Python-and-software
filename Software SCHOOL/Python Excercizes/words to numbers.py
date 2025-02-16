
numbers ={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0} #zero redundant
multipliers = {"oneUnit":1,"hundred":100,"thousand":1000,"million":1000000}
def stringTwords(numberTxt:str):
    allWords=[]
    try:        
        if numberTxt[0]==" ":
            numberTxt = numberTxt[1:] #removes space as a first charactar
        while True:
            endofWord = numberTxt.index(" ") #If no spaces, exception raised
            allWords.append(numberTxt[:endofWord])
            numberTxt = numberTxt[endofWord+1:]
    except ValueError:#should be no spaces left
        if numberTxt not in [""," "]:
            allWords.append(numberTxt) #adds the last word
        return allWords
    except KeyboardInterrupt:
        print("User Cancelled process")
        return []
wordList = stringTwords(input("Type your number Ryan!!!!!! "))
try:
    wordList.remove("and")
except ValueError:
    pass
for word in wordList:
    if "," in word:
        wordList[wordList.index(word)] = word[:len(word)-1]
wordList.append("oneUnit")
groupedNumbers = []
for index in range(len(wordList)):
    if index % 2 == 0:
        groupedNumbers.append([numbers[wordList[index]],multipliers[wordList[index+1]]]) #find the integer equivalent 
groupedNumbers = groupedNumbers[len(groupedNumbers)::-1]
runningTotal = 0
for unit in groupedNumbers:
    runningTotal += unit[0]*unit[1]
print(runningTotal)
