def newRowUp(j, who):
    newRow = [[0,0]]*len(grid[0])
    grid.insert(0,newRow)
    grid[0][j] = who

def newRowRight(i,who):
    for x in grid:
        x.append([0,0])
    grid[i][len(grid[0])-1]=who
def newRowLeft(i,who):
    for x in grid:
        x.insert(0,[0,0])
    grid[i][0] = who
def newRowDown(j,who):
    newRow = [[0,0]]*len(grid[0])
    grid.append(newRow)
    grid[len(grid)-1][j] = who

grid = [[[10,10]]]

f = open("day3.txt")

input = f.readline()
input = ">^^v^<>v<<<v<v^>>v^^^<v<>^^><^<<^vv>"
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
    print(tick)
    for y in grid:
        print(y)
    if sTime == 1:
        if '^' in x:
            if santaVer == 0:
                newRowUp(santaHor,[1,0])
                roboVer = roboVer + 1
            else:
                santaVer = santaVer -1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
        if '>' in x:
            if santaHor == len(grid[0]) -1:
                newRowRight(santaVer,[1,0])
                santaHor = santaHor +1
            else:
                santaHor = santaHor +1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
        if 'v' in x:
            if santaVer == len(grid) -1:
                newRowDown(santaHor,[1,0])
                santaVer = len(grid) -1
            else:
                santaVer = santaVer +1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
        if '<' in x:
            if santaHor == 0:
                newRowLeft(santaVer,[1,0])
                roboHor = roboHor + 1
            else:
                santaHor = santaHor -1
                grid[santaVer][santaHor][0] = grid[santaVer][santaHor][0] +1
    else:
        if '^' in x:
            if roboVer == 0:
                newRowUp(roboHor,[0,1])
                santaVer = santaVer + 1
            else:
                roboVer = roboVer -1
                grid[roboVer][roboHor][1] = grid[roboVer][roboHor][1] +1
        if '>' in x:
            if roboHor == len(grid[0]) -1:
                newRowRight(roboVer,[0,1])
                roboHor = roboHor +1
            else:
                roboHor = roboHor +1
                grid[roboVer][roboHor][1] = grid[roboVer][roboHor][1] +1
        if 'v' in x:
            if roboVer == len(grid) -1:
                newRowDown(roboHor,[0,1])
                roboVer = len(grid) -1
            else:
                roboVer = roboVer +1
                grid[roboVer][roboHor][1] = grid[roboVer][roboHor][1] +1
        if '<' in x:
            if roboHor == 0:
                newRowLeft(roboVer,[0,1])
                santaHor = santaHor + 1
            else:
                roboHor = roboHor -1
                grid[roboVer][roboHor][1] = grid[roboVer][roboHor][1] +1

count = 0

for row in grid:
    for x in row:
        if x[0] > 0 or x[1] > 0: count = count +1

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


