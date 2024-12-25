from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

n, m = 103, 101
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

def pos(p0, p1, v0, v1, t):
    x = (p0 + v0*t) % m
    y = (p1 + v1*t) % n
    return (x, y)

for t in range(0, 10000):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    ok = True

    for p0, p1, v0, v1 in robots:
        x, y = pos(p0, p1, v0, v1, t)
        if matrix[y][x] > 0:
            ok = False
            break
        matrix[y][x] += 1
    
    if ok:
        print(t)
        break
