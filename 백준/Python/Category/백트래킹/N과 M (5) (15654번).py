n,m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []

def backtracking():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in num:
        if i not in s:
            s.append(i)
            backtracking()
            s.pop()

backtracking()
