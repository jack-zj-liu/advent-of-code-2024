from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

SIDE = 71
NBYTES = 1024
n, m = SIDE, SIDE
matrix = [['.' for _ in range(m)] for _ in range(n)]
ans = 0
coords = []

for line in stdin:
    line = line.strip().split(',')
    line = list(map(int, line))
    x, y = line
    coords.append((y, x))

for i in range(NBYTES):
    r, c = coords[i]
    matrix[r][c] = '#'

minheap = [(0, 0, 0)]
direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
seen = set()

while minheap:
    cost, r, c = heapq.heappop(minheap)

    if (r, c) == (n-1, m-1):
        print(cost)
        break
    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in direc:
        dr += r
        dc += c
        if 0 <= dr < n and 0 <= dc < m and matrix[dr][dc] == '.':
            heapq.heappush(minheap, (cost+1, dr, dc))

    