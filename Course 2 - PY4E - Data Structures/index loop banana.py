#fruit = 'banana'
#index = 0
#while index < len(fruit):
#    letter = fruit[index]
#    print(index, letter)
#    index = index + 1

count = 0
fruit = 'banana'
#0:4 means coutn the letters up to and not including 4 from 0.
for letter in fruit[0:4]:
    if letter == 'a':
        count = count + 1
        #using in to find strings within strings
    if 'n' in fruit:
        print("Hey, I found an N")
    print(letter)
print(count, "letter As")

