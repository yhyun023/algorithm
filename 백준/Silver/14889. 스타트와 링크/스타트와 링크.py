
from itertools import combinations

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

total = 10**18
mem = n // 2
memlist = []

for i in range(n):
    memlist.append(i)

for c in combinations(memlist, mem):
    t1 = 0
    for a, b in combinations(set(c), 2):
        t1 += maps[a][b] + maps[b][a]
    t2 = 0
    for a, b in combinations(set(memlist) - set(c), 2):   
        t2 += maps[a][b] + maps[b][a]
    total = min(total, abs(t1 - t2))
print(total)