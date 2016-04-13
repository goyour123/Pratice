#Sum the numbers in span anchor tags

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
#Sample URL: http://python-data.dr-chuck.net/comments_42.html
#Actual URL: http://python-data.dr-chuck.net/comments_261109.html

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

sum = 0
for tag in tags:
    sum += int(tag.contents[0])

print sum