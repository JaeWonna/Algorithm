'''
시간초과를 해결하기 위해서는 import sys 사용을 생활화하자
리스트 안의 값의 빈도수에 대한 문제는 (Counter -> 딕셔너리) 과 (most_common -> 튜플의 리스트)을 활용하자
개념은 블로그에 정리
'''

import sys
from collections import Counter

numbers = []
for _ in range(int(sys.stdin.readline())):
	num = int(sys.stdin.readline())
	numbers.append(num)

numbers.sort()

cnt = Counter(numbers).most_common(2)

print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
if len(numbers) > 1:
	if cnt[0][1] == cnt[1][1]:
		print(cnt[1][0])
	else:
		print(cnt[0][0])
else:
	print(cnt[0][0])
print(max(numbers) - min(numbers))
