import math
#████████████
#████████████
# INCOMPLETE
#████████████
#████████████
interval = [0,math.pi]
step = 0.00001
def function(x):
    y = math.sin(x)
    return y
magnitude = abs(interval[1]-interval[0])
i= 0
n=0
allValues = []
while i<magnitude:
    allValues.append(function(i))
    i += step
    n +=1
    print(n)
print("DONE")
runningTotal = 0
for value in allValues:
    runningTotal += value
print(runningTotal/n)

    
    
    

