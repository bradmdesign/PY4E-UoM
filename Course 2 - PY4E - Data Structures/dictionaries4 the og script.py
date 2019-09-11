
name = input('Enter file:')
handle = open(name)

#Making an empty dictionary
counts = dict()
#go through the file line by line
for line in handle:
    #and then split each one under "words"
    words = line.split()
    #and then split, and add to the counts dict each time you cycle through.
    for word in words:
        counts[word] = counts.get(word,0) + 1

print(counts) 

#Now we're going to figure out which word is biggest
# Set them both to None because they start with no value
bigcount = None
bigword = None
#Now, set the key and values as "word" and "count", use count.items() because it will give you BOTH values.
for word,count in counts.items():
    #if bigcount is None or lower than the current value it's drawing, set it as the new highest count (bigcount). Set the bigword accordingly.
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)