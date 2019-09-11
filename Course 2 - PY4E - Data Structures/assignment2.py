# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
totalspam = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        currentnumber = line[20:]
        totalspam = totalspam + float(currentnumber)
#        print(currentnumber)
#        print(count)
print("Average spam confidence:", totalspam/count)

