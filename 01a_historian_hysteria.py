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

l1.sort()
l2.sort()
l3 = [abs(l1[i]-l2[i]) for i in range(len(l1))]

print(sum(l3))