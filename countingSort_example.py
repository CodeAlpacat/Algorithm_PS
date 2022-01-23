#카운팅 정렬
def counting_sorted(arr, K): #arr는 배열, K는 arr에 들어갈 수 있는 숫자들의 최대값이다. K는 arr의 요소들 중에 가장 큰 값 이상이어야만 한다.
    c = [0] * K # arr안에 포함될 수 있는 최대값 크기의 리스트 c를 생성하고 0을 할당한다.
    sorted_arr = [0] * len(arr) # 정렬된 arr를 저장하기위한 sorted_arr 리스트 생성.
    
    for i in arr: 
        c[i] += 1 # arr안의 값에 해당하는 c리스트의 인덱스에 해당 값의 개수를 할당. [0, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(1,K): #[0, 1, 2, 3, 4, 6, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9,....9]
        c[i] += c[i-1] #K크기의 배열이므로 K-1까지 c배열의 누적합을 구한다. 0~ K-1까지의 리스트이므로 없는 값은 0이 할당되어있다.
   
    for i in range(len(arr)): #sorted_arr[2] = 3, sorted_arr[5] = 5, sorted_arr[0] = 1 ...
        sorted_arr[c[arr[i]]-1] = arr[i] #입력받은 리스트 arr의 값을 순서대로 c를 기준으로 sorted_arr에 재배치한다.
        c[arr[i]] -= 1 # c 배열의 값을 1씩 줄여줌. 안 줄여준다면 중복을 제거해서 중복된 수의 자리가 0으로 채워져 정렬됨.

    return sorted_arr
        
arr = [3, 5, 1, 2, 9, 6, 4, 7, 5, 1, 1, 1]
print(counting_sorted(arr, 20))