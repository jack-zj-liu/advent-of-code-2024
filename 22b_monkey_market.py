from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


MOD = 16777216
ans = 0
starts = []

for line in stdin:
    starts.append(int(line.strip()))


def get_next(curr):
    curr = curr ^ (curr*64)
    curr %= MOD

    curr = curr ^ (curr//32)
    curr %= MOD

    curr = curr ^ (curr*2048)
    curr %= MOD

    return curr

cntr = Counter()

for n in starts:
    streak = []
    seen = set()
    for i in range(2000):
        new_n = get_next(n)
        streak.append(new_n%10-n%10)
        n = new_n
    
        curr = tuple(streak[-4:])
        if curr in seen:
            continue
        seen.add(curr)
        cntr[curr] += new_n%10


for a in range(-9, 10):
    for b in range(-9, 10):
        for c in range(-9, 10):
            for d in range(-9, 10):
                ans = max(ans, cntr[(a, b, c, d)])

print(ans)
