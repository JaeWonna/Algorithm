n,k = map(int, input().split())
arr = [i for i in range(1,n+1)]
answer = []
idx = k-1

for _ in range(n):
    if idx < len(arr):
        answer.append(arr.pop(idx))
        idx += k-1
    elif idx >= len(arr):
        idx = idx % len(arr)
        answer.append(arr.pop(idx))
        idx += k-1

print("<", ', '.join(str(i) for i in answer), ">", sep='')
