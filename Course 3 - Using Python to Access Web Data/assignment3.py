import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
#Turn into an integer, this is how many links it will give you
countx = int(count)
position = input('Enter position: ')
#Turn into integer, this is the position it will begin on
positionx = int(position)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
names = list()
ticker = 0

# Retrieve all of the anchor tags
tags = soup('a')

#As long as we haven't maxed out, keep the loop going
while ticker != countx:

    #Run it again and reset
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #Track with: print("Cycle 1A")

    #Start at the position and go x amount of times
    for tag in tags[(positionx - 1):]:

        print("Retrieving: ", tag.get('href', None))
        url = tag.get('href', None)
        ticker = ticker + 1
        # Track with: print("Cycle 1B")
        break

        #names.append(stag)
        if ticker == countx:
            break

        #Uncommenting below would get you the exact names
        #for stag in tag:
        #    ticker = ticker + 1
        #    names.append(stag)
        #    if ticker = countx:
        #        break
            #print(stag)

#print(tag[0:4])
#print(names[positionx])
