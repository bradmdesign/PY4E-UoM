import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

geturl = input("Please enter a URL")
if len(geturl) < 1:
    geturl="http://py4e-data.dr-chuck.net/comments_42.xml"

fhand = urllib.request.urlopen(geturl)

count = 0
totalsum = 0

#commentinfo>comments>comment>count

print('Retrieving', geturl)
uh = urllib.request.urlopen(geturl, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())


stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print('User count:', len(lst))

for item in lst:
    #print('Count: ', item.find('count').text)
    num = int(item.find('count').text)
    count = count + 1
    totalsum = totalsum + num
    

print("Count: ", count)
print("Sum: ", totalsum)


    

