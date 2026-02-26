from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    food = []
    
    q = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            cnt = 0
            if maps[i][j] != "X" and not visited[i][j]:
                q.append((int(i), int(j)))
                cnt = int(maps[i][j])
                visited[i][j] = True
            while q:
                r, c = q.popleft()
                
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if visited[nr][nc]:
                        continue
                    if maps[nr][nc] == "X":
                        continue
                    
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += int(maps[nr][nc])
            if cnt != 0:
                food.append(cnt)
    if len(food) == 0:
        food.append(-1)
    food.sort()
    return food