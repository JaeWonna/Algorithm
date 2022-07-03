import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []
DP = [0]*(N+1)

for _ in range(N):
    time, price = map(int, input().split())
    T.append(time)
    P.append(price)

max_value = 0
for i in range(N):
    max_value = max(max_value, DP[i])

    if i + T[i] > N:
        continue
    DP[i+T[i]] = max(DP[i+T[i]], max_value + P[i])

print(max(DP))
