from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    dist = [0] * (n + 1)
    
    q = deque()
    q.append(1)
    dist[1] = 1
    
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] != 0:
                continue
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
    print(dist)
    max_dist = max(dist)
    cnt = 0
    for a in dist:
        if a == max_dist:
            cnt += 1
    return cnt