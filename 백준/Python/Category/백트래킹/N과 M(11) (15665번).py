n,m = map(int,input().split())
num = sorted(list(set(map(int,input().split()))))
s = []

def backtracking(cnt):
    if cnt == m:
        print(*s)
        return
    
    cnt += 1

    for i in num:
        s.append(i)
        backtracking(cnt) 
        s.pop()

backtracking(0)
