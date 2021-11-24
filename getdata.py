import time

print (time.time())
print (time.ctime(1620601200))

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

from sys import stdin

k=''
for line in stdin.readlines():
    k=json.loads(line)

alldata={}
alltimes={}
for stock in k.keys():
    print('Stock %s'%(stock))
    alldata[stock]={}
    times=k[stock]['timestamp']
    close=k[stock]['close']
    for i in range(len(times)):
        alltimes[int(times[i])]=i
        dd=time.ctime(times[i]).split()
        print('%s %s\t%s'%(dd[1],dd[2],close[i]))
        alldata[stock][times[i]]=close[i]
history=[int(i) for i in alltimes.keys()]
history.sort()
for stock in k.keys():
    print (stock)
    for hh in history:
        try:
            print (hh,alldata[stock][hh])
        except:
            print ('no data')
