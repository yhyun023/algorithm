n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key = lambda x: (x[1], x[0]))

last = 0
cnt = 0
for start, end in times:
    if start >= last:
        last = end
        cnt += 1

print(cnt)