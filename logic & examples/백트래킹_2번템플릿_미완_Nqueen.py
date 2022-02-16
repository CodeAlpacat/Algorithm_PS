# 9663. N - queen (웰노운 문제, 잘알려진 문제라 티어가 낮게나온다.)
# N by N 의 상태를 하나의 수열로 표현할 수 있다.
# 0 1 2 3
# 0 1 3 2
# 0 2 1 3
# 0 2 3 1
# ....
# 3 2 1 0

# 2번 템플릿(중복되지 않는 뽑기)

n = int(input())
arr = [0 for i in range(n)]
visited = [False for i in range(n)]

def check(cur):
	# 대각선인지 아닌지 구분하는코드를 필요로함
    # 나중에 올려주신대용
    # 이부분 완성해야됨
    return True

def recur(cur):
    if check(cur):
        return
    
    
    if cur == n:
        return
    
    for i in range(n):
        if visited[i]:
            continue
		
        arr[cur] = i
        visited[i] = True
        recur(cur+1)
        visited[i] = False
