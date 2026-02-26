from collections import deque

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    l1 = len(queue1)
    l2 = len(queue2)
    if total%2 == 1:
        return -1
    target = total // 2
    
    q1 = deque()
    q2 = deque()
    for a in queue1:
        q1.append(a)
    for b in queue2:
        q2.append(b)
    
    s1 = sum(q1)
    s2 = sum(q2)
    cnt = 0
    while s1 != target:
        if s1 > s2:
            n = q1.popleft()
            q2.append(n)
            s1 -= n
            s2 += n
        else:
            n = q2.popleft()
            q1.append(n)
            s1 += n
            s2 -= n
        cnt += 1
        if cnt > (l1 + l2) * 4:
            cnt = -1
            break
    
    return cnt