from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

a, b, c = 0, 0, 0
ans = 0

for line in stdin:
    if line == '\n':
        break
    line = line.strip().split()
    if line[1][-2] == 'A':
        a = int(line[2])
    if line[1][-2] == 'B':
        b = int(line[2])
    if line[1][-2] == 'C':
        c = int(line[2])

program = []
for line in stdin:
    program = line.split()[1].split(',')
    program = list(map(int, program))

def getcombo(op):
    if 0 <= op <= 3:
        return op
    if op == 4:
        return a
    if op == 5:
        return b
    if op == 6:
        return c

outputs = []
i = 0
while i < len(program):
    p = program[i]
    op = program[i+1]
    combo = getcombo(op)
    
    if p == 0:
        a = a // 2**combo
        i += 2
    elif p == 1:
        b = b ^ op
        i += 2
    elif p == 2:
        b = combo%8
        i += 2
    elif p == 3:
        if a != 0:
            i = op
        else:
            i += 2
    elif p == 4:
        b = b ^ c
        i += 2
    elif p == 5:
        outputs.append(combo%8)
        i += 2
    elif p == 6:
        b = a // 2**combo
        i += 2
    elif p == 7:
        c = a // 2**combo
        i += 2

    
print(a, b, c)

outputs = list(map(str, outputs))
print(','.join(outputs))
