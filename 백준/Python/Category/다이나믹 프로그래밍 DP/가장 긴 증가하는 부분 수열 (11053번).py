n = int(input())
a = list(map(int, input().split()))
d = [1]*n

for i in range(n):
  for j in range(i):
    if a[j] < a[i]:
      d[i] = max(d[i], d[j]+1)

print(max(d))
