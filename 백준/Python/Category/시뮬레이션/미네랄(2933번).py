''' 수정중!! '''

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    v = [[0]*c for _ in range(r)]
    queue.append((x,y))
    v[x][y] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] != '.' and v[nx][ny] == 0:
                    queue.append((nx,ny))
                    v[nx][ny] = 1

def down(): # 막 하면 안된다 모양 유지시키면서 내려와야 한다
    for i in range(r-2,-1,-1):
        for j in range(c):
            if a[i][j] != '.' and a[i+1][j] == '.':
                for k in range(i+1,r): 
                    if k == r-1 and a[k][j] == '.':
                        a[k][j] = a[i][j]
                    elif a[k][j] != '.':
                        a[k-1][j] = a[i][j]
                        break
                a[i][j] = '.'


r,c = map(int, input().split()) # r은 높이
a = [list(input().rstrip()) for _ in range(r)]
n = int(input()) # 막대 던진 횟수
h = list(map(int, input().split()))
flag = 1
before = flag

for i in range(n):
    if i % 2 == 0:
        for j in range(c):
            if a[r-h[i]][j] != '.':
                a[r-h[i]][j] = '.'
                break
    else:
        for j in range(c-1,-1,-1):
            if a[r-h[i]][j] != '.':
                a[r-h[i]][j] = '.'
                break

    for i in range(r):
        for j in range(c):
            if a[i][j] != '.':
                bfs(i,j)
    
    # down()은 언제? 모양 유지시키면서 내려오는건 언제? 


# 마지막 결과값
for i in range(r):
    for j in range(c):
        print(a[i][j], end='')
    print()


# Question) 그래프를 건들 수 없다면 모든 인덱스마다 시행해야 하는가? 무조건?
