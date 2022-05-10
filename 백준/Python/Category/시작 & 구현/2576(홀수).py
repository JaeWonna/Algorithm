import sys
input = sys.stdin.readline

a = []
for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        a.append(num)

if a:
    print(sum(a))
    print(min(a))
else:
    print(-1)
