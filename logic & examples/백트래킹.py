# 중복 을 허용한 n자리 m진수 / 중복을 전부 허용하는 순열
# 시간 복잡도 n^m
# 부분집합의 합과도 비슷함.
n, m = map(int,input().split())
arr = [0 for i in range(n)]
# 템플릿 약간 변형함.
def recur(cur): #cur = 종료 조건 / N = 자릿수/ M = 진수 / N자릿수 배열
    if cur == n:
        #종료전에 실행을 원하는 모든게 여기 들어감
        print(*arr)
        return

    for i in range(m):
        arr[cur] = i #i는 인덱스 번호나 다름 없음. arr2[i]를 입력넣어도댐.
        recur(cur+1) #cur + 1로 n까지

recur(0)


#2번 템플릿 /순열 중복제거
#시간복잡도 nPm

n = int(input())
arr = list(map(int, input().split()))
arr2 = [0 for i in range(n)]
visited = [False for i in range(n)]
def check():
    #내가 백트래킹이 끝나기 직전에 연산하고 싶은것!
    return
def recur(cur):
    if cur == n:
        #종료 전에 계산을 원하는 함수 check
        check()
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        arr2[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

#반복문을 충분히 쌓고 뭐할지가 if문 아래 들어감
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             #여기가 cur==n 바로 밑

#3번 템플릿 / 조합
#시간복잡도 nCm



#4번 템플릿 / 조합