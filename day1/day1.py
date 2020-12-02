# Sharon Lu
# Advent of Code Day 1
# day1.py
# 12/1/2020

num_list = []
f = open("day1input.txt", "r")
fl = f.readlines()
for x in fl:
    num_list.append(int(x))
length = len(num_list)

## Part 1 ###############################################################
for y in range(length):
    for z in range(1,length):
        if num_list[y] + num_list[z] == 2020:
            break
        else:
            continue
        break
    else:
        continue
    break

print("Part 1: %d" %(num_list[y]*num_list[z]))

## Part 2 ###############################################################
for x in range(length):
    for y in range(1,length):
        for z in range(2,length):
            if num_list[x] + num_list[y] + num_list[z] == 2020:
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

print("Part 2: %d" %(num_list[x]*num_list[y]*num_list[z]))

f.close()