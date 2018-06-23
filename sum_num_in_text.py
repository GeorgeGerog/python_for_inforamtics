import re

txt=open('regex_sum_350185.txt','r')

total=0

for line in txt:
 line=line.rstrip()
 x=re.findall('[0-9]+',line)
 if len(x)>0:
  for i in x:
   total=total+ int(i)
   
print total