def binary_search(array, target, start, end):
    if start > end:
        return 0
    middle = (start + end) // 2

    if array[middle] == target:
        return 1
    elif array[middle] < target:
        return binary_search(array, target, middle+1, end)
    else:
        return binary_search(array, target, start, middle-1)

n = int(input())
nlst = sorted(list(map(int, input().split())))
m = int(input())
mlst = list(map(int, input().split()))

for i in mlst:
    print(binary_search(nlst, i, 0, n-1))
       
