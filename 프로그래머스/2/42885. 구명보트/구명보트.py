def solution(people, limit):
    people.sort()
    n = len(people)
    l = 0
    r = n - 1
    ans = 0
    
    while r >= l:
        if people[l] + people[r] <= limit:
            ans += 1
            l += 1
            r -= 1
        else:
            ans += 1
            r -= 1
    return ans