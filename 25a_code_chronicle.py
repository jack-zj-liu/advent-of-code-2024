from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
from functools import lru_cache
import heapq


ans = 0

inputs = []
curr = []

for line in stdin:
    if line == '\n':
        inputs.append(curr)
        curr = []
    else:
        curr.append(line.strip())

inputs.append(curr)

locks, keys = [], []

def get_lock_ht(input):
    ans = []
    for j in range(5):
        for i in range(7):
            if input[i][j] == '.':
                ans.append(i-1)
                break
    return ans

def get_key_ht(input):
    ans = []
    for j in range(5):
        for i in range(6, -1, -1):
            if input[i][j] == '.':
                ans.append(5-i)
                break
    return ans


for ip in inputs:
    if ip[0] == '#####':
        locks.append(get_lock_ht(ip))
    else:
        keys.append(get_key_ht(ip))

for lock in locks:
    for key in keys:
        ok = True
        for i in range(5):
            if lock[i] + key[i] > 5:
                ok = False
                break

        if ok:
            ans += 1

print(ans)
