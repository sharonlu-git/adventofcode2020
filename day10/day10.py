# Sharon Lu
# Advent of Code Day 10
# day10.py
# 12/13/2020

## Part 1 ##########################################################
# f = open("day10input.txt", "r")
f = open("day10test1.txt", "r")
# f = open("day10test2.txt", "r")
fl = f.readlines()
f.close()
flsplit = []
for x in range(len(fl)):
    fl[x] = int(fl[x].strip("\n"))
fl.sort()
fl.append(max(fl)+3)
fl.insert(0,0)

oneJoltCount = 0
threeJoltCount = 0

for x in range(1,len(fl)):
    if(fl[x] - fl[x-1] == 1):
        oneJoltCount = oneJoltCount + 1
    elif(fl[x] - fl[x-1] == 3):
        threeJoltCount = threeJoltCount + 1


# print("One Jolt Count: %d Three Jolt Count: %d" % (oneJoltCount, threeJoltCount))
# print("One Jolt x Three Jolt = % d" %(oneJoltCount*threeJoltCount))

## Part 2 ##########################################################
numerOfArrangements = 1
# test = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
# test = [4, 5, 6, 7]
test = [1, 2, 3, 4, 5]

def findListOfCombinations(listToSolve, listLength, combinations):
    if listLength == 2:
        combinations.append(listToSolve)
    else:
        findListOfCombinations(listToSolve[0:listLength-1], listLength-1, combinations)
        combinationsLength = len(combinations)
        for x in range(combinationsLength):
            tempList = combinations[x].copy()
            tempList.append(listToSolve[listLength-1])
            combinations[x] = tempList
            if len(tempList) >= 4:
                if(tempList[len(tempList)-4] <= tempList[len(tempList)-1]-3):
                    if (tempList.(len(tempList)-3) == tempList(len(tempList)-4)+1):
                        poppedList = tempList.copy()
                        poppedList.pop(len(tempList)-3)
                        combinations.append(poppedList)
                    poppedList = tempList.copy()
                    poppedList.pop(len(tempList)-2)
                    combinations.append(poppedList)
                    poppedList = tempList.copy()
                    poppedList.pop(1)
                    poppedList.pop(1)
                    combinations.append(poppedList)
            elif len(tempList) == 3:
                if(tempList[len(tempList)-3] <= tempList[len(tempList)-1]-2 and \
                    tempList[2]-tempList[0] <= 3):
                        poppedList = tempList.copy()
                        poppedList.pop(1)
                        combinations.append(poppedList)

combos = []
findListOfCombinations(test, len(test), combos)
combosReduced = [] 
for i in combos: 
    if i not in combosReduced: 
        combosReduced.append(i)
print(combosReduced)

# blah = [1, 1, 2, 3]
# print(blah)
# print(list(set(blah)))