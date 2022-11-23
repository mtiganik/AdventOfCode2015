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

input = ">^^v^<>v<<<v<v^>>v^^^<v<>^^><^<<^vv>"
input = "^>v<"
input = f.readline()
tick = 0
sString, rString = "", ""
for x in input:
    tick = tick +1
    if tick%2 == 1: sString = sString + x
    else : rString = rString +x

print(sString)
print("")
print(rString)
santaVer,santaHor,sTime,roboVer,roboHor=0,0,0,0,0
tick = 0
for x in input:
    tick = tick +1
    if tick % 2 == 1: sTime = 1
    else: sTime = 0
    # print(tick)
    # for y in grid:
    #     print(y)
    if sTime == 1:
        if '^' in x:
            if santaVer == 0:
                newRowUp(santaHor)
                roboVer = roboVer + 1
            else:
                santaVer = santaVer -1
                grid[santaVer][santaHor] = 1
        if '>' in x:
            if santaHor == len(grid[0]) -1:
                newRowRight(santaVer)
                santaHor = santaHor +1
            else:
                santaHor = santaHor +1
                grid[santaVer][santaHor] = 1
        if 'v' in x:
            if santaVer == len(grid) -1:
                newRowDown(santaHor)
                santaVer = len(grid) -1
            else:
                santaVer = santaVer +1
                grid[santaVer][santaHor] = 1
        if '<' in x:
            if santaHor == 0:
                newRowLeft(santaVer)
                roboHor = roboHor + 1
            else:
                santaHor = santaHor -1
                grid[santaVer][santaHor] = 1
    else:
        if '^' in x:
            if roboVer == 0:
                newRowUp(roboHor)
                santaVer = santaVer + 1
            else:
                roboVer = roboVer -1
                grid[roboVer][roboHor] = -1
        if '>' in x:
            if roboHor == len(grid[0]) -1:
                newRowRight(roboVer)
                roboHor = roboHor +1
            else:
                roboHor = roboHor +1
                grid[roboVer][roboHor] = -1
        if 'v' in x:
            if roboVer == len(grid) -1:
                newRowDown(roboHor)
                roboVer = len(grid) -1
            else:
                roboVer = roboVer +1
                grid[roboVer][roboHor] = -1
        if '<' in x:
            if roboHor == 0:
                newRowLeft(roboVer)
                santaHor = santaHor + 1
            else:
                roboHor = roboHor -1
                grid[roboVer][roboHor] = -1

count = 0

for row in grid:
    for x in row:
        if x == 1 or x == -1: count = count +1

for x in grid:
    print(x)

print(count)

# leng = len(grid[0])
# gridlen = len(grid[1]) -1
# for i in range(gridlen):
#     if len(grid[i]) != leng:
#         text = "item {} length was {}"
#         print(text.format(i, len(grid[i])))

# print("len of first: ",leng)


# for x in grid:
#     print(x)

# for row in grid:
#     for x in row:
#         print(x[0], x[1], end = " ")
#     print("")


