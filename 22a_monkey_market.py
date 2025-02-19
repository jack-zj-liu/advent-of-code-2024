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


for n in starts:
    for i in range(2000):
        n = get_next(n)
    ans += n

print(ans)

