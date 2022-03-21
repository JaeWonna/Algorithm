'''
666을 포함하는 숫자중에서 몇 번째 숫자인가 하는 문제이다.

1. 666
2. 1666
3. 2666
4. 3666
5. 4666
6. 5666
7. 6660
8. 6661 ...

위와 같이 진행이 되기 때문에 six_n을 1씩 더해가는 while문을 만들어 666이 안에 들어있다면 cnt를 1 증가시키고,
cnt가 n과 같다면 six_n을 출력해준다.
'''


n = int(input())
cnt = 0
six_n = 666

while True:
    if "666" in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1
