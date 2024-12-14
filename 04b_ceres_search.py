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
    matrix.append(line.strip())

for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[0])-1):
        if matrix[i][j] == 'A':
            d1 = matrix[i-1][j-1] + matrix[i+1][j+1]
            d2 = matrix[i+1][j-1] + matrix[i-1][j+1]
            if (d1 == 'MS' or d1 == 'SM') and (d2 == 'MS' or d2 == 'SM'):
                ans += 1

print(ans)
    