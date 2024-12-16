from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0

for line in stdin:
    line = line.strip()
    goal, arr = line.split(':')
    goal = int(goal)
    arr = arr.split()
    arr = list(map(int, arr))

    vals = set([arr[0]])
    newvals = set()

    for i in range(1, len(arr)):
        newvals = set()
        for v in vals:
            newvals.add(v + arr[i])
            newvals.add(v * arr[i])

        vals = newvals.copy()

    if goal in vals:
        ans += goal

print(ans)