smallest = None
print("We'll start with nothing and determine the lowest number.")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('Lowest is', smallest)
