from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count


n = int(input())
graph = []
cnt = []

for i in range(n):
    graph.append(list(map(int, input())))

for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            cnt.append(bfs(a,b))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
