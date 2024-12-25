from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

games = []
game = []
ans = 0
INCREASE = 10000000000000
# INCREASE = 0

for line in stdin:
    if line == '\n':
        games.append(game)
        game = []
    else:
        arr = line.strip().split()
        x, y = 0, 0
        if line[0] == 'B':
            x = int(arr[2][2:-1])
            y = int(arr[3][2:])
        else:
            x = int(arr[1][2:-1]) + INCREASE
            y = int(arr[2][2:]) + INCREASE
        game.append((x, y))

games.append(game)

def calc(a, b, prize):
    m = lcm(a[0], a[1])

    a0, b0, p0 = a[0] * m//a[0], b[0] * m//a[0], prize[0] * m//a[0]
    a1, b1, p1 = a[1] * m//a[1], b[1] * m//a[1], prize[1] * m//a[1]

    nb = b0-b1
    nprize = p0-p1
    if nprize%nb != 0:
        return -1
    
    y = nprize//nb

    if (p0-b0*y)%a0 != 0:
        return -1 
    
    x = (p0-b0*y) // a0

    return 3*x + y

for game in games:
    cost = calc(game[0], game[1], game[2])
    if cost != -1:
        ans += cost

print(ans)
