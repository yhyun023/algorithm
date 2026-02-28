def solution(s):
    answer = True
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')' and stack:
            stack.pop()
        elif ch == ')' and not stack:
            answer = False
            break
        else:
            print("error")
            break
    
    if stack:
        answer = False
    
    return answer