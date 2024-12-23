from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

arr = []
ans = 0

for line in stdin:
    line = line.strip()
    arr = line.split()
    arr = list(map(int, arr))

def run(arr):
    newarr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            newarr.append(1)
        elif len(str(arr[i]))%2 == 0:
            s = str(arr[i])
            n = len(s)//2
            newarr.append(int(s[0:n]))
            newarr.append(int(s[n:]))
        else:
            newarr.append(arr[i] * 2024)

    return newarr

for i in range(75):
    arr = run(arr)

print(len(arr))