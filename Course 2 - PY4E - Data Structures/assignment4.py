name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()

for line in handle:
    words = line.split()
    #print(words)
    if line.startswith('From '):
        #print(words[5])
        hour = (words[5]).split(':')
        #print(hour[0])
        xhour = hour[0]
        hours[xhour] = hours.get(xhour,0) + 1
        #print("hours: ",hours, "xhour: ",xhour)
        
lst = list()

for key,val in hours.items():
    newtup = (key,val)
    #print(newtup)
    lst.append(newtup)

#print(lst)
lst = sorted(lst)
#print(lst)

for val,key in lst :
    print(val,key)
