import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
count=int(raw_input('Enter count:'))
position=int(raw_input('Enter position:'))

print 'Retrieving', url

numcount=0

while True:
 numposition=1
 html = urllib.urlopen(url).read()
 soup = BeautifulSoup(html,"html.parser")
 tags = soup('a')
 for tag in tags:
  if(numposition==position):
   print 'Retrieving', tag.get('href', None)
   url=tag.get('href', None)  
   break
  numposition=numposition+1 
 numcount=numcount+1
 if numcount==count: break 
  




    