def toggle(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            grid[i][j] = 1 - grid[i][j]

def off(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            grid[i][j] = 0
def on(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            grid[i][j] = 1

grid = []
#initialize grid
for i in range(0,1000):
    grid.append([0]*1000)
f = open("day6.txt")
#dummyData = ["toggle 4,8 through 8,9", "turn off 3,3 through 4,8", "toggle 0,0 through 9,0"]
#dummyData=["toggle 4,8 through 8,9"]
for input in f:
    if "turn " in input: 
        input = input.split("turn ", 1)[1]
    input = input.split(" ")
    start=input[1].split(",")
    start = [eval(i) for i in start]
    end=input[3].split(",")
    end = [eval(i) for i in end]
    if input[0] == "toggle":
        toggle(start, end)
    if input[0] == "off":
        off(start, end)
    if input[0] == "on":
        on(start, end)
# for x in grid:
#     print(x)

count = 0
for x in grid:
    count = count + x.count(1)

print("Count: " , count)