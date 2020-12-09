# Sharon Lu
# Advent of Code Day 7
# day7.py
# 12/8/2020

## Part 1 ##########################################################
KEYCOLOR = "shiny gold"
f = open("day7input.txt", "r")
# f = open("day7test.txt", "r")
fl = f.readlines()
f.close()
containerColor = []
insideColors = []
insideNumbers = [] # For Part 2

for x in fl:
    containIndex = x.index("bags contain")
    containerColor.append(x[0: containIndex-1])
    if x.count("no other bags") == 0:
        insideColorsSplit = x[containIndex+13:len(x)-1].split(", ")
        insideNumberList = [] # for part 2
        for i in range(len(insideColorsSplit)):
            if i == len(insideColorsSplit)-1: ## handle last color in list
                insideColorsSplit[i] = insideColorsSplit[i].strip(".")
            insideColorsSplitList = insideColorsSplit[i].split(" ")
            insideNumberList.append(insideColorsSplitList[0])
            insideColorsSplitList.pop(0)
            insideColorsSplitList.pop(len(insideColorsSplitList)-1)
            spaces = " "
            insideColorsSplit[i] = spaces.join(insideColorsSplitList)
        insideColors.append(insideColorsSplit)
        insideNumbers.append(insideNumberList)
    else:
        insideColors.append("")
        insideNumbers.append(0)

def findContainerColors(colorOfContainer):
    for x in range(len(containerColor)):
        if containerColor[x] != colorOfContainer:
            if(insideColors[x].count(colorOfContainer) > 0):
                if (colorsThatCanContainKey.count(containerColor[x]) == 0):
                    colorsThatCanContainKey.append(containerColor[x])

colorsThatCanContainKey = []
findContainerColors(KEYCOLOR)
index = 0
while(index < len(colorsThatCanContainKey)):
    findContainerColors(colorsThatCanContainKey[index])
    index = index + 1

print("The number of colors that can contain shiny gold are : %d" %len(colorsThatCanContainKey))

## Part 2 ##########################################################
bagColorAndNum = {} # Number is the count of bags INCLUDING the outside container
while KEYCOLOR not in bagColorAndNum:
    for x in range(len(insideColors)):
        if containerColor[x] not in bagColorAndNum:
            hasValidBags = 1
            colorsPerBag = 0
            for y in range (len(insideColors[x])):
                if insideColors[x][y] not in bagColorAndNum:
                    hasValidBags = 0
            if hasValidBags == 1:
                for z in range (len(insideColors[x])):
                    colorsPerBag = colorsPerBag + int(insideNumbers[x][z]) * int(bagColorAndNum[insideColors[x][z]])
                bagColorAndNum[containerColor[x]] = colorsPerBag + 1

print("The number of bags within a %s bag is : %d" %(KEYCOLOR, bagColorAndNum[KEYCOLOR]-1))