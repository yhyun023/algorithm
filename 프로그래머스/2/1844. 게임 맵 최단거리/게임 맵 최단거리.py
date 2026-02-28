from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[0]*m for _ in range(n)]
    dist[0][0] = 1
    
    q = deque()
    q.append((0, 0))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == m - 1:
            return dist[r][c]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if dist[nr][nc] != 0:
                continue
            if maps[nr][nc] == 0:
                continue
            
            q.append((nr, nc))
            dist[nr][nc] = dist[r][c] + 1
            
    return -1