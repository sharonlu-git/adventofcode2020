# Sharon Lu
# Advent of Code Day 8
# day8.py
# 12/9/2020

## Part 1 ##########################################################
f = open("day8input.txt", "r")
# f = open("day8test.txt", "r")
fl = f.readlines()
f.close()
flsplit = []
indexesAddressed = []
for x in fl:
    flsplit.append(x.strip("\n").split(" "))

index = 0
acc = 0

def addSubtract(numToAddSub, numString):
    if(numString[0] == '+'):
        numToAddSub = numToAddSub + int(numString[1:len(numString)])
    else:
        numToAddSub = numToAddSub - int(numString[1:len(numString)])
    return numToAddSub

while(indexesAddressed.count(index) == 0):
    indexesAddressed.append(index)
    if(flsplit[index][0] == "nop"):
        index = index + 1
    elif(flsplit[index][0] == "acc"):
        acc = addSubtract(acc, flsplit[index][1])
        index = index + 1
    elif(flsplit[index][0] == "jmp"):
        index = addSubtract(index, flsplit[index][1])
print("The ACC Value for Part 1 is : %d" % acc)

## Part 2 ##########################################################
problemIndexFound = 0
indexToChange = 0
while(problemIndexFound == 0 and len(flsplit) > indexToChange):
    ## Switch jmp for nop and vice versa
    while (len(flsplit) > indexToChange):
        if(flsplit[indexToChange][0] == "nop"):
            if(flsplit[indexToChange][1][1] != '0'):
                flsplit[indexToChange][0] = "jmp"
                break
        elif(flsplit[indexToChange][0] == "jmp"):
            flsplit[indexToChange][0] = "nop"
            break
        elif(indexToChange == len(flsplit)-1):
            break
        indexToChange = indexToChange + 1

    indexesAddressed = []
    index = 0
    acc = 0
    while(indexesAddressed.count(index) == 0 and index < len(flsplit)):
        indexesAddressed.append(index)
        if(flsplit[index][0] == "nop"):
            index = index + 1
        elif(flsplit[index][0] == "acc"):
            acc = addSubtract(acc, flsplit[index][1])
            index = index + 1
        elif(flsplit[index][0] == "jmp"):
            index = addSubtract(index, flsplit[index][1])
        if index >= len(flsplit):
            problemIndexFound = 1

    # Switch back
    if(flsplit[indexToChange][0] == "nop"):
        flsplit[indexToChange][0] = "jmp"
    elif(flsplit[indexToChange][0] == "jmp"):
        flsplit[indexToChange][0] = "nop"

    if problemIndexFound == 1:
        blah = 0
    else:
        indexToChange = indexToChange + 1
print("The ACC Value for Part 2 is : %d" % acc)