
allInt = ['1','2','3','4','5','6','7','8','9','0']   
allOp = ['a','b','c','d']                
error = False
class exception(Exception): pass #If any error occurs throughout the code, we call an EXCEPTION.
# Whenever an exception is called, it ignores the rest of the try loop, and skips to except loop (seen later)
def Error(errorType):  #This is a method to make it easier to call errors later
    if errorType == 1:
        raise exception("Syntax error")
    elif errorType == 2:
        raise exception("Math error")
    elif errorType == 3:
        raise exception("User called error")
def checkForErrors(subject, Lst): #This checks if input is one of the inputs in the lists at the top
    c = 0
    if subject == "*": # If the input is an astrix, then just reset the code
        Error(3)
    elif subject is None:
        Error(1)       #This means somewhere in the code there is an error in setting up the function
    else:
        for item in Lst: # Loop through the list and make sure its in the list
            if subject == item: 
                item = subject
                break
            else:
                c += 1
        if len(Lst) <= c:
            Error(1)
def morseCodeTranslator(char,inputType): #This checks if the morse code inputed is valid
  if inputType == "int": 
    if char == ".----":
      return "1"
    elif char == "..---":
      return "2"
    elif char == "...--":
      return "3"
    elif char == "....-":
      return "4"
    elif char == ".....":
      return "5"
    elif char == "-....":
      return "6"
    elif char == "--...":
      return "7"
    elif char == "---..":
      return "8"
    elif char == "----.":
      return "9"
    elif char == "-----":
      return "0"
    else:
      Error(1) # input isn't valid
  elif inputType == "op":
    if char == ".-":
      return "a"
    elif char == "-...":
      return "b"
    elif char == "-.-.":
      return "c"
    elif char == "-..":
      return "d"
    else:
      Error(1) #input isn't valid
  else:
    Error(1) # input isn't valid
   
    
while True:
    try:
        int1 = morseCodeTranslator(".","int") #covert morse code into a number or operator
        checkForErrors(int1, allInt) # double check if there is any error
    except exception: #This means that an error was raised during the Try loop
        print("fdsf") 
        #Reset the try loop



