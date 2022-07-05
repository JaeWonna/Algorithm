import sys
input = sys.stdin.readline

dp = [1]*10001

cnt = 0
for i in range(2,10001):
    if i % 2 == 0:
        cnt += 1
    dp[i] += cnt

for j in range(3,10001):
    dp[j] += dp[j-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
