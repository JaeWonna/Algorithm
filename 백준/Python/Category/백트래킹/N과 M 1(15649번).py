def backtracking(idx):
    if idx == m:
        print(' '.join(map(str, s)))
        return 0

    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            backtracking(idx+1)
            s.pop()

n,m = map(int, input().split())
s = []
backtracking(0)    
