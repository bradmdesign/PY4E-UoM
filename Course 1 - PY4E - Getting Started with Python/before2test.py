
#This script runs through the numbers, compares the numbers, counts how many numbers total and produces a sum.
biggest_number = -1
count = 0
total = 0

print("Begin")
for current_number in [1,42,42,73,14,62,77,53,16,87]:
    print(current_number, "vs", biggest_number)
    count = count + 1
    total = total + current_number
    if current_number > biggest_number:
        biggest_number = current_number
    print("winner is", biggest_number)
    print("Current count is", count)
    print("Total number is", total)
    print("Average is", total/count)
print("Done!")
