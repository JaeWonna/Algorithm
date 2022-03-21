'''
문제의 핵심은 두 가지 경우의 수에 대해서 생각을 해야 한다는 것이다
'W'로 시작할 때의 index1과
'B'로 시작할 때의 index2에 대해서
N-7, M-7이라는 범위한정과 a+8, b+8이라는 각각의 체스판 안에서의 경우의 수를 생각하면 된다

''' 



N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
