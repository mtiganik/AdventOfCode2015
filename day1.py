def day1P1(input):
    up = input.count('(')
    down = input.count(')')
    result = up - down
    print(result)

def day1P2(input):
    floor = 0
    index = 0
    for x in input:
        index = index +1
        if '(' in x:
            floor = floor + 1
        elif ')' in x:
            floor = floor - 1
        if floor < 0:
            txt = "Floor reached on {}"
            print(txt.format(index))
            break

f = open("test.txt")
input = f.readline()
day1P1(input)
day1P2(input)
