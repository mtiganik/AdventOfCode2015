import hashlib

input = "abcdef"
charLen = len(input)
for i in range(809045):
    input = input + str(i)
    output = hashlib.md5(input.encode('utf-8')).hexdigest()
    if output.startswith("00000"):
        txt = "found {} output, answer is {}"
        print(txt.format(output, input))
        break
    input = input[:charLen]

print("end of program")