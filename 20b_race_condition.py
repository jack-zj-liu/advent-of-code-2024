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
            
sr, sc = find('S')
er, ec = find('E')

nocheattime = inf

def bfs(r, c):
    q = deque([(0, r, c)])
    dists = dict()

    direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        time, r, c = q.popleft()

        if (r, c) in dists:
            continue
        dists[(r, c)] = time

        for dr, dc in direc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                q.append((time+1, nr, nc))
    
    return dists

# use no cheating time from part a
nocheat = 9324

from_s, to_e = bfs(sr, sc), bfs(er, ec)

for i in range(1, n-1):
    for j in range(1, m-1):
        if (i, j) not in from_s:
            continue

        startdist = from_s[(i, j)]

        for dr in range(-20, 21):
            for dc in range(-20, 21):
                if abs(dr) + abs(dc) > 20:
                    continue

                nr, nc = i+dr, j+dc
                if not (0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#'):
                    continue
            
                if (nr, nc) not in to_e:
                    continue

                enddist = to_e[(nr, nc)]

                totaldist = startdist + abs(dr) + abs(dc) + enddist
                if nocheat - totaldist >= 100:
                    ans += 1

print(ans)
