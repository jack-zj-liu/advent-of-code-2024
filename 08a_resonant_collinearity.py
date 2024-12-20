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
    x1 = p1[0] - (p2[0] - p1[0])
    y1 = p1[1] - (p2[1] - p1[1])
    x2 = p2[0] - (p1[0] - p2[0])
    y2 = p2[1] - (p1[1] - p2[1])

    if 0 <= x1 < m and 0 <= y1 < n:
        antinodes.add((x1, y1))
    if 0 <= x2 < m and 0 <= y2 < n:
        antinodes.add((x2, y2))

    return ans

for arr in locs.values():
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            cnt_antinode(arr[i], arr[j])

print(len(antinodes))

