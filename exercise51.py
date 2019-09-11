num = 0
tot = 0.0


while True:
    sval = input("Enter a number: ")
    #if done, break the loop and print out
    if sval == 'done':
        break
    #convert this string to a float. If it breaks it, start it again after telling them invalid input.
    try:
        fval=float(sval)
    except:
        print("invalid input.")
        continue
    print(fval)
    #count it
    num = num + 1
    #total it
    tot = tot + fval

print('all done.')
print(tot,num,tot/num)
