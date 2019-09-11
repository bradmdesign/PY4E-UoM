abc = 'String converted to list'
splitlist = abc.split()
print(splitlist)
for w in splitlist:
    print(w)

weirdlist = 'this;is;a;bunch;of;words;to;be;split'
splitweirdlist = weirdlist.split(';')
print(splitweirdlist)