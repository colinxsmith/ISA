import time
import json
import re
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
        stamp=times[i]
        ttt=time.ctime(stamp)
        ttt=re.sub('..:..:..','00:00:00',ttt)
        obb=time.strptime(ttt, "%a %b %d %H:%M:%S %Y")
        stamp=time.mktime(obb)
        alltimes[int(stamp)]=i
        alldata[stock][stamp]=close[i]
history=[int(i) for i in alltimes.keys()]
history.sort()
last=0
n=len(k.keys())
tlen=len(history)-1
week = 7*24*60*60
R=0.02/53
periodlength=[max(1,(history[i+1]-history[i])/week) for i in range(tlen)]
#periodlength)
m=1
DATA='n\n%d\n'%n
DATA+='m\n%d\n'%m
DATA+='nfac\n%d\n'%-1
DATA+='tlen\n%d\n'%(tlen)
DATA+='periodlength\n'
for kk in periodlength:
    DATA+='%d '%kk
DATA+='\nL\n'
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
prices=[0]*int(n*(tlen+1))
tt=0


for stock in k.keys():
    #print (tt,stock)    
    for hhhh in range(tlen+1):
        hhh=history[hhhh]
        hh=time.ctime(hhh).replace(' 00:00:00','')
        
        try:
                if alldata[stock][hhh]!=0.0:
                    last=alldata[stock][hhh]
                    break
        except:pass

    for hhhh in range(tlen+1):
        hhh=history[hhhh]
        hh=time.ctime(hhh).replace(' 00:00:00','')
        try:
            if alldata[stock][hhh]==0.0:alldata[stock][hhh]=last
            #print ('%s %s %f' % (stock,hh,alldata[stock][hhh]))
            last=float(alldata[stock][hhh])
            prices[tt]=alldata[stock][hhh]
            tt+=1
        except:
            #print ('%s %f' % (hh,last))
            prices[tt]=last
            tt+=1
DATA+='\nDATA\n'
tk=0
R=0
for st in range(n):
    for kk in range(tlen):
        R+=(prices[tk+1]/prices[tk]-1)/periodlength[kk]
        DATA+='%.16e '%((prices[tk+1]/prices[tk]-1)/periodlength[kk])
        tk+=1
    DATA+='\n'
R/=float(n*tlen)
DATA+='\nlambda\n1e2\n'
DATA+='R\n%f\n'%(R)
DATA+='\nQQQ\n'
for kk in range(int(n*(n+1)/2)):
    DATA+='0 '
DATA+='\nQ\n  \n'
DATA+='\nalpha\n  \n'
DATA+='gamma\n0.5\n'
DATA+='kappa\n0.5\n'
DATA+='basket\n-1\n'
DATA+='delta\n-1\n'
DATA+='lpower\n1\n'
DATA+='longbasket\n-1\n'
DATA+='shortbasket\n-1\n'
DATA+='minRisk\n-1\n'
DATA+='maxRisk\n-1\n'
DATA+='Rmin\n-1\n'
DATA+='Rmax\n-1\n'
DATA+='LSValue\n1\n'
DATA+='trades\n-1\n'
print(DATA)
