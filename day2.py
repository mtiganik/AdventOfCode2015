def Day2P2(input):
    total = 0
    for x in f:
        len, width, height = x.split("x")
        box = [int(len), int(width), int(height)]
        box.sort()
        ribbon = 2*box[0] + 2*box[1]
        bow = box[0]*box[1]*box[2]
        area = bow + ribbon
        print(area)
        total = total + area
    print(total)

def Day2P1(input):
    total= 0
    for x in f:
        len, width, height = x.split("x")
        len, width, height = int(len), int(width), int(height)
        box = [2*len*width, 2*width*height, 2* height*len]
        box.sort()
        area = box[0] + box[1]+box[2] + box[0]/2
        print(area)
        total = total + area
    print(total)

f = open("day2.txt")
Day2P2(f)
#Day2P1(f)