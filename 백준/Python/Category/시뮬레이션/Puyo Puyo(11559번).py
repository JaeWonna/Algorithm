import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
Pyo = ['R','G','B','P','Y']
count = [0,0,0,0,0]
ans = 0

# 해야하는것 : 동서남북으로 4개 이상일떄, 없애고 점으로 만들기

def bfs(a,b,graph): # 몇 연쇄인지 변수에 저장해서 return
    global ans # 정답
    global count # 각 알파벳 몇개인지 세기
    queue = deque()
    queue.append((a,b))

    if graph[a][b] == 'R':
        count[0] += 1
        alpha = 'R'
        idx = 0
    elif graph[a][b] == 'G':
        count[1] += 1
        alpha = 'G'
        idx = 1
    elif graph[a][b] == 'B':
        count[2] += 1
        alpha = 'B'
        idx = 2
    elif graph[a][b] == 'P':
        count[3] += 1
        alpha = 'P'
        idx = 3
    elif graph[a][b] == 'Y':
        count[4] += 1
        alpha = 'Y'
        idx = 4

    graph[a][b] = '.'

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == alpha:
                queue.append((nx,ny))
                count[idx] += 1
                graph[nx][ny] = '.'
    
    if count[idx] >= 4:
        ans += 1
        # 그래프 내리기

    # 그래프 확인
    for i in range(12):
        for j in range(6):
            print(graph[i][j], end="")
        print()
    print("\n\n\n")

graph = []

for _ in range(12):
    graph.append(list(input().rstrip()))
print("\n\n")

for x in range(12):
    for y in range(6):
        if graph[x][y] in Pyo:
            bfs(x,y,graph)

print(ans)
