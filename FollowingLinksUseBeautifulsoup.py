import urllib
from BeautifulSoup import *

def findurl(url, position):
    index = 1
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')

    for tag in tags:
        if index == position:
            url = tag.get('href', None)
            break
        else:
            index += 1
    return url

url = raw_input('Enter URL: ')
count = int (raw_input('Enter Count: '))
position = int (raw_input('Enter Position: '))

print url

for num in range(0, count):
    url = findurl(url, position)
    print url
