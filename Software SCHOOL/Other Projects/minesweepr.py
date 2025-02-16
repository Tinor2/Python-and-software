import random
import string
# Debug tools
import os
import sys
def suppress_print():# Suppress print statements
    sys.stdout = open(os.devnull, 'w')
def unsuppress_print():# Unsuppress print statements
    sys.stdout = sys.__stdout__
# Debug tools

numMines = 10
gridSize = 10
def colors(text:str = "", color = "plain"): # Allow for changing the colors of a text. Takes an input of a certain string, and then a color. The default color is plain
    color = color.lower()
    startingEscape = "\033[" # Uses tags that indicate different colors to change the color
    endingEscape = "\033[0m" # Linking different colors with their corrosponding tags
    options = {"plain":"37m", "red":"31m", "green":"32m","yellow":"33m","blue":"34m","magenta":"35m", "cyan":"36m"}
    if color in options:    
        colorToken = options[color] # find the tag based on the input 
    text = startingEscape + colorToken + text + endingEscape # add in the tags
    return text
def renderGrid(grid):
    for row in grid:
        rowStr = ""
        for cell in row:
            if cell == "0":
                rowStr += colors(str("0"), "cyan") + " "
            elif cell == "X":
                rowStr += colors(str("X"), "red") + " "
            else:
                rowStr += colors(str(cell), "magenta") + " "
        print(rowStr)
def indexDuplicate(iterable, substring):
    returnIndex = ()
    for i in range(len(iterable)):
        if substring == iterable[i]:
            returnIndex += (i,)
    return returnIndex
def generateGrid(gridSize,numMines=3):
    mineCoordinates = []
    if gridSize*gridSize < numMines:
        return ["too many mines",""]
    for mine in range(numMines): #generate mine coordinates
        while True:  #make sure there are no duplicates generated. If the coordinate generated already exists, try again
            coords = (random.randint(0,gridSize-1),random.randint(0,gridSize-1)) 
            try:    
                mineCoordinates.index(coords)
            except:
                break
        mineCoordinates.append(coords)
    sortedMines = [mineCoordinates[0],(gridSize+1,gridSize+1)] #adding an out of range tuple, will be removed at the end
    #sort tuple list
    for mine in mineCoordinates[1:]:
        mineCount = 0
        isSorted = False
        for sort in sortedMines:
            if mine[0] > sort[0]:
                mineCount += 1
                continue
            elif mine[0] < sort[0]:
                sortedMines.insert(mineCount,mine)
                mineCount += 1
                isSorted = True
                break
            elif mine[0] == sort[0]:
                colSorted = False
                finalIndex = None
                for column in sortedMines[mineCount:]:
                    if mine[0] != column[0]:
                        finalIndex = sortedMines.index(column)
                        break
                    elif mine[1] < column[1]:
                        sortedMines.insert(sortedMines.index(column),mine)
                        colSorted = True
                        break
                if finalIndex is not None and not colSorted:
                    sortedMines.insert(finalIndex,mine)
                mineCount += 1
                isSorted = True
                break
            mineCount += 1
        if not isSorted:
            sortedMines.insert(len(sortedMines),mine)
    sortedMines = sortedMines[:len(sortedMines)-1]
    print(f"{mineCoordinates}: unsorted\n    {len(mineCoordinates)}: length of unsorted")
    print(f"{sortedMines}: sorted \n    {len(sortedMines)}: length of sorted")
    mineCoordinates = sortedMines
    grid = []
    mineCount = 0
    for rowCount in range(gridSize): #create grid
        row = []
        for colCount in range(gridSize):
            if mineCount != numMines and mineCoordinates[mineCount] == (rowCount,colCount): #if there are still more mines to generate and we are on a mine coordinate
                cell = "X" #X represents mines
                mineCount += 1
            else:
                cell = "/" #/ means no mine
            row.append(cell)
        grid.append(row)
    paddingList = [["."]*(gridSize+2)]
    middlemanGrid = paddingList
    count = 0
    for row in grid:
        count+= 1
        if type(row) == list and count != len(grid): #suppress error    
            middlemanGrid.append(["."]+row+["."])
    grid = middlemanGrid
    paddingList = ["."]*(gridSize+2)
    grid.append(paddingList)
    return grid
def generateDistances(grid):
    paddingList = ["⠀"]*(gridSize+2)
    middleManGrid = [paddingList]
    rowCount = 0
    for row in grid:
        print(row)
        if rowCount == 0: #ignore padding rows
            rowCount += 1
            continue
        cellCount = 0
        middleManRow = []
        for cell in row:
            # print(cellCount,rowCount,(rowCount*gridSize)+cellCount)
            if cellCount == gridSize and rowCount == gridSize:
                print("break")
                break
            elif cell == "." or cell == "X": #if the cell is a mine or a padding cell
                if cell == ".": middleManRow.append("⠀")
                else: middleManRow.append("X")
                cellCount += 1
                continue
            surroundingCells = [grid[rowCount-1][cellCount-1],grid[rowCount-1][cellCount],grid[rowCount-1][cellCount+1], #all cells above
                                grid[rowCount][cellCount-1],grid[rowCount][cellCount+1], #cells to the left and right
                                grid[rowCount+1][cellCount-1],grid[rowCount+1][cellCount],grid[rowCount+1][cellCount+1]] #all cells below
            if indexDuplicate(surroundingCells,"X") != (): #if there is a mine in the surrounding cells    
                middleManRow.append(str(len(indexDuplicate(surroundingCells,"X"))))#Check how many surrounding cells are mines, and add that number to the grid
            else: 
                middleManRow.append("0")
            cellCount += 1
        if cellCount == gridSize and rowCount == gridSize:
            print("break")
            if middleManGrid == None: middleManGrid = []   
            middleManGrid.append(paddingList)
            return middleManGrid
        else:
            middleManGrid.append(middleManRow)    
            rowCount += 1
def addCoordinateBorder(grid):
    numberList = [colors(str(x),"yellow") for x in range(gridSize)]
    grid[0] = [colors("⠀","yellow")]+numberList+["⠀"]
    count = 1
    for row in grid[1:]:
        if row == grid[-1]: break        
        row[0] = colors(string.ascii_uppercase[count-1],"yellow") 
        count += 1
    return grid
suppress_print() 
grid = generateGrid(gridSize,numMines)   
numberedGrid = generateDistances(grid)
unsuppress_print()
awnswerGrid = addCoordinateBorder(numberedGrid)
renderGrid(addCoordinateBorder(numberedGrid))

