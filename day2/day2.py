# Sharon Lu
# Advent of Code Day 2
# day2.py
# 12/2/2020

## Part 1 ##########################################################
num_valid_passwords_pt_1 = 0
input_list = []
f = open("day2input.txt", "r")
# f = open("day2test.txt", "r")
fl = f.readlines()
for x in fl:
    min = int(x[0:x.index("-")])
    max = int(x[x.index("-")+1:x.index(" ")])
    char = x[x.index(" ")+1]
    password = x[x.index(": ")+2:len(x)]
    if(password.count(char) >= min and password.count(char) <= max):
        num_valid_passwords_pt_1 = num_valid_passwords_pt_1 + 1

print("Number of valid passwords for Part 1 : %d" % (num_valid_passwords_pt_1))

## Part 2 ##########################################################
num_valid_passwords_pt_2 = 0
for x in fl:
    lower_index = int(x[0:x.index("-")])
    upper_index = int(x[x.index("-")+1:x.index(" ")])
    char = x[x.index(" ")+1]
    password = x[x.index(": ")+2:len(x)]
    if(password[lower_index-1] == char and password[upper_index-1] != char):
        num_valid_passwords_pt_2 = num_valid_passwords_pt_2 + 1
    elif(password[lower_index-1] != char and password[upper_index-1] == char):
        num_valid_passwords_pt_2 = num_valid_passwords_pt_2 + 1

print("Number of valid passwords for Part 2 : %d" % (num_valid_passwords_pt_2))

f.close()