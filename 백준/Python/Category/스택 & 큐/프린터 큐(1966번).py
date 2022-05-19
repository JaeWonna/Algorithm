def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

n = int(input())

for _ in range(n):
    num, index = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, index))
