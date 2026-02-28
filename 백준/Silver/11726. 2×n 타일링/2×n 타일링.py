
n = int(input())

dp = [0] * (max(3, n + 1))

dp[0] = 0
dp[1] = 1
dp[2] = 2
if n < 3:
    print(dp[n])
    exit()
for i in range(3, n+1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])