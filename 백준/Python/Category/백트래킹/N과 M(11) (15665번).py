n,m = map(int,input().split())
num = sorted(list(set(map(int,input().split()))))
s = []

def backtracking():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(len(num)):
        s.append(num[i])
        backtracking()
        s.pop()

backtracking()
