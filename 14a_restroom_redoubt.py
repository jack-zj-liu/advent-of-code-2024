from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

n, m = 103, 101
TIME = 100
matrix = []
ans = 0

robots = []

for line in stdin:
    p, v = line.strip().split()

    p0, p1 = p.split(',')
    v0, v1 = v.split(',')

    p0 = int(p0[2:])
    p1 = int(p1)

    v0 = int(v0[2:])
    v1 = int(v1)

    robots.append((p0, p1, v0, v1))

def pos(p0, p1, v0, v1):
    x = (p0 + v0*TIME) % m
    y = (p1 + v1*TIME) % n
    return (x, y)

quadrants = [0, 0, 0, 0]

matrix = [[0 for _ in range(m)] for _ in range(n)]

for p0, p1, v0, v1 in robots:
    x, y = pos(p0, p1, v0, v1)
    matrix[y][x] += 1

    if x > m//2 and y > n//2:
        quadrants[3] += 1
    elif x > m//2 and y < n//2:
        quadrants[0] += 1
    elif x < m//2 and y > n//2:
        quadrants[2] += 1
    elif x < m//2 and y < n//2:
        quadrants[1] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
