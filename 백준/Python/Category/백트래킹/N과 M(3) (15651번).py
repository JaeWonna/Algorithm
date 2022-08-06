def backtracking():
    if len(s) == n:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1,m+1):
        s.append(i)
        backtracking()
        s.pop()

m,n = map(int, input().split())
s = []
backtracking()
