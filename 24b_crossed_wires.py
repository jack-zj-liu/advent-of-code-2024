from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = 0
vals, parents, operation, indegree, children = dict(), dict(), dict(), Counter(), defaultdict(list)
gates = dict()

for line in stdin:
    if line == '\n':
        break

    a, b = line.strip().split()
    vals[a[0:3]] = int(b)

eqns = []
XORs, ANDs, TMPs, RESs = set(), set(), set(), set()
carries = set(['nvd'])
paired = dict()

fails = set()

for line in stdin:
    a, op, b, _, c = line.strip().split()
    eqns.append((a, op, b, c))

for a, op, b, c in eqns:
    if c[0] == "z" and op != "XOR" and c != 'z45':
        fails.add(c)
    
    if op == 'XOR':
        if c[0] != 'z' and not ((a[0] == 'x' and b[0] == 'y') or (a[0] == 'y' and b[0] == 'x')):
            fails.add(c)
        for sa, sop, sb, sc in eqns:
            if (sa == c or sb == c) and sop == 'OR':
                fails.add(c)
                continue
    
    if op == 'AND' and a != 'x00' and b != 'x00':
        for sa, sop, sb, sc in eqns:
            if (sa == c or sb == c) and sop != 'OR':
                fails.add(c)
                continue

print(','.join(sorted(fails)))
