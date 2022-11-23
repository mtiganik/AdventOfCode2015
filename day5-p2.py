def checkTwoLettersAppearTwice(input):
    for i in range(0, len(input)-3):
        strToCompare = input[i] + input [i+1]
        for j in range(i+2, len(input)-1):
            str = input[j]+input[j+1]
            if strToCompare == str: 
                return True
    return False

def checkLetterOneLetterBetween(input):
    for i in range(len(input)-2):
        if input[i] == input[i+2]: 
            return True
    return False

f = open("day5.txt")

count = 0
for x in f:
    if checkLetterOneLetterBetween(x) and checkTwoLettersAppearTwice(x): 
        count = count +1
        continue
text = "count is {} "
print(text.format(count))


# print(checkTwoLettersAppearTwice("xyxy")) #true
# print(checkTwoLettersAppearTwice("aabcdefgaa")) #true
# print(checkTwoLettersAppearTwice("aaa")) #false
# print(checkTwoLettersAppearTwice("aaaa")) #true
# print(checkTwoLettersAppearTwice("qjhvhtzxzqqjkmpb")) #true
# print(checkTwoLettersAppearTwice("xxyxx")) #true
# print(checkTwoLettersAppearTwice("uurcxstgmygtbstg")) #true
# print(checkTwoLettersAppearTwice("ieodomkazucvgmuy")) #false

# print(checkLetterOneLetterBetween("xyxy")) #true
# print(checkLetterOneLetterBetween("aabcdefgaa")) #false
# print(checkLetterOneLetterBetween("aabbddggaa")) #false
# print(checkLetterOneLetterBetween("aaa")) #true
# print(checkLetterOneLetterBetween("abcdefeghi")) #true
# print(checkLetterOneLetterBetween("qjhvhtzxzqqjkmpb")) #true
# print(checkLetterOneLetterBetween("xxyxx")) #true
# print(checkLetterOneLetterBetween("uurcxstgmygtbstg")) #false
# print(checkLetterOneLetterBetween("ieodomkazucvgmuy")) #true

# print(checkLetterOneLetterBetween("qjhvhtzxzqqjkmpb") and checkTwoLettersAppearTwice("qjhvhtzxzqqjkmpb")) 
# print(checkLetterOneLetterBetween("xxyxx") and checkTwoLettersAppearTwice("xxyxx"))
# print(checkLetterOneLetterBetween("uurcxstgmygtbstg") and checkTwoLettersAppearTwice("uurcxstgmygtbstg"))
# print(checkLetterOneLetterBetween("ieodomkazucvgmuy") and checkTwoLettersAppearTwice("ieodomkazucvgmuy"))
# print(checkLetterOneLetterBetween("kpslrrrljgtjiqka") and checkTwoLettersAppearTwice("kpslrrrljgtjiqka")) 
# print(checkLetterOneLetterBetween("edpizkxnsxeeebfl") and checkTwoLettersAppearTwice("edpizkxnsxeeebfl"))
# print(checkLetterOneLetterBetween("zkhunhhhigbsslfk") and checkTwoLettersAppearTwice("zkhunhhhigbsslfk"))
# print(checkLetterOneLetterBetween("tuyajhkexrrrvnlb") and checkTwoLettersAppearTwice("tuyajhkexrrrvnlb"))
