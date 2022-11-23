
#list = ["ab","bc","cd","de","ef","fg","gh","hi","ij","jk","kl","lm","mn","no","op","pq","qr","rs","st","tu","uv","vw","wx","xy","yz"]
def checkContiniousLetter(input):
    list=["ab","cd","pq","xy"]
    for i in list:
        if i in input:
            text = "same letter, {} in {}, continue"
            #print(text.format(i, input))
            return True
    return False

def checkDoubleLetters(input):
    for i in range(1, len(input)):
        if input[i-1] == input[i]: return True
    return False

def checkWovels(input):
    count = 0
    for x in input:
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            count = count +1
    if count >= 3: return True
    return False





f = open("day5.txt")

count = 0
for x in f:
    if checkContiniousLetter(x):
        continue
    if checkDoubleLetters(x) and checkWovels(x): 
        count = count +1
text = "count is {}"
print(text.format(count))
