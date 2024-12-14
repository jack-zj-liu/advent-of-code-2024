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

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        curr = 0
        if matrix[i][j:j+4] == 'XMAS' or matrix[i][j:j+4] == 'SAMX':
            curr += 1

        if i+3 < len(matrix):
            word = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
            if word == 'XMAS' or word == 'SAMX':
                curr += 1

        if i+3 < len(matrix) and j+3 < len(matrix[0]):
            word = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
            if word == 'XMAS' or word == 'SAMX':
                curr += 1

        if i-3 >= 0 and j+3 < len(matrix[0]):
            word = matrix[i][j] + matrix[i-1][j+1] + matrix[i-2][j+2] + matrix[i-3][j+3]
            if word == 'XMAS' or word == 'SAMX':
                curr += 1

        ans += curr

print(ans)
    