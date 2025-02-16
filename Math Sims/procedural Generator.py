# import CSVfunc

xLength = 32 #Length of grid
yLength = 40 #Height of grid
seed = [0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0]
print(len(seed))
emptyGrid = [[0]*xLength]*(yLength)
grid = []
grid.insert(0,seed)
def colors(text:str = "", color = "plain"): # Allow for changing the colors of a text. Takes an input of a certain string, and then a color. The default color is plain
    color = color.lower()
    startingEscape = "\033[" # Uses tags that indicate different colors to change the color
    endingEscape = "\033[0m"
    options = {"plain":"37m", # Linking different colors with their corrosponding tags
               "red":"31m", 
               "green":"32m",
               "yellow":"33m",
               "blue":"34m",
               "magenta":"35m", 
               "cyan":"36m"}
    if color in options:    
        colorToken = options[color] # find the tag based on the input 
    else: 
        colorToken = options["plain"] # If there is any misspellings, it will just show it to be plain
    text = startingEscape + colorToken + text + endingEscape # add in the tags
    return text
def renderGrid(grid):
    for row in grid:
        rowStr = ""
        for cell in row:
            if cell == 1:
                rowStr += colors(str("1"), "green") + " "
            elif cell == 0:
                rowStr += colors(str("0"), "red") + " "
            else:
                rowStr += colors(str(cell), "cyan")
        print(rowStr)
i = 0
yPos = 0 #row count, or the y position, or the height.
for row in emptyGrid:
    if yPos == 0: #seed does not get overwritten
        yPos += 1 
        continue
    xPos = 0 #column count, or x position, or length.
    print(f"row: {yPos}")
    finalRow = []
    for cell in row:
        if xPos not in [0,xLength-1] and yPos not in [0,yLength-1]: #Filtering out edges and corners
            # Find the diagonals and adjacent cell values of a certain cell
            diagonals = [grid[yPos-1][xPos-1],
                         grid[yPos-1][xPos+1]]
            adjacents = [finalRow[xPos-1],
                         grid[yPos-1][xPos]] # X AND Y ARE SWITCHED AROUND ACTUALS ANNOYING 
        else:
            diagonals = [2,2] #no value
            adjacents = [2,2]
            finalRow.append(0)
            print(f"    xcoord: {xPos}, ycoord: {yPos}, cell Value {0}")
            print("        edgeCase")
            xPos += 1
            continue
        if adjacents == [1,1] and diagonals[0] == 1:
            finalRow.append(0)
            print(f"    xcoord: {xPos}, ycoord: {yPos}, cell Value {0}")
            print("        cancel box")

        elif adjacents == [1,1] and diagonals == [0,0] or adjacents == [0,0] and diagonals == [1,1]:
            finalRow.append(0)
            print(f"    xcoord: {xPos}, ycoord: {yPos}, cell Value {0}")
            print("        cancel junction")
        elif adjacents == [0,1] and diagonals == [0,0]:
            print(f"{adjacents}, {diagonals}")
            finalRow.append((i%3)%2)
            i+=1
            print(f"    xcoord: {xPos}, ycoord: {yPos}, cell Value {1}")
            print("        close room")
        else:
            print(f"{adjacents}, {diagonals}")
            finalRow.append(1)
            print(f"    xcoord: {xPos}, ycoord: {yPos}, cell Value {1}")
            print("        base fill")
        xPos += 1
        # finalGrid.append((xPos,yPos))
    grid.append(finalRow)
    renderGrid(grid)
    # input()
    finalRow = []
    yPos += 1

print("________________________")
renderGrid(grid)
# CSVfunc.listTcsv(grid,"render.csv")
