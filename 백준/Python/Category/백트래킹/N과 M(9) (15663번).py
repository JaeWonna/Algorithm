from itertools import permutations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) #순서대로 나오게 정렬 먼저

output = []
for numbers in list(permutations(N_list, M)):
    output.append(numbers)
output = sorted(list(set(output))) #중복 제거 후 정렬 까지 한번에!

for numbers in output:
    for num in numbers:
        print(num, end=' ')
    print()
