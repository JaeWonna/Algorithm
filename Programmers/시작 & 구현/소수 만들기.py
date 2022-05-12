from itertools import combinations 

def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : 
            return False 
    return True 

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))

    # print(combinations(nums, 3)) 를 하면 단순 주소값만 나오고 
    # print(list(combinations(nums, 3))) list형식으로 출력해야 [(a,b,c) .. ]이런식이 된다

    for i in A: 
        if check(i[0], i[1], i[2]): 
            answer += 1
    return answer

nums = list(map(int, input().split()))
print(solution(nums))
