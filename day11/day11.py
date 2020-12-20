# Sharon Lu
# Advent of Code Day 11
# day11.py
# 12/14/2020
import copy

## Part 1 ##########################################################
# f = open("day11input.txt", "r")
f = open("day11test.txt", "r")
fl = f.readlines()
f.close()
stringOfFloorSpaces = "." *(len(fl)+2)
fl.insert(0,stringOfFloorSpaces)
fl.append(stringOfFloorSpaces)
for x in range(1,len(fl)-1):
    fl[x] = (fl[x].strip("\n"))
    fl[x] = "." + fl[x] + "."
for x in range(len(fl)):
    fl[x] = list(fl[x])
flpt2 = copy.deepcopy(fl)

def seatStatusNextRound(matrixOfSeats, seatRow, seatColumn):
    if (matrixOfSeats[seatRow][seatColumn] == '.'):
        return '.'
    elif(matrixOfSeats[seatRow][seatColumn] == 'L'):
        for x in range(seatRow-1, seatRow+2):
            for y in range(seatColumn-1, seatColumn+2):
                if matrixOfSeats[x][y] == '#':
                    return 'L'
        else:
            return '#'
    elif(matrixOfSeats[seatRow][seatColumn] == '#'):
        adjacentOccupiedCount = 0
        for x in range(seatRow-1, seatRow+2):
            for y in range(seatColumn-1, seatColumn+2):
                if matrixOfSeats[x][y] == '#':
                    adjacentOccupiedCount = adjacentOccupiedCount + 1
        if adjacentOccupiedCount > 4:
            return 'L'
        else:
            return '#'
    
newSeatArrangement = copy.deepcopy(fl)
seatingDoesntChange = 0
while seatingDoesntChange == 0:
    for x in range(1,len(fl)-1):
        for y in range(1,len(fl[0])-1):
            newSeatArrangement[x][y] = seatStatusNextRound(fl,x,y)
    if newSeatArrangement == fl:
        seatingDoesntChange = 1
    else:
        fl = copy.deepcopy(newSeatArrangement)

numberOfOccupiedSeats = 0
for x in range(len(fl)):
    for y in range(len(fl[x])):
        if fl[x][y] == '#':
            numberOfOccupiedSeats = numberOfOccupiedSeats + 1

print("Part 1 Number of Occupied Seats is : %d" %numberOfOccupiedSeats)

## Part 2 ##########################################################
def seatStatusNextRoundPart2(matrixOfSeats, seatRow, seatColumn):
    if (matrixOfSeats[seatRow][seatColumn] == '.'):
        return '.'
    elif(matrixOfSeats[seatRow][seatColumn] == 'L'):
        directionFound = []
        for x in range(seatRow, -1, -1):
            if directionFound.count("N") == 0 and matrixOfSeats[x][seatColumn] == '#':
                print(x)
                print(seatColumn)
                return 'L'
        else:
            return '#'
    
# newSeatArrangement = copy.deepcopy(fl)
# seatingDoesntChange = 0
# while seatingDoesntChange == 0:
#     for x in range(1,len(fl)-1):
#         for y in range(1,len(fl[0])-1):
#             newSeatArrangement[x][y] = seatStatusNextRound(fl,x,y)
#     if newSeatArrangement == fl:
#         seatingDoesntChange = 1
#     else:
#         fl = copy.deepcopy(newSeatArrangement)

# numberOfOccupiedSeats = 0
# for x in range(len(fl)):
#     for y in range(len(fl[x])):
#         if fl[x][y] == '#':
#             numberOfOccupiedSeats = numberOfOccupiedSeats + 1

# print("Part 2 Number of Occupied Seats is : %d" %numberOfOccupiedSeats)
