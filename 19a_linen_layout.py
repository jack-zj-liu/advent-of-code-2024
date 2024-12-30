from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq


ans = 0
patterns = []
towels = []

for line in stdin:
    if line == '\n':
        break
    patterns = line.strip().split(',')

for i in range(len(patterns)):
    patterns[i] = patterns[i].strip()

for line in stdin:
    towels.append(line.strip())

for t in towels:
    n = len(t)
    dp = [1] + [0] * (n)

    for i in range(n):
        if dp[i] == 0:
            continue

        for p in patterns:
            if t[i:i+len(p)] == p:
                dp[i+len(p)] = 1

    if dp[n] == 1:
        ans += 1

print(ans)
