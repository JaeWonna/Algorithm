n,m = map(int, input().split())
num = sorted(list(map(int, input().split())))
s = []

def backtracking(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n):
        s.append(num[i])
        backtracking(i)
        s.pop()

backtracking(0)
