from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0

for line in stdin:
    level = line.split()
    level = list(map(int, level))

    for i in range(len(level)):
        newlevel = level[0:i] + level[i+1:]

        if newlevel != sorted(newlevel) and newlevel != sorted(newlevel, reverse=True):
            continue

        safe = True 

        for i in range(1, len(newlevel)):
            if abs(newlevel[i]-newlevel[i-1]) < 1 or abs(newlevel[i]-newlevel[i-1]) > 3:
                safe = False
                break

        if safe:
            ans += 1
            break

print(ans)