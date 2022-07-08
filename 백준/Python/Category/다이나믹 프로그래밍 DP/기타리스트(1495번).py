import sys
input = sys.stdin.readline

n,s,m = map(int,input().split())

v = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            num1 = j + v[i]
            num2 = j - v[i]
            # 더한게 10보다 작으면 볼륨조절 가능
            if 0 <= num1 <= m:
                dp[i+1][num1] = 1
            # 뺀게 0보다 크면 볼륨조절가능
            if 0 <= num2 <= m:
                dp[i+1][num2] = 1
ans = -1
for i in range(m+1):
    #마지막 곡  n
    if dp[n][i] == 1:
        ans = i
print(ans)
