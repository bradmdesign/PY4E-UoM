
import urllib.request, urllib.parse, urllib. error
from bs4 import BeautifulSoup
import ssl
import re



url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
count = 0
totalnum = 0

tags = soup('span')
for tag in tags:
    for stag in tag:
        #print (stag)
        numbcount = int(stag)
        count = count + numbcount
        totalnum = totalnum + 1
    #stag = tag.split()
    #print(stag)

print("Count", count)
print("Sum", totalnum)

