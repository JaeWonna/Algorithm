import sys, heapq

input = sys.stdin.readline

def solution(data):
    smallh = []
    bigh = []
    middle = data[0]
    result = [middle]
    for idx, val in enumerate(data[1:], 1):
        if val > middle:
            heapq.heappush(bigh, val)
        else:
            heapq.heappush(smallh, (-val, val))
        if idx % 2 == 0:
            if len(smallh) < len(bigh):
                heapq.heappush(smallh, (-middle, middle))
                middle = heapq.heappop(bigh)
            elif len(smallh) > len(bigh):
                heapq.heappush(bigh, middle)
                middle = heapq.heappop(smallh)[1]
            result.append(middle)
    print(len(result))

    for i in range(len(result)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(result[i], end=" ")
    print()


t = int(input().rstrip()) # 테스트 케이스 개수
for i in range(t):
    m = int(input().rstrip())
    data = []
    if m % 10 == 0:
        for _ in range(m//10):
            data.extend(list(map(int, input().rstrip().split(" "))))
    else:
        for _ in range(m//10+1):
            data.extend(list(map(int, input().rstrip().split(" "))))
    solution(data)
