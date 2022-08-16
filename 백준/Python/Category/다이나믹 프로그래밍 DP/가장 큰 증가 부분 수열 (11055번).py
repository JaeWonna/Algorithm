n = int(input())
A = list(map(int, input().split()))
d = [x for x in A]

for i in range(n):
  for j in range(i):
    if A[j] < A[i]:
      d[i] = max(d[i], d[j]+A[i])

print(max(d))
