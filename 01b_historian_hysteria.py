from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

l1, l2 = [], []

for line in stdin:
    n1, n2 = line.split()
    l1.append(int(n1))
    l2.append(int(n2))

l2 = Counter(l2)
l3 = [x * l2[x] for x in l1]

print(sum(l3))