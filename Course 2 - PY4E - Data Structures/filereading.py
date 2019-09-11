# \n means newline
#stuff = 'Hello \nWorld!'
#print(stuff)
#print(len(stuff))
#count = 0
#xfile = open('mbox.txt')
#totalchars = xfile.read()
#for cheese in xfile:
#    count = count +1
#print("Lines: ", count)
#print("Characters: ", len(totalchars))
#print(totalchars)


fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line.rstrip())


fartbox = open("mbox.txt")
for line in fartbox:
    line = line.rstrip()
    #Skip lines that dont start with s
  #  if not line.startswith("s"):
   #     continue
    #and then print the ones that do
    #print(line)
    if 'gh' in line:
        continue
    print(line)

