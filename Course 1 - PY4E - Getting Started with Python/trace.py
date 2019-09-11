x = "Hey bob"
try:
    x = x + 1
except:
    print("That didn't work, let's try again.")
x = input("Give us a number: ")
try:
    x = int(x) + 1
    print(x)
except:
    print("That didn't work, you should give up.")
