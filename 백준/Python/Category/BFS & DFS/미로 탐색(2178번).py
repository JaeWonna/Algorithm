'''
2차원 리스트 -> 리스트 [세로인덱스] [가로인덱스]

'''

from collections import deque

def prt(lst,x,y):
    for i in range(x):
        for j in range(y):
            print(str(lst[i][j]).rjust(2), end=" ")
        print()
    print("\n\n")

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        print(f"현재 위치는 {x}, {y} 입니다!")

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: 
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        print(f"다음 목적지 queue : {queue}")
        prt(graph, n, m)
    return graph[n-1][m-1]

n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))
print("\n\n\n")


dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
print("\n\n")
