#K 번째 작은 수
#counting sort 연습 모든 케이스가 정수인 경우. 1<= N <= 1000
T = int(input())

def cntSort(x):
    list_cnt = [0 for _ in range(1001)] # 각 값들의 개수를 저장해줄 공간. 자료의 최대값만큼의 배열 생성.
    list_x_sum =[0 for _ in range(len(x))] #실제 정렬을 위한 누적합 배열
    
    for i in x:
        list_cnt[i] += 1
    
    for i in range(1, len(list_cnt)): #누적합
        list_cnt[i] += list_cnt[i-1]
    
    for i in range(len(x)):
        list_x_sum[list_cnt[x[i]] -1] = x[i] #입력받은 리스트 x의 값을 마지막 배열에 재배치.
        list_cnt[x[i]] -= 1 # 중복값을 바로 앞 인덱스에 할당.
    
    return list_x_sum
        


for i in range(T):
    N, K = map(int, input().split())
    list_num = list(set(map(int, input().split())))
    sorted_list_num = cntSort(list_num)
    print(f'#{i+1}', sorted_list_num[K-1])