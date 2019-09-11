
#Search using a Boolean Variable

#We are going to search for the number 3
found = False
print('Before', found)

for value in [1,2,3,4,5]:
    print('Found',value)
    if value == 3:
        print('Found the number', value)
        found = True
        break
print('After', found)
