import sys
input = sys.stdin.readline

n = int(input())
T,P = [],[]
d = [0]*(n+1)

for _ in range(n):
    time, price = map(int, input().split())
    T.append(time)
    P.append(price)

M = 0

for i in range(n):
    M = max(M, d[i])
    if i+T[i] > n:
        continue
    d[i+T[i]] = max(d[i+T[i]], M + P[i])

print(max(d))
