from itertools import combinations

n,s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1,n+1):
    comb = combinations(arr, i)
    for j in comb:
        if sum(j) == s:
            cnt += 1

print(cnt)
