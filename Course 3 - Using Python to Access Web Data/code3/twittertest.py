import urllib.request, urllib.parse, urllib.error
import oauth
from twurl import augment
import ssl

print("Calling twitter")
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'bradmdesign', 'count': '2'})
print(url)

#ignore ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data.decode)
headers = dict(connection.getheaders())
print("Remaining x-rate: ", headers['x-rate-limit-remaining'])