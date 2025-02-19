from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = 0
adj = defaultdict(set)
computers = set()

for line in stdin:
    l = line.strip()
    a, b = l[0:2], l[3:]
    adj[a].add(b)
    adj[b].add(a)
    computers.add(a)
    computers.add(b)

seen = set()
trips = []

for c in computers:
    for a in adj[c]:
        for b in adj[c]:
            if a not in seen and b not in seen and b in adj[a] and a < b:
                trips.append((a, b, c))

    seen.add(c)

for a, b, c, in trips:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        ans += 1

print(ans)