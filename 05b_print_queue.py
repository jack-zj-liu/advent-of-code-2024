from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
orders = defaultdict(set)

for line in stdin:
    if line == '\n':
        break

    a, b = line.split('|')
    orders[int(a)].add(int(b))

def sort_query(query):
    for i in range(len(query)):
        ok = True

        for j in range(i+1, len(query)):
            if query[j] not in orders[query[i]]:
                ok = False

        if ok:
            return [query[i]] + sort_query(query[0:i] + query[i+1:])
    
    return []

for line in stdin:
    query = line.split(',')
    query = list(map(int, query))
    

    sorted_query = sort_query(query)
    if sorted_query != query:
        ans += sorted_query[len(query)//2]

print(ans)
    