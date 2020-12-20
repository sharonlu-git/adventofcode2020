# Sharon Lu
# Advent of Code Day 9
# day9.py
# 12/11/2020

## Part 1 ##########################################################
f = open("day9input.txt", "r")
#f = open("day9test.txt", "r")
fl = f.readlines()
f.close()
LENGH_OF_PREAMBLE = 25

def checkPreviousInputs(listOfFive, valueToCheck):
	valueIsSum = 0
	for x in range(len(listOfFive)-1):
		for y in range(x+1, len(listOfFive)):
			if(listOfFive[x] + listOfFive [y] == valueToCheck):
				return 1
	return 0

## Remove \n from each entry
for x in range(len(fl)):
	fl[x] = int(fl[x].strip("\n"))

for x in range(LENGH_OF_PREAMBLE,len(fl)):
	if checkPreviousInputs(fl[x-LENGH_OF_PREAMBLE:x], fl[x]) == 0:
		badNum = fl[x]
		break

print("The number that does not follow the rules is : %d" %badNum)
## Part 2 ##########################################################
lowerIndex = 0
upperIndex = 0
badNumReached = 0
for x in range(len(fl)-1):
	if badNumReached == 0:
		total = fl[x]
		for y in range(x+1, len(fl)):
			total = total + fl[y]
			if total > badNum:
				break
			elif total == badNum:
				badNumReached = 1
				lowerIndex = x
				upperIndex = y
				break
	else:
		break

part2val = min(fl[lowerIndex:upperIndex+1]) + max(fl[lowerIndex:upperIndex+1])
print("The answer for part 2 is: %d" %part2val)

