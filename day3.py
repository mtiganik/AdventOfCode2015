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

grid = [[1]]

f = open("day3.txt")
input = f.readline()
ver,hor=0,0
for x in input:
    if '^' in x:
        if ver == 0:
            newRowUp(hor)
        else:
            ver = ver -1
            grid[ver][hor] = grid[ver][hor] +1
    if '>' in x:
        if hor == len(grid[0]) -1:
            newRowRight(ver)
            hor = hor +1
        else:
            hor = hor +1
            grid[ver][hor] = grid[ver][hor] +1
    if 'v' in x:
        if ver == len(grid) -1:
            newRowDown(hor)
            ver = len(grid) -1
        else:
            ver = ver +1
            grid[ver][hor] = grid[ver][hor] +1
    if '<' in x:
        if hor == 0:
            newRowLeft(ver)
        else:
            hor = hor -1
            grid[ver][hor] = grid[ver][hor] +1
count = 0
# for x in grid:
#     print(x)

for row in grid:
    for x in row:
        if x > 0: 
            count = count +1

print(count)
