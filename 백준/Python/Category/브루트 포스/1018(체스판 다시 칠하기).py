'''
N*M 보드를 map() 함수를 이용하여 띄어쓰기로 구분하여 입력 받는다.

원래의 판을 저장하기 위한 리스트 original과 

바뀐 채스판의 갯수를 저장하기 위한 리스트 count를 정의한다.

N(행)의 갯수만큼 원래의 판을 입력 받는다.

original이 리스트 이므로 append(input())을 이용하여 리스트에 추가 해준다.
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
