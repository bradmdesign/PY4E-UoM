import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

geturl = input("Please enter a URL")
if len(geturl) < 1:
    geturl="http://py4e-data.dr-chuck.net/comments_42.json"


count = 0
totalsum = 0

print('Retrieving', geturl)

#Make the connection
connection = urllib.request.urlopen(geturl, context=ctx)
#Convert the data and make it readable
data = connection.read().decode()
#Make it json readable
js = json.loads(data)
print(json.dumps(js, indent=2))

#for every comments line
for u in js['comments']:
    #Pull the count number and add it to totalsum
    totalsum = u['count'] + totalsum
    count = count + 1




    

print("Count: ", count)
print("Sum: ", totalsum)


    

