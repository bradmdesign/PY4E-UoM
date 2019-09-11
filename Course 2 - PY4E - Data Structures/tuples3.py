fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    #print(words)
    for word in words:
        print(word)
        #Grab the counts dictionary, find the word being run, add 1. If it doesnt exist, set it to 0, then add 1. Right to left!
        counts[word] = counts.get(word, 0) + 1
        print(counts[word])

#Make an empty list
lst = list()
#Grab the key and value for everything in the dict counts. "items" makes sure it grabs both.
for key, val in counts.items() :
    #Switch them around - this being in a bracket makes it a tuple. Value, key means number, name.
    newtup = (val, key)
    #grab each value and add the newtup values in val,key order to the list.
    lst.append(newtup)

#Sort it in reverse.
lst = sorted(lst, reverse=True)

#first 10
for val,key in lst[:10] :
    #Show it the order we want.
    print(key,val)

#Shorten it all:
c = {'a':10, 'b':1, 'c': 22}
print(sorted([(v,k) for k,v in c.items()]))

#List Comprehension