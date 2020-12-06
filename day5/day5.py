# Sharon Lu
# Advent of Code Day 5
# day5.py
# 12/5/2020
import math

## Part 1 ##########################################################
f = open("day5input.txt", "r")
# f = open("day5test.txt", "r")
fl = f.readlines()
f.close()

TOTAL_LINES = 128
upper_row = 127
lower_row = 0
upper_col = 7
lower_col = 0
seat_id = 0
last_id = 0 

for line in fl:
    # Get Row
    for index in range(7):
        if(line[index] == "F"):
            upper_row = math.floor((upper_row-lower_row)/2)+lower_row
        elif(line[index] == "B"):
            lower_row = math.ceil((upper_row-lower_row)/2)+lower_row
    if(line[6] == "B"):
        row = lower_row
    else:
        row = upper_row
    upper_row = 127
    lower_row = 0

    # Get Column
    for index in range(7, 10):
        if(line[index] == "L"):
            upper_col = math.floor((upper_col-lower_col)/2)+lower_col
        elif(line[index] == "R"):
            lower_col = math.ceil((upper_col-lower_col)/2)+lower_col
    if(line[9] == "R"):
        col = lower_col
    else:
        col = upper_col
    upper_col = 7
    lower_col = 0

    seat_id = row * 8 + col
    if(seat_id > last_id):
        last_id = seat_id
    
print("The highest seat ID is : %d" %last_id)

## Part 2 ##########################################################
seat_id_list = []

for line in fl:
    # Get Row
    for index in range(7):
        if(line[index] == "F"):
            upper_row = math.floor((upper_row-lower_row)/2)+lower_row
        elif(line[index] == "B"):
            lower_row = math.ceil((upper_row-lower_row)/2)+lower_row
    if(line[6] == "B"):
        row = lower_row
    else:
        row = upper_row
    upper_row = 127
    lower_row = 0

    # Get Column
    for index in range(7, 10):
        if(line[index] == "L"):
            upper_col = math.floor((upper_col-lower_col)/2)+lower_col
        elif(line[index] == "R"):
            lower_col = math.ceil((upper_col-lower_col)/2)+lower_col
    if(line[9] == "R"):
        col = lower_col
    else:
        col = upper_col
    upper_col = 7
    lower_col = 0

    seat_id = row * 8 + col
    seat_id_list.append(seat_id)

seat_id_list.sort()
lower_seat_id = 0
upper_seat_id = 0
for x in range(1,len(seat_id_list)-2):
    if(seat_id_list[x+1] == seat_id_list[x]+2):
        your_seat_id = seat_id_list[x]+1

print("Your seat is: %d" %your_seat_id)