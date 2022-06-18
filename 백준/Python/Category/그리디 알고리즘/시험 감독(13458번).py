n = int(input())
person = list(map(int, input().split()))
b,c = map(int, input().split())
cnt = n

for i in person:
    i -= b

    if i > 0:
        if i % c == 0:
            cnt += (i // c)
        else:
            cnt += (i // c) + 1

print(cnt)
