# NQUEEN 풀이

# 우선 각 행마다 한명의 퀸만 존재할 수 있으니 가장 윗줄의 몇번째 위치에 퀸을 놓을건지, 두번째 줄의 몇번째 위치에 퀸을 놓을건지, ...를 이용해 하나의 배치를 수열 하나로 표현 가능합니다.(2013이라면 가장 윗줄은 왼쪽에서 세번째, 위에서 두번째 줄은 가장 왼쪽, 세번째 줄은 왼쪽에서 두번째, 맨 아랫줄은 가장 오른쪽 열에 퀸을 놓은걸 의미합니다.)
# 각 열마다도 한명의 퀸만 존재할 수 있으니 visited를 이용해 각 열에 퀸이 있는지 여부를 저장할 수 있습니다.
# 생각해보면 각 대각선마다도 한명의 퀸만 존재할 수 있습니다. 왼쪽아래에서 오른쪽위로 가는 대각선을 생각할 때(/모양) 같은 대각선에 포함된 칸들은 행의 번호와 열의 번호의 합이 같습니다. 예를들어 (1, 3), (2, 2), (3, 1)은 같은 대각선에 속합니다. 이 합이 그 대각선의 인덱스라고 생각하고 방문처리 합니다.
# 반대쪽 대각선(\모양)의 경우 같은 대각선에 포함된 칸들은 행의 번호 - 열의 번호 값이 같습니다. 이걸로 방문처리 해줍니다.
# 위 세 방문처리가 모두 겹치지 않는 칸들에만 퀸을 놓으면서 끝까지 도착한다면 정답입니다.

n = int(input())
visited = [False for i in range(n)]
visited2 = [False for i in range(3*n)]
visited3 = [False for i in range(3*n)]

answer = 0

def recur(cur):
    global answer

    if cur == n:
        answer += 1
        return

    for i in range(n):
        if visited[i] or visited2[cur + i] or visited3[cur - i + n]:
            continue

        visited[i] = True
        visited2[cur + i] = True
        visited3[cur - i + n] = True
        recur(cur + 1)
        visited[i] = False
        visited2[cur + i] = False
        visited3[cur - i + n] = False

recur(0)

print(answer)