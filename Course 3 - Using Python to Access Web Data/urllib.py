import urllib.request, urllib.parse, urllib.error

#This is like "open file"
geturl = input("Please enter a URL")
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

#Go through line for line of the doc
for line in fhand:
    #Split it word for word
    words = line.decode().split()
    #Read through each word and separate
    for word in words:
        #Check if the word is present, if not add 1, either way add 1 to the dictionary
        counts[word] = counts.get(word, 0) + 1

print(counts)
