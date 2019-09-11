largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        intnum = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = intnum
    if smallest is None:
        smallest = intnum
    if intnum < smallest:
        smallest = intnum
    if intnum > largest:
        largest = intnum

#    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
