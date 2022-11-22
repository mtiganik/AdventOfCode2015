def newRowUp(j):
    newRow = [0]*len(grid[0])
    grid.insert(0,newRow)
    grid[0][j] = 1

def newRowRight(i):
    for x in grid:
        x.append(0)
    grid[i][len(grid[0])-1]=1
def newRowLeft(i):
    for x in grid:
        x.insert(0,0)
    grid[i][0] = 1
def newRowDown(j):
    newRow = [0]*len(grid[0])
    grid.append(newRow)
    grid[len(grid)-1][j] = 1

grid = [[[10,10]]]

f = open("day3.txt")

#input = f.readline()
input ="^v^v^v^v^v"
santaVer,santaHor,sTime,roboVer,roboHor=0,0,0,0,0
tick = 0
for x in input:
    tick = tick +1
    if tick % 2 == 1: sTime = 1
    else: sTime = 0
    if sTime == 1:
        if '^' in x:
            if santaVer == 0:
                newRowUp(santaHor)
                roboVer = roboVer + 1
            else:
                santaVer = santaVer -1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
        if '>' in x:
            if santaHor == len(grid[0]) -1:
                newRowRight(santaVer)
                santaHor = santaHor +1
            else:
                santaHor = santaHor +1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
        if 'v' in x:
            if santaVer == len(grid) -1:
                newRowDown(santaHor)
                santaVer = len(grid) -1
            else:
                santaVer = santaVer +1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
        if '<' in x:
            if santaHor == 0:
                newRowLeft(santaVer)
                roboHor = roboHor + 1
            else:
                santaHor = santaHor -1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
    else:
        if '^' in x:
            if roboVer == 0:
                newRowUp(roboHor)
                santaVer = santaVer + 1
            else:
                roboVer = roboVer -1
                grid[roboVer][roboHor][1] = grid[roboVer][roboHor][1] +1
        if '>' in x:
            if roboHor == len(grid[0]) -1:
                newRowRight(roboVer)
                roboHor = roboHor +1
            else:
                roboHor = roboHor +1
                grid[roboVer][roboHor][1] = grid[roboVer][roboHor][0] +1
        if 'v' in x:
            if roboVer == len(grid) -1:
                newRowDown(roboHor)
                roboVer = len(grid) -1
            else:
                roboVer = roboVer +1
                grid[roboVer][roboHor][0] = grid[roboVer][roboHor][0] +1
        if '<' in x:
            if roboHor == 0:
                newRowLeft(roboVer)
                santaHor = santaHor + 1
            else:
                roboHor = roboHor -1
                grid[roboVer][roboHor][0] = grid[roboVer][roboHor][0] +1

count = 0
# for x in grid:
#     print(x)

for row in grid:
    for x in row:
        print(x[0], x[1], end = " ")
    print("")
print(count)
