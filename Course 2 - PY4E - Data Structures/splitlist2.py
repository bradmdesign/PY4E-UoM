fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        email = (words[1])
        pieces = email.split('@')
        name = pieces[0]
        print("Name: ", name)