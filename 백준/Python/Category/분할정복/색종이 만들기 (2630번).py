def makepaper(x,y,n):
    global wCount, bCount
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                makepaper(x,y,n//2)
                makepaper(x,y+n//2, n//2)
                makepaper(x+n//2, y, n//2)
                makepaper(x+n//2, y+n//2, n//2)
                return
    
    if color == 0:
        wCount += 1
    else:
        bCount += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
wCount, bCount = 0,0

makepaper(0,0,n)
print(wCount)
print(bCount)
