import re

hand = open('regex_sum_278160.txt')
numlist = list()
count = 0

for line in hand:
    line = line.rstrip()
    #Look for a number and if found, add 1
    if re.findall('([0-9]+)', line):
        number = re.findall('([0-9]+)', line)
        for indinum in number:
            newnum = int(indinum)
            numlist.append(newnum)
            count = count + 1
        print("line: ", line)
        print("Number: ", number)
      #  numlist.append(float(number[:])
        print("Numlist: ", numlist)


print("Sum: ", sum(numlist))
print("Count: ", count)