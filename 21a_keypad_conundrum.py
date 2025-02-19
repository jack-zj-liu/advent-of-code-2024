from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = 0
codes = []

for line in stdin:
    codes.append(line.strip())

numpad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          ['_', '0', 'A']]

dirpad = [['_', '^', 'A'],
          ['<', 'v', '>']]

dir = {
    '^': (-1, 0),	
	'>': (0, 1),	
	'<': (0, -1),	
	'v': (1, 0),	
}

layers = 2
pads = []

for i in range(layers):
    pads.append(dirpad)
pads.append(numpad)

def get_paths(p, x1, y1, x2, y2):
    n, m = len(pads[p]), len(pads[p][0])
    ans = []
    def go(x, y, cur):
        if not (0 <= x < n and 0 <= y < m and pads[p][x][y] != '_'):
            return
        if (x, y) == (x2, y2):
            ans.append(cur)
        if len(cur) >= 5:
            return
        for s, d in dir.items():
            go(x+d[0], y+d[1], cur+s)
    go(x1, y1, '')
    return ans

def find(p, c):
    for i in range(len(pads[p])):
        for j in range(len(pads[p][0])):
            if pads[p][i][j] == c:
                return (i, j)


@lru_cache(maxsize=128, typed=False)
def min_dist(p, x1, y1, x2, y2):
    cur = inf

    for path in get_paths(p, x1, y1, x2, y2):
        if p == 0:
            cur = min(cur, len(path) + 1)
        else:
            route = 0
            path = 'A' + path + 'A'
            for i in range(len(path)-1):
                cx1, cy1 = find(p-1, path[i])
                cx2, cy2 = find(p-1, path[i+1])
                route += min_dist(p-1, cx1, cy1, cx2, cy2)
            cur = min(cur, route)

    return cur

for code in codes:
    path = 'A' + code
    cur = 0
    for i in range(len(path)-1):
        cx1, cy1 = find(layers, path[i])
        cx2, cy2 = find(layers, path[i+1])
        cur += min_dist(layers, cx1, cy1, cx2, cy2)
    
    print(int(code[0:3]), cur)
    ans += cur * int(code[0:3])

# print(get_paths(0, 0, 1, 1, 0))
# print(find(0, '^'))
print(ans)