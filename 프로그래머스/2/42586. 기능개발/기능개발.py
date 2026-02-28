def solution(progresses, speeds):
    answer = []
    l = 0
    for k in range(100):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[l] >= 100:
            cnt = 1
            l += 1
            if l >= len(progresses):
                answer.append(cnt)
                break
            while progresses[l] >= 100:
                l += 1
                cnt += 1
                if l >= len(progresses):
                    break
            answer.append(cnt)
        if l >= len(progresses):
            break
    
        
    return answer