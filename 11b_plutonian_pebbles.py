from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
from functools import cache
import heapq

arr = []
ans = 0

for line in stdin:
    line = line.strip()
    arr = line.split()
    arr = list(map(int, arr))

@cache
def go(num, times):
    if times == 0:
        return 1
    
    if num == 0:
        return go(1, times-1)

    elif len(str(num))%2 == 0:
        s = str(num)
        n = len(s)//2
        return go(int(s[0:n]), times-1) + go(int(s[n:]), times-1)
    
    else:
        return go(num*2024, times-1)

for num in arr:
    ans += go(num, 75)

print(ans)