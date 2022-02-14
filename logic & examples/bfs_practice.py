from collections import deque


def bfs(graph, start, visited):
    #큐 구현에 적합한 deque 사용
    queue = deque([start]) # 현재 노드 큐에 삽입(방문)

    visited[start] = True #큐에 들어간 후 방문 처리

    while queue:
        #큐에서 원소 출력
        v = queue.popleft()
        print(v, end =' ')
        #아직 방문하지 않은 원소들 queue에 삽입하고 방문 -> 직접 연결되지 않은 노드들까지 모두 방문하기 위함.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
#각 노드를 False로 방문하지 않았음을 표시
visited = [False] * 9

bfs(graph, 1, visited)