import time
import json
from sys import stdin
k=''
for line in stdin.readlines():
    k=json.loads(line)
alldata={}
alltimes={}
for stock in k.keys():
    alldata[stock]={}
    times=k[stock]['timestamp']
    close=k[stock]['close']
    for i in range(len(times)):
        alltimes[int(times[i])]=i
        alldata[stock][times[i]]=close[i]
history=[int(i) for i in alltimes.keys()]
history.sort()
last=0
for stock in k.keys():
    print (stock)
    for hhh in history:
        hh=time.ctime(hhh).replace(' 00:00:00','')
        try:
            if alldata[stock][hhh]==0.0:alldata[stock][hhh]=last
            print ('%s %f' % (hh,alldata[stock][hhh]))
            last=alldata[stock][hhh]
        except:
            print ('%s %f' % (hh,last))