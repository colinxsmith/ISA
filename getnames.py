import json
from sys import stdin
k=''
for line in stdin.readlines():
    k=json.loads(line)

names={}
for stock in k['quoteResponse']['result']:
    #print(stock['symbol'],stock['shortName'],stock['regularMarketPrice'])
    names[stock['symbol']]=stock['shortName'].strip().replace(' ','_')
print(names)