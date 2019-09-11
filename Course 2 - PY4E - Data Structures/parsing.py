data = "From stephen.marquard@uct.ac.za  Sat Jan 5 09:14:16 2008"
startposition = data.find('@')
finishposition = data.find('  ')
host = data[startposition+1 : finishposition]
handle = data[0:startposition]
date = data [finishposition:]
print(startposition)
print(finishposition)
print("Host: ", host)
print("Handle: ", handle.capitalize())
print("Date: ", date)