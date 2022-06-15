from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                cnt += 1
    return cnt

m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1,x2):
            graph[i][j] = 1

res = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i,j))

print(len(res))
print(*sorted(res))
