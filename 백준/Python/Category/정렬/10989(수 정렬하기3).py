'''
< 시간초과를 피하려면 어떻게 해야 하는가 >

import sys
sys.stdin.readline()을 이용한다

리스트의 크기를 미리 할당해놓는다 -> 이 문제에서는 0으로 초기화했다
인덱스의 값을 이용할거면 상황에 따라서 +1을 할 수도 있다 -> 값에 범위에 유의하기
크기가 10000 일 경우 [0 ~ 9999] 이지만
크기가 10001 일 경우 [0 ~ 10000] 이다

이 문제에서는 모든 값을 0으로 초기화한후 이용하려는 인덱스의 값에 +1씩 더해주었다


< for문 >

보통은 for i in range()이거나 for a in list이지만
i나 a를 사용하지 않는 인덱스나 리스트의 값의 사용이 아니라면
for _ in range()와 같이 뜻을 확실히 할 수도 있다

'''

import sys
n = int(sys.stdin.readline())
data = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    data[num] += 1

for i in range(10001):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)
