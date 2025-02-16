#Stream 2 Week 2
# Note, this was mostly review
def isPalidrome(stringIN:str):
    if stringIN == stringIN[::-1]:
        return "This is a palindrome"
    else:
        return "This isnt a plaindrome"
# print(isPalidrome("abcd")) # ==> "This isnt a plaindrome"
# print(isPalidrome("racecar")) # ==> "This is a palindrome"

def listManipulation(listIN:list):
    # return all even numbers
    evenList = [num for num in listIN if num % 2 is 0]
    return evenList
# print(listManipulation([1,2,3,4,5,6])) # ==> [2, 4, 6]

def longestWord(listIN: list):
    return max(listIN)
# print(longestWord(["a", "aa", "aaa", "aaaa"])) # ==> "aaaa" 

import string
def ceaserShift(uncrypted: str, shift: int):
    allLetters = string.ascii_lowercase
    encrypted = ""
    for letter in uncrypted:
        if letter.lower() in allLetters:
            encrypted += allLetters[(allLetters.index(letter) + shift) % 26] # Find the index of og letter, then shift it by given amount, if it spills over 26, loop it back to the start
        else:
            encrypted += letter # If letter isnt in the alphabet, just add it to the string (symbols, numbers, etc)
    return encrypted
# print(ceaserShift("abc", 1)) # ==> "bcd"

'''
Reflection question:
How does modular project organisation help during development?
    It helps to keep code organised. For example, if you have a lenghthy function that is constantly reused in the project, but feels like
    it takes up a lot of space, just move it to a different file in the same folder, and then import it at the start of the project. You can use this to make 
    a library of pre-made functions that you can use in any project.
What challenges did you face in advanced string or list operations?
    This is familiar to me, so not really
How would you apply these concepts to the Hangman game?
    Finding the longest word would help to decide the dificulty of a certain word
    List comprehension could make code a lot more consise
'''