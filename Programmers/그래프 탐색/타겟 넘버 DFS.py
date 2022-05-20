def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: 
            return 0
    else:
        answer += DFS(numbers, target, depth+1)
        print(f"answer의 값은 {answer}이고 depth+1의 값은 {depth+1}이다 그리고 DFS(numbers, target, depth+1)의 값은 {DFS(numbers, target, depth+1)} 입니다!")
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        print(f"answer의 값은 {answer}이고 depth+1의 값은 {depth+1}이다 그리고 DFS(numbers, target, depth+1)의 값은 {DFS(numbers, target, depth+1)} 입니다!")
        return answer

numbers = [1,1]
target = 0
print(solution(numbers, target))
