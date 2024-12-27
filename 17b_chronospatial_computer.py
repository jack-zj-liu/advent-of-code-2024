from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

program = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]

def prog(a, b, c):
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

    return outputs

def dfs(a, proglen):
    if prog(a, 0, 0) == program: 
        print(a)
    if prog(a, 0, 0) == program[-proglen:] or proglen == 0:
        for n in range(8): 
            dfs(8*a+n, proglen+1)

dfs(0, 0)
