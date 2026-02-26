def solution(order):
    n = len(order)
    sub = []
    cnt = 0
    idx = 0
    for i in range(1, n + 1):
        sub.append(i)
        
        while sub and sub[-1] == order[idx]:
            cnt += 1
            idx += 1
            sub.pop()
        
    return cnt