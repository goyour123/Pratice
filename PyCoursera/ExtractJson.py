import json
import urllib

#url = raw_input('Enter Location: ')
url = 'http://python-data.dr-chuck.net/comments_261110.json'

input = urllib.urlopen(url)
data = input.read()
info = json.loads(data)

print "Retrieving ", url
print "Retrieved ", len(data)

sum = 0
for item in info['comments']:
    sum += int(item['count'])

print "Sum", sum
