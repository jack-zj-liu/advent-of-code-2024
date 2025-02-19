from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = 0
vals, parents, operation, indegree, children = dict(), dict(), dict(), Counter(), defaultdict(list)

for line in stdin:
    if line == '\n':
        break

    a, b = line.strip().split()
    vals[a[0:3]] = int(b)

for line in stdin:
    a, op, b, _, c = line.strip().split()
    parents[c] = (a, b)
    operation[c] = op
    indegree[c] = 2
    children[a].append(c)
    children[b].append(c)

bfs = deque(vals.keys())

def eval(c):
    a, b = parents[c]
    aval, bval, op = vals[a], vals[b], operation[c]
    if op == 'AND':
        return aval & bval
    if op == 'OR':
        return aval | bval
    if op == 'XOR':
        return aval ^ bval

while bfs:
    curr = bfs.popleft()

    for c in children[curr]:
        indegree[c] -= 1
        if indegree[c] == 0:
            bfs.append(c)
            vals[c] = eval(c)

zkeys = []
for k, v in vals.items():
    if k[0] == 'z':
        zkeys.append((k, v))

zkeys.sort()

for i in range(len(zkeys)):
    ans |= zkeys[i][1] << i

print(zkeys)
print(ans)
