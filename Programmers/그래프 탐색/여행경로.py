'''

print문 참고하면서 복습하기
비행기표 티켓 순서대로 가면서 스택을 쌓고 더 이상 갈곳이 없을때 방향을 틀면서 역주행으로
길을 잡았다
따라서 마지막에 비행기표 티켓 순서를 따라서 [::-1]을 해주어야 한다 


'''

from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        print(f"여기에요! {routes}\n\n")
        return routes

    # 스택을 사용한 DFS
    def dfs():
        stack = ["ICN"]
        path = []  # 가려고하는 경로를 저장하는 변수
        while len(stack) > 0:  # stack이 비어있을 때까지
            top = stack[-1]
            
            print(f"top의 값은 {top} 입니다!!!")
            print(f"연산 전의 stack의 값은 {stack} 이고요")
            print(f"연산 전의 path(정답><)의 값은 {path} 이고요")
            print(f"연산 전의 routes의 값은 {routes} 이에욥]\n")
            
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                print(f"top not in routes의 값은 {top not in routes}입니다")
                print(f"len(routes[top])의 값은 {len(routes[top])} 입니다")
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
            print(f"연산이 끝나고 난 후의 stack의 값은 {stack} 이고요")
            print(f"연산이 끝나고 난 후의 path(정답><)의 값은 {path} 이고요")
            print(f"연산이 끝나고 난 후의 routes의 값은 {routes} 이에욥]\n\n\n")

        print(f"stack의 값은 {stack} 입니다")
        print(f"path의 값은 {path} 입니다")
        return path[::-1]

    routes = init_graph()

    print(f"정렬하기전!! routes의 값은 {routes} 입니다")
    for r in routes:
        routes[r].sort()
    print(f"정렬 후!! routes의 값은 {routes} 입니다")

    answer = dfs()
    return answer

li = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(li))
