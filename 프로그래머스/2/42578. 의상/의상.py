def solution(clothes):
    d = {}
    for a, b in clothes:
        d[b] = d.get(b, 0) + 1
    
    ans = 1
    for v in d.values():
        ans *= (v + 1)
    ans -= 1
    return ans