from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
orders = defaultdict(set)

for line in stdin:
    if line == '\n':
        break

    a, b = line.split('|')
    orders[int(a)].add(int(b))

for line in stdin:
    queue = line.split(',')
    queue = list(map(int, queue))
    ok = True
    for i in range(len(queue)-1):

        for j in range(i+1, len(queue)):
            if queue[j] not in orders[queue[i]]:
                ok = False
                break

        if ok == False:
            break

    if ok:
        ans += queue[len(queue)//2]

print(ans)
    