fh = open('romeo.txt')
lst = list()
for line in fh:
    #print(line.rstrip())
    words = line.split()
    for moresplit in words:
        #print(moresplit)
        if moresplit not in lst:
            lst.append(moresplit)

lst.sort()
print(lst)
#finalwords.sort
#print(finalwords)

