from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

matrix = []
ans = set()
PATH_LEN = 72428

for line in stdin:
    line = list(line.strip())
    matrix.append(line)

n, m = len(matrix), len(matrix[0])
r, c = 0, 0
endr, endc = 0, 0

direc = ((-1, 0), (0, 1), (1, 0), (0, -1))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            r, c = i, j
        if matrix[i][j] == 'E':
            endr, endc = i, j

minheap = [(0, r, c, 1, set())] # cost, row, col, direction, path
cheapest = dict()
pathto = dict()

while minheap:
    cost, r, c, d, path = heapq.heappop(minheap)

    if (r, c) == (endr, endc) and cost == PATH_LEN:
        ans |= path
        continue

    if cost > PATH_LEN: 
        continue

    if (r, c, d) in cheapest:
        if cheapest[(r, c, d)] < cost:
            continue
        else: # cheapest[(r, c, d)] = cost, means alternative path
            pathto[(r, c, d)] |= path
    else:
        cheapest[(r, c, d)] = cost
        pathto[(r, c, d)] = path

    dr, dc = r + direc[d][0], c + direc[d][1]

    if matrix[dr][dc] != '#':
        heapq.heappush(minheap, (cost+1, dr, dc, d, path | {(r, c)}))
    heapq.heappush(minheap, (cost+1000, r, c, (d+1)%4, path | {(r, c)}))
    heapq.heappush(minheap, (cost+1000, r, c, (d-1)%4, path | {(r, c)}))

print(len(ans)+1)
