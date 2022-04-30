'''
1. 입력시간 줄이기 sys
2. 이중리스트 이용시 미리 리스트 선언 후 append
3. 배열 요소 출력시 for 

'''


import sys
n = int(sys.stdin.readline())

so = []
for i in range(n):
	so.append(list(map(int, sys.stdin.readline().split())))

so.sort(key = lambda x : (x[1], x[0]))

for i in so:
	print(i[0], i[1])
