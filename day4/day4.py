# Sharon Lu
# Advent of Code Day 4
# day4.py
# 12/4/2020

## Part 1 ##########################################################
f = open("day4input.txt", "r")
# f = open("day4test.txt", "r")
fl = f.readlines()
f.close()

num_valid = 0
is_invalid = 0
input_segment = []
counts = [0, 0, 0, 0, 0, 0, 0]
for x in fl:
    input_segment.append(x)
    if(x == "\n" or x == fl[len(fl)-1]):
        ## Get Input Length
        if (x != fl[len(fl)-1]):
            input_length = len(input_segment) - 1
        else:
            input_length = len(input_segment)
        for y in range(input_length):
            counts[0] = counts[0] + input_segment[y].count("byr")
            counts[1] = counts[1] + input_segment[y].count("iyr")
            counts[2] = counts[2] + input_segment[y].count("eyr")
            counts[3] = counts[3] + input_segment[y].count("hgt")
            counts[4] = counts[4] + input_segment[y].count("hcl")
            counts[5] = counts[5] + input_segment[y].count("ecl")
            counts[6] = counts[6] + input_segment[y].count("pid")
        if (sum(counts) == 7):
            num_valid = num_valid + 1
        input_segment = []
        counts = [0, 0, 0, 0, 0, 0, 0]

print("Part 1 Number of Valid Passports: %d" %num_valid)

## Part 2 ##########################################################
f = open("day4input.txt", "r")
# f = open("day4test.txt", "r")
fl = f.readlines()
f.close()

num_valid = 0
input_segment = []
input_split_string = []
passport_valid = 1
passport = {}
field_vals = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for x in fl:
    input_segment.append(x.strip("\n"))
    # Create Dictionary Entry of Passport
    if(x == "\n" or x == fl[len(fl)-1]):
        ## Get Input Length
        if (x != fl[len(fl)-1]):
            input_length = len(input_segment) - 1
        else:
            input_length = len(input_segment)
        for y in range (input_length):
            split_string = input_segment[y].split(" ")
            for z in split_string:
                input_split_string.append(z)
        for input_string in input_split_string:
            for field in field_vals:
                if(input_string.count(field)>0 and len(input_string) > 4):
                    index_of_field = input_string.index(field)
                    passport[field] = input_string[index_of_field+4:len(input_string)]
        if(len(passport) == 7): ## Checks for 7 valid fields
            if(len(passport["byr"]) < 4 or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002):
                passport_valid = 0
            if(len(passport["iyr"]) < 4 or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020):
                passport_valid = 0
            if(len(passport["eyr"]) < 4 or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030):
                passport_valid = 0
            if(passport["hgt"].count("cm") == 1):
                if(passport["hgt"].index("cm") == len(passport["hgt"])-2):
                    if (int(passport["hgt"][0:len(passport["hgt"])-2]) < 150 or int(passport["hgt"][0:len(passport["hgt"])-2]) > 193):
                        passport_valid = 0
                else:
                    passport_valid = 0
            elif(passport["hgt"].count("in") == 1):
                if(passport["hgt"].index("in") == len(passport["hgt"])-2):
                    if (int(passport["hgt"][0:len(passport["hgt"])-2]) < 59 or int(passport["hgt"][0:len(passport["hgt"])-2]) > 76):
                        passport_valid = 0
                else:
                    passport_valid = 0
            else:
                passport_valid = 0
            if(passport["hcl"][0] == "#" and len(passport["hcl"]) == 7):
                hcl_values = "0123456789abcdef"
                for hcl_index in range(1,7):
                    if(hcl_values.count(passport["hcl"][hcl_index]) == 0):
                        passport_valid = 0
            else:
                passport_valid = 0
            ecl_colors = "amb blu brn gry grn hzl oth"
            if(ecl_colors.count(passport["ecl"]) == 0):
                passport_valid = 0
            if(len(passport["pid"]) == 9):
                if(not passport["pid"].isdigit()):
                    passport_valid = 0
            else:
                passport_valid = 0

            if passport_valid == 1:
                num_valid = num_valid + 1
            
        input_segment = []
        input_split_string = []
        passport = {}
        passport_valid = 1

print("Part 2 Number of Valid Passports: %d" %num_valid)