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
n=len(k.keys())
m=1
DATA='n\n%d\n'%n
DATA+='m\n%d\n'%m
DATA+='nfac\n%d\n'%-1
DATA+='tlen\n%d\n'%len(history)
DATA+='R\n0\n'
DATA+='L\n'
for kk in range(n):
    DATA+='0 '
DATA+='1\n'
DATA+='U\n'
for kk in range(n):
    DATA+='1 '
DATA+='1\n'
DATA+='A\n'
for kk in range(n-1):
    DATA+='1 '
DATA+='1\n'
DATA+='names\n'
for kk in k.keys():
    DATA+='%s '%kk
DATA+='\nDATA\n'
for stock in k.keys():
    #print (stock)
    for hhh in history:
        hh=time.ctime(hhh).replace(' 00:00:00','')
        try:
            if alldata[stock][hhh]==0.0:alldata[stock][hhh]=last
            #print ('%s %f' % (hh,alldata[stock][hhh]))
            last=float(alldata[stock][hhh])
            DATA+='%f '%alldata[stock][hhh]
        except:
            #print ('%s %f' % (hh,last))
            DATA+='%f '%last
DATA+='\nlambda\n1'
DATA+='\nQ\n'
for kk in range(n*(n+1)/2):
    DATA+='0 '
DATA+='\nalpha\n'
for kk in range(n):
    DATA+='0 '
DATA+='\nlog\n2\n'
print(DATA)