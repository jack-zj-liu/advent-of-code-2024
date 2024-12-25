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
            x = int(arr[1][2:-1])
            y = int(arr[2][2:])
        game.append((x, y))

games.append(game)

def calc(a, b, prize):
    mincost = inf

    for i in range(0, 101):
        x, y = a[0] * i, a[1] * i
        remx, remy = prize[0]-x, prize[1]-y

        if remx%b[0] == 0 and remy%b[1] == 0 and remx//b[0] == remy//b[1]:
            mincost = min(mincost, 3*i + remx//b[0])

    return mincost if mincost < inf else -1

for game in games:
    cost = calc(game[0], game[1], game[2])
    if cost != -1:
        ans += cost

print(ans)
