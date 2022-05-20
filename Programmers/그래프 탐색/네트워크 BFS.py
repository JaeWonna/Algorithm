# 해설포함

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
            print(f"BFS가 끝났고 answer은 {answer}입니다\n\n")
    return answer



def BFS(n, computers, com, visited):
    print(f"BFS가 시작되었고 n은 {n}이고 computers는 {computers}이고 com은 {com}이고 visited는 {visited} 입니다")
    visited[com] = True
    queue = []
    queue.append(com)
    print(f"while문 전 queue는 {queue} 입니다 그리고 len(queue)의 값은 {len(queue)} 입니다")
    while len(queue) != 0:
        com = queue.pop(0)
        print(f"com은 {com} 입니다")

        visited[com] = True
        
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                print(f"connect의 값은 {connect}이고 {computers}[{com}][{connect}] = {computers[com][connect]} 입니다")
                if visited[connect] == False:
                    queue.append(connect)

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
