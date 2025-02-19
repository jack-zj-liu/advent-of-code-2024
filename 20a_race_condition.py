from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = 0
grid = []

for line in stdin:
    grid.append(list(line.strip()))

n, m = len(grid), len(grid[0])

def find(char):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == char:
                return (i, j)
            
# get no cheating time
sr, sc = find('S')
er, ec = find('E')

nocheattime = inf

def get_time(grid):
    minheap = [(0, sr, sc)]
    seen = set()

    direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while minheap:
        time, r, c = heapq.heappop(minheap)

        if (r, c) == (er, ec):
            return time

        if (r, c) in seen:
            continue
        seen.add((r, c))

        for dr, dc in direc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                heapq.heappush(minheap, (time+1, nr, nc))
    
    return -1

nocheat = get_time(grid)
saves = Counter()

for i in range(1, n-1):
    print(i, ans)
    for j in range(1, m-1):
        if grid[i][j] == '#':
            grid[i][j] = '.'
            t = get_time(grid)
            saves[nocheat-t] += 1

            if nocheat-t >= 100:
                ans += 1

            grid[i][j] = '#'

print(nocheat, ans)
