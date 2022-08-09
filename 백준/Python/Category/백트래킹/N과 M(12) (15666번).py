n,m = map(int, input().split())
num = sorted(list(set(map(int, input().split()))))
s = []

def backtracking(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start,len(num)):
        s.append(num[i])
        backtracking(i)
        s.pop()

backtracking(0)
