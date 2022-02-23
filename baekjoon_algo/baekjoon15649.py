#블랙잭 백트래킹 조합(중복x)

N, M = map(int, input().split())
li = []
visited = [False] * (N+1)
def recur(cur):
    
    if cur == M: #선택한 개수
        print(*li)
        return


    for i in range(1, N+1): # 1~N개 중에 M개를 중복없이 출력
        if visited[i]:
            continue
        
        li.append(i) #탐색하기위해 리스트에 넣어줌.
        visited[i] = True #방문처리해야 자기자신을 불러와 똑같은 애들로 검증가능.
        recur(cur+1)
        visited[i] = False
        li.pop() #탐색이 끝나면 빼줌. 1을 고정으로 넣은 경우의 수 다구하고 빼고 2를 넣고 ~ N까지 반복

recur(0)