import urllib.request, urllib.parse, urllib.error

#This is like "open file"
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')


#Go through line for line of the page
for line in fhand:
    print(line.decode().strip())

