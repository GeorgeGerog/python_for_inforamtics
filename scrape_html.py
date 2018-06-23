import urllib
from bs4 import BeautifulSoup
#from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# Retrieve a list of anchor tags
#Each tag is like a dictionary of HTML attributes
tags = soup('span')
total=0
for tag in tags:
 #Look at the parts of tag
 #print 'Tag:', tag
 #print 'Url:', tag.get('href',None)
 #print 'Content:',tag.contents[0] 
 #print 'Attrs', tag.attrs
 total=total +int(tag.contents[0])
print 'sum:',total 