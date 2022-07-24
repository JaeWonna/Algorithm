import sys
input = sys.stdin.readline

n = int(input())
dx = [0,-1,0,1]
dy = [1,0,-1,0]

for _ in range(n):
    data = list(input().rstrip())
    dire = 0
    x,y = 0,0
    max_x, min_x, max_y, min_y = 0,0,0,0

    for i in data:
        if i == 'F':
            x += dx[dire]
            y += dy[dire]
        
        elif i == 'B':
            x -= dx[dire]
            y -= dy[dire]
        
        elif i == 'R':
            if dire == 0:
                dire = 3
            else:
                dire -= 1
        
        elif i == 'L':
            if dire == 3:
                dire = 0
            else:
                dire += 1
        
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    print(abs(max_x - min_x) * abs(max_y - min_y))

