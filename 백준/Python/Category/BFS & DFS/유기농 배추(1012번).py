'''
문제의 포인트는 세로 가로를 헷갈리지 않는것
x,y대신 a,b사용한것
'''


from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

def bfs(graph, a,b):
    queue = deque()
    graph[a][b] = 0
    queue.append((a,b))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1
    
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a,b)
                cnt += 1
    print(cnt)
