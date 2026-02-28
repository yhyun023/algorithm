from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
    n = len(tickets)
    graph = defaultdict(list)
    tickets.sort()
    for i, (a, b) in enumerate(tickets):
        graph[a].append((b, i))
    
    route = []
    used = [False] * n
    
    def findroute(cur):
        route.append(cur)
        if len(route) == n + 1:
            return route
        for nxt, idx in graph[cur]:
            if used[idx]:
                continue
            used[idx] = True
            if findroute(nxt):
                return route
            used[idx] = False
        route.pop()
        
    return findroute("ICN")