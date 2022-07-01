import sys
input = sys.stdin.readline

n,m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in tree:
        if i > mid:
            cnt += (i - mid)
    
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
