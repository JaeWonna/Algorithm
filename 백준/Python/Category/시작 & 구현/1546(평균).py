n = int(input())
a = list(map(int, input().split()))
a_max = max(a)

for i in range(n):
    a[i] = (a[i]/a_max) * 100
print(sum(a)/n)
