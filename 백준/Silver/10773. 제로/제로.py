
k = int(input())
s = []
for _ in range(k):
    a = int(input())
    if a == 0:
        s.pop()
    else:
        s.append(a)
print(sum(s))