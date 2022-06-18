n = int(input())
L = list(map(int, input().split()))

L.sort(reverse = True)

cnt = 0
for i in L[1:]:
    cnt += L[0] + i
print(cnt)
