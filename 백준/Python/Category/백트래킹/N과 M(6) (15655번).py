n,m = map(int, input().split())
num = sorted(list(map(int, input().split())))
s = []

def backtracking(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n):
        if num[i] not in s:
            s.append(num[i])
            backtracking(i+1)
            s.pop()

backtracking(0)
