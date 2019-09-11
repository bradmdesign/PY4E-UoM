d = {'a':10, 'd':4, 'b':1, 'c':22}
t = sorted (d.items())
tmp = list()

print("original:", d)
print("sorted tuple:", t)
#This sorts the tuples alphabetically based on the key's first letter/digit
for k,v in sorted(d.items()):
    print("Re-sorting (k-v to v-k)")
    tmp.append((v,k))

print(tmp)
tmp = sorted(tmp)
print(tmp)
tmp = sorted(tmp,reverse=True)
print("Reversed: ", tmp)


