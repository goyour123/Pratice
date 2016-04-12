import urllib
import re

fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')

#
# Prtint First Page
#
for line in fhand:
    line = line.strip()
    print line
    hrefs = re.findall('href=\"(.*)\"', line)
    if len(hrefs) != 0:
        shand = urllib.urlopen (hrefs[0])

print

#
#  Print Second Page
#
for line in shand:
    line = line.strip()
    print line
