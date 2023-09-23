import time
import json
import re
from sys import stdin
k=''
fund=''
for line in stdin.readlines():
    k=json.loads(line)
for op in k.keys():
    fund=k[op]['result'][0]
print(fund['underlyingSymbol'],fund['quote']['longName'],fund['quote']['dividendYield'])