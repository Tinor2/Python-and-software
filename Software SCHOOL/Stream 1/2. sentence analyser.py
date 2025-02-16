'''
# New thing learned: 1 line loops
[char for char in iterable if char is "x"]  
    #note that the first word is what the variable is equal to at every iteration.
            ==>
def func(iterable):    
    for char in iterable
        if char is "x":
            newList.append(char)
    return newList
'''

inSentence = input("Sentence to analyse: ")
if inSentence[0] == " ":   
    inSentence = inSentence[1:] #Counting words by spaces, if there is a space at start or end, doesnt count as new word
if inSentence[len(inSentence)-1] == " ": 
    inSentence = inSentence[:len(inSentence)-2]
vowels = "aeiou"
countWords = len([char.lower() for char in inSentence if char == " "]) 
countVowels = len([char.lower() for char in inSentence if char in vowels]) + 1 #lowercase each letter, in order to also process uppercase vowels
listedString = [char for char in inSentence]
listedString.insert(0, " ")
for index in range(len(listedString)):
    if listedString[index] == " ":
        listedString[index+1] = listedString[index+1].upper()
captilized = "".join(listedString)
print(f"Results: \n  {countVowels} vowels\n  {countWords} words\n Title Case: {captilized}")




