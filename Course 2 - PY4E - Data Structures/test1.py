fname = input("Give us a file name.")
filename = open(fname)
for line in filename:
    line = line.rstrip()
    print(line.upper())