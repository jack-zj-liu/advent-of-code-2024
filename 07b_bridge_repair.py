from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
inputs = []
valid = set()

for line in stdin:
    line = line.strip()
    goal, arr = line.split(':')
    goal = int(goal)
    arr = arr.split()
    arr = list(map(int, arr))
    inputs.append([goal, arr])

for goal, arr in inputs:
    vals = set([arr[0]])
    newvals = set()

    for i in range(1, len(arr)):
        newvals = set()
        for v in vals:
            p1, p2, p3 = v + arr[i], v * arr[i], v * 10**len(str(arr[i])) + arr[i]
            if p1 <= goal:
                newvals.add(p1)
            if p2 <= goal:
                newvals.add(p2)
            if p3 <= goal:
                newvals.add(p3)
        
        vals = newvals.copy()

    if goal in vals:
        ans += goal
        valid.add(goal)
        
print(ans)