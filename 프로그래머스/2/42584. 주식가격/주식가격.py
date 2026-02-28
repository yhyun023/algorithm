def solution(prices):
    n = len(prices)
    stack = []
    cur = 0
    answer = [0] * n
    for i in range(n):
        a = i
        while stack and stack[-1][0] > prices[i]:
            val, idx = stack.pop()
            answer[idx] = i - idx
        stack.append((prices[i], i))
    for i in range(n):
        if answer[i] == 0:
            answer[i] = n - 1 - i

    return answer