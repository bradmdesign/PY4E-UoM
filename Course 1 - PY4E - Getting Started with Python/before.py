largest_so_far = -1
print('Before', largest_so_far)

#Run the_num through this array/set - if the number is greater than the current largest so far, set that as the current largest so far and print it.
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
