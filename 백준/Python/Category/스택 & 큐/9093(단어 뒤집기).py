n = int(input())

for _ in range(n):
    arr = list(input().split())
    for i in arr:
        print(i[: :-1], end=" ")
    print()
