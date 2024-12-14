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

    if level != sorted(level) and level != sorted(level, reverse=True):
        continue

    safe = True 

    for i in range(1, len(level)):
        if abs(level[i]-level[i-1]) < 1 or abs(level[i]-level[i-1]) > 3:
            safe = False
            break

    if safe:
        ans += 1

print(ans)