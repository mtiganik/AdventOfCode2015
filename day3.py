def newRowUp(j,grid):
    newRow = [0]*len(grid[0])
    grid.insert(0,newRow)
    grid[0][j] = 1

def newRowRight(i,grid):
    for x in grid:
        x.append(0)
    grid[i][len(grid[0])-1]=1
def newRowLeft(i,grid):
    for x in grid:
        x.insert(0,0)
    grid[i][0] = 1
def newRowDown(j,grid):
    newRow = [0]*len(grid[0])
    grid.append(newRow)
    grid[len(grid)-1][j] = 1

class GridWorker:
    def __init__(self, hor,ver):
        self.hor = hor
        self.ver = ver


    def populateGrid(self, x, grid):
        if '^' in x:
            if self.ver == 0:
                newRowUp(self.hor,grid)
            else:
                self.ver = self.ver -1
                grid[self.ver][self.hor] = grid[self.ver][self.hor] +1
        if '>' in x:
            if self.hor == len(grid[0]) -1:
                newRowRight(self.ver,grid)
                self.hor = self.hor +1
            else:
                self.hor = self.hor +1
                grid[self.ver][self.hor] = grid[self.ver][self.hor] +1
        if 'v' in x:
            if self.ver == len(grid) -1:
                newRowDown(self.hor,grid)
                self.ver = len(grid) -1
            else:
                self.ver = self.ver +1
                grid[self.ver][self.hor] = grid[self.ver][self.hor] +1
        if '<' in x:
            if self.hor == 0:
                newRowLeft(self.ver,grid)
            else:
                self.hor = self.hor -1
                grid[self.ver][self.hor] = grid[self.ver][self.hor] +1

def getStartIndex(grid):
    col = 0
    for x in grid:
        col = col +1
        santaStart = [col,0]
        if max(x) > 100:
            maxVal=max(x)
            row = x.index(maxVal)
            santaStart = [col-1, row]
            break
    return santaStart

def findValsinArea(colS, colE, rowS, rowE, grid):
    counter = 0
    for i in range(colS, colE):
        for j in range(rowS, rowE):
            if grid[i][j] > 0: counter = counter +1
    return counter

santaGrid, roboGrid = [[1000]],[[1000]]
santaClass = GridWorker(0,0)
roboClass = GridWorker(0,0)
f = open("day3.txt")
input = f.readline()
#input = "<<^>v^^>>^>^v>>"
counter = 0
for x in input:
    counter = counter +1
    if counter % 2 == 1 :
        santaClass.populateGrid(x,santaGrid)
    else :
        roboClass.populateGrid(x,roboGrid)

# for x in santaGrid:
#     print(x)

# print("roboGrid")
# for x in roboGrid:
#     print(x)

santaStart = getStartIndex(santaGrid)
roboStart = getStartIndex(roboGrid)


print("Santa start:")
print(santaStart)
print("Robo start:")
print(roboStart)




santatxt = "Santas grid is 0-{} wide and 0-{} tall"
robotxt = "Robo grid is 0-{} wide and 0-{} tall"
print(santatxt.format(len(santaGrid[0])-1, len(santaGrid)-1))
print(robotxt.format(len(roboGrid[0])-1, len(roboGrid)-1))

count = 0

print(findValsinArea(0,22,0,52, santaGrid))
print(findValsinArea(22,115,0,22, santaGrid))
print(findValsinArea(84,115,22,53, santaGrid))
print(findValsinArea(0,62,30,68, roboGrid))
count = count + findValsinArea(0,22,0,52, santaGrid) + findValsinArea(22,115,0,22, santaGrid) + findValsinArea(84,115,22,53, santaGrid) + findValsinArea(0,62,30,68, roboGrid)


print("values in non matching places:")
print(count)

santaGrid = santaGrid[22:85]
for x in santaGrid:
    for i in range(22):
        x.pop(0)
print(len(santaGrid))
print(len(roboGrid))
print(len(santaGrid[0]))

lapCount=0
for i in range(63):
    for j in range(31):
        if santaGrid[i][j] > 0 or roboGrid[i][j] > 0: lapCount = lapCount +1 

print("lapCount")
print(lapCount)

print("total")
count = count + lapCount
print(count)
# for row in santaGrid:
#     for x in row:
#         if x > 0:
#             count = count +1
# print(robotxt.format(len(roboGrid[0]), len(roboGrid)))

# for row in roboGrid:
#     for x in row:
#         if x > 0:
#             count = count +1

# print(count)
