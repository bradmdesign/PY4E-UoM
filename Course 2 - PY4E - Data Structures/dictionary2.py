counts = dict()
names = ['csev ', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
#    if name not in counts:
#        counts[name] = 1
#    else :
#        counts[name] = counts[name] + 1

#Better way of doing this is with get.
    counts[name] = counts.get(name, 0) + 1
print(counts)