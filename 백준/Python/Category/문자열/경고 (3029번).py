A = list(map(int, input().split(':')))
B = list(map(int, input().split(':')))

if A[2] > B[2]:
    S = 60+B[2]-A[2]
    A[1] += 1
else:
    S = B[2] - A[2]

if A[1] > B[1]:
    M = 60+B[1]-A[1]
    A[0] += 1
else:
    M = B[1] - A[1]

if A[0] > B[0]:
    H = 24+B[0]-A[0]
else:
    H = B[0]-A[0]

if A[0] == B[0] and A[1] == B[1] and A[2] == B[2]:
    H = 24
    M = 0
    S = 0

print("%02d:%02d:%02d" % (H,M,S))
