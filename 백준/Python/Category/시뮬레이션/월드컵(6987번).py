import sys
input = sys.stdin.readline
from itertools import combinations as cb

def solution(round):
    global ans
    if round == 15:
        ans = 1
        for sub in res:
            if sub.count(0) != 3:
                ans = 0
                break
        return
    
    t1,t2 = game[round]
    for x,y in ((0,2),(1,1),(2,0)):
        if res[t1][x] > 0 and res[t2][y] > 0:
            res[t1][x] -= 1
            res[t2][y] -= 1
            solution(round+1)
            res[t1][x] += 1
            res[t2][y] += 1

answer = []
game = list(cb(range(6), 2))

for _ in range(4):
    data = list(map(int, input().split()))
    res = [data[i*3:(i+1)*3] for i in range(6)]
    ans = 0
    solution(0)
    answer.append(ans)

print(*answer)
