f = open("day2.txt")
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
#input = f.readline()
