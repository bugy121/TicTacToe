# I created a program that never loses at tic tac toe
# I was just messing around with python and thought I would submit it

grid = []
i=1
isOver = False
for x in range(0,3):
    grid.append([])
    for y in range(0,3):
        grid[x].append(i)
        i += 1

isTie = False
i = 0
while isOver == False and i < 5:
    movAval = False
    for x in range(0,3):
        print(grid[x])
    print("make your move")
    move = int(input())

    for x in range(0,3):
        for y in range(0,3):
            if grid[x][y] == move:
                grid[x][y] = "X"
                movAval = True
            
    if movAval == True:
        i += 1
        hasMoved = False

        #check winning diagonals
        if grid[1][1] == "O":
            if grid[0][0] == "O":
                if grid[2][2] != "X":
                    grid[2][2] = "O"
                    hasMoved = True
                    isOver = True
            if grid[2][2] == "O" and hasMoved == False:
                if grid[0][0] != "X":
                    grid[2][2] = "O"
                    hasMoved = True
                    isOver = True
            if grid[0][2] == "O" and hasMoved == False:
                if grid[2][0] != "X":
                    grid[2][0] = "O"
                    hasMoved = True
                    isOver = True
            if grid[2][0] == "O" and hasMoved == False:
                if grid[0][2] != "X":
                    grid[0][2] = "O"
                    hasMoved = True
                    isOver = True

        #check winning horizontal
        for x in range(0,3):
            if grid[x].count("O") == 2 and grid[x].count("X") == 0:
                for y in range(0,3):
                    if grid[x][y] != "O" and hasMoved == False:
                        grid[x][y] = "O"
                        isOver = True
                        hasMoved = True
        
        #check vertical
        for x in range(0,3):
            count = 0
            for y in range(0,3):
                if grid[y][x] == "X":
                    count += 1
                if grid[y][x] == "O":
                    count -= 1
            if count == -2 and hasMoved == False:
                for z in range(0,3):
                    if grid[z][x] != "O":
                        grid[z][x] = "O"
                        isOver = True
                        hasMoved = True
            if count == 2 and hasMoved == False:
                for z in range(0,3):
                    if grid[z][x] != "X":
                        grid[z][x] = "O"
                        hasMoved = True
        
        #check losing horizontal
        for x in range(0,3):
            if grid[x].count("X") == 2 and grid[x].count("O") == 0 and hasMoved == False:
                for y in range(0,3):
                    if grid[x][y] != "X" and hasMoved == False:
                        grid[x][y] = "O"
                        hasMoved = True

        #check losing diagonals
        if grid [1][1] == "X" and hasMoved == False:
            if grid[0][0] == "X":
                if grid[2][2] != "O":
                    grid[2][2] = "O"
                    hasMoved = True
            if grid[2][2] == "X" and hasMoved == False:
                if grid[0][0] != "O":
                    grid[2][2] = "O"
                    hasMoved = True
            if grid[0][2] == "X" and hasMoved == False:
                if grid[2][0] != "O":
                    grid[2][0] = "O"
                    hasMoved = True
            if grid[2][0] == "X" and hasMoved == False:
                if grid[0][2] != "O":
                    grid[0][2] = "O"
                    hasMoved = True
        if grid[0][0] == "X" and hasMoved == False:
            if grid [2][2] == "X":
                if grid[1][0] != "O" and grid[1][0] != "X":
                    grid[1][0] = "O"
                    hasMoved = True

        #Check corners first
        if grid[1][1] == 5 and hasMoved == False:
            grid[1][1] = "O"
            hasMoved = True
        if hasMoved == False:
            for x in range(0,3):
                for y in range(0,3):
                    if grid[x][y] != "X" and grid[x][y] != "O":
                        if int(grid[x][y]) % 2 == 1 and hasMoved == False:
                            grid[x][y] = "O"
                            hasMoved = True
            if hasMoved == False:
                for x in range(0,3):
                    for y in range(0,3):
                        if grid[x][y] != "X" or grid[x][y] != "O":
                            grid[x][y] = "O"
                            hasMoved = True
        if hasMoved == False:
            isTie = True
            isOver = True
    else:
        print ("That is not a valid move")
for x in range(0,3):
    print(grid[x])
if i == 5:
    print("It's a tie!")
else:
    print("You lose :(")