'''
문제 이해 잘하기, 문제 단어 장난 잘 구별하기
성적x 성적순위o

'''

import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    score = []
    cnt = 1

    n = int(input())
    for i in range(n):
        a,b = map(int, input().split())
        score.append([a,b])
    
    score.sort()
    Min = score[0][1]

    for i in range(1,n):
        if score[i][1] < Min:
            cnt += 1
            Min = score[i][1]

    print(cnt)
