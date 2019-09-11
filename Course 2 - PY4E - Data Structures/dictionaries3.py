counts = dict()
print('Enter a line of text:')
line = input('')
#You have now turned line into a string
print('Your line: ', line)
#You now take the string "line" and make it into a list, titled "words"
words = line.split()

print('Words:', words)

print('Counting...')
#Now you go through each word in the list "words", and replace "word" with it each time. Each time you add another 1 to the word in your dict when ti comes up.
for word in words:
    counts[word] = counts.get(word,0) + 1

print('Counts', counts)