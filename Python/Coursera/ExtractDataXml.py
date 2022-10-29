import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
results = tree.findall('comments/comment')

sum = 0
for result in results:
    sum += int(result.find('count').text)

print 'sum', sum
