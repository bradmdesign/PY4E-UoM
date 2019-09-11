import re

#x = open('mbox-short.txt')
#for line in x:
#    y = re.findall('^From (\S+@\S+)', line
#        print(y)
#y = re.findall('\S+@\S+', x)
#print(y)

# Find way of doing this:
data = 'From stephen.marquard@uct.ac.za Sat Jun  5 09:14:16 2008'
#atpos = data.find('@')
#print(atpos)
#sppos = data.find(' ',atpos)
#print(sppos)
#host = data[atpos+1 : sppos]
#print(host)

#Double Split way:

words = data.split()
print(words)
email = words[1]
pieces = email.split('@')
print(pieces)
print(pieces[1])