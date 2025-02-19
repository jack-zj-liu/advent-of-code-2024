from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = []
adj = defaultdict(list)
computers = set()

for line in stdin:
    l = line.strip()
    a, b = l[0:2], l[3:]
    adj[a].append(b)
    adj[b].append(a)
    computers.add(a)
    computers.add(b)

'''
all adjacency lists have len 13

so the maximum clique size is 14. We tried 14 it doesnt work, so we try 13, which does :DD
'''

for c in computers:
    for i in range(len(adj[c])):
        arr = adj[c][0:i] + adj[c][i+1:]

        ok = True
        for a in arr:
            for b in arr:
                if a not in adj[b] and a != b: 
                    ok = False
                    break

        if ok:
            ans = sorted(arr + [c])
            break

'''
this function is able to find cliques of size 12, then times out :OO
so the max clique must be either size 12, 13 or 14
'''
def find(curr):
    if len(curr) > ans[-1]:
        ans.append(len(curr))
        print(ans)
    for c in computers:
        if curr.issubset(adj[c]):
            find(curr | set([c]))

print(','.join(ans))
