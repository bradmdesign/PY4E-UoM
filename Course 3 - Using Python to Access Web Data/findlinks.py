
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://beleave.com')

count = 0

for line in fhand:
    sline = line.decode().strip()
    fline = sline.split()
    for find in fline:
        if 'href' in find:
            print("link found!")
            count = count + 1
print(count)