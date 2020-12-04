# Sharon Lu
# Advent of Code Day 3
# day3.py
# 12/3/2020
import math

input_list = []
column = 0
num_of_trees = 0

## Part 1 ###########################################################################

# f = open("day3test.txt", "r")
f = open("day3input.txt", "r")
fl = f.readlines()
f.close()
input_list_length_iterations = math.ceil(len(fl)*3/len(fl[0]))
for x in fl:
    input_list.append(x.strip('\n')*(1+input_list_length_iterations))

for row in range(1,len(input_list)):
    column = column+3
    if(input_list[row][column]) == "#":
        num_of_trees = num_of_trees + 1

print("Part 1 Number of Trees : %d" % (num_of_trees))

## Part 2 ###########################################################################
num_of_trees_multiplied = 1
num_of_trees = 0
column = 0
right_down = [[1, 1], [1, 3], [1, 5], [1,7], [2,1]]

for x in range(len(right_down)):
    input_list= []
    input_list_length_iterations = math.ceil(len(fl)*right_down[x][1]/len(fl[0]))
    for y in fl:
        input_list.append(y.strip('\n')*(2+input_list_length_iterations))
    for row in range(right_down[x][0],len(input_list),right_down[x][0]):
        column = column+right_down[x][1]
        if(input_list[row][column]) == "#":
            num_of_trees = num_of_trees + 1
    num_of_trees_multiplied = num_of_trees_multiplied * num_of_trees
    column = 0
    num_of_trees = 0

print("Part 2 Number of Trees : %d" %num_of_trees_multiplied)
