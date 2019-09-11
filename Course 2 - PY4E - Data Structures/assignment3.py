handle = open('mbox-short.txt')
counts = dict()
for line in handle:
    email = line.split()
    if line.startswith("From ") :
       #print(email[1])
        counts[email[1]] = counts.get(email[1],0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword,bigcount)
