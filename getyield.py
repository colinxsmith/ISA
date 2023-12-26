import time
import json
import re
from sys import stdin
from os import system
k=''
fund=''
for line in stdin.readlines():
    k=json.loads(line)
for op in k.keys():
    fund=k[op]['result'][0]
stock=fund['underlyingSymbol']
longname=fund['quote']['longName']
longname=longname.replace(' ','_')
longname=longname.replace('&','and')
#print (longname)
system('sed -i "s/%s/%s/" GLdist' % (stock,longname))
print(fund['underlyingSymbol'],fund['quote']['longName'],fund['quote']['dividendYield'])
