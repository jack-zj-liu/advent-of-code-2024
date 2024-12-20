from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
matrix = []

for line in stdin:
    line = line.strip()
    matrix.append(line)

locs = defaultdict(list)

n, m = len(matrix), len(matrix[0])

for i in range(n):
    for j in range(m):
        if matrix[i][j] != '.':
            locs[matrix[i][j]].append((i, j))

antinodes = set()

def cnt_antinode(p1, p2):
    xdiff, ydiff = p2[0] - p1[0], p2[1] - p1[1]

    x, y = p1
    while 0 <= x < m and 0 <= y < n:
        antinodes.add((x, y))
        x += xdiff
        y += ydiff

    x, y = p1
    while 0 <= x < m and 0 <= y < n:
        antinodes.add((x, y))
        x -= xdiff
        y -= ydiff

for arr in locs.values():
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            cnt_antinode(arr[i], arr[j])

print(len(antinodes))

