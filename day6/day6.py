# Sharon Lu
# Advent of Code Day 6
# day6.py
# 12/8/2020

## Part 1 ##########################################################
f = open("day6input.txt", "r")
# f = open("day6test.txt", "r")
fl = f.readlines()
f.close()
group_entries = []
letters = "abcdefghijklmnopqrstuvwxyz"
line = 0
group_counts = 0
total_counts = 0

for x in fl:
	group_entries.append(x.strip("\n"))
	if(x == "\n" or line == len(fl)-1):
		if(x == "\n"):
			group_entries.pop(len(group_entries)-1) 
		print(group_entries)
		for y in range(len(letters)):
			letter_present = 0
			for z in group_entries:
				if z.count(letters[y]) > 0:
					letter_present = 1
			if letter_present == 1:
				group_counts = group_counts +1;

		group_entries = []
		print(group_counts)
		total_counts = total_counts + group_counts
		group_counts = 0

	line = line + 1

print("The total count for Part 1 is : %d" %total_counts)

## Part 2 ##########################################################
group_entries = []
letters = "abcdefghijklmnopqrstuvwxyz"
line = 0
group_counts = 0
total_counts = 0

for x in fl:
	group_entries.append(x.strip("\n"))
	if(x == "\n" or line == len(fl)-1):
		if(x == "\n"):
			group_entries.pop(len(group_entries)-1) 
		print(group_entries)
		for y in range(len(letters)):
			letter_present = 0
			for z in group_entries:
				if z.count(letters[y]) > 0:
					letter_present = letter_present + 1
			if letter_present == len(group_entries):
				group_counts = group_counts +1;

		group_entries = []
		print(group_counts)
		total_counts = total_counts + group_counts
		group_counts = 0

	line = line + 1

print("The total count for Part 2 is : %d" %total_counts)
