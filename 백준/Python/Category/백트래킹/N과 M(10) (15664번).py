from itertools import combinations

n,m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = []

for i in list(combinations(lst, m)):
    result.append(i)

result = sorted(list(set(result)))

for res in result:
    for i in res:
        print(i, end=' ')
    print()
