from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

matrix = []
ans = 0

for line in stdin:
    line = list(line.strip())
    line = list(map(int, line))
    matrix.append(line)


n, m = len(matrix), len(matrix[0])

cnt = [[set() for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        cnt[i][j] = set([(i, j)]) if matrix[i][j] == 9 else set()

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

for i in range(8, -1, -1):
    for r in range(n):
        for c in range(m):
            if matrix[r][c] != i:
                continue

            for dr, dc in dir:
                dr += r
                dc += c
                if 0 <= dr < n and 0 <= dc < m and matrix[dr][dc] == i+1:
                    cnt[r][c] = cnt[r][c] | cnt[dr][dc]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            ans += len(cnt[i][j])

print(ans)