def quick_sort(s, e):
    if s >= e: return
    # 파티션
    
    i, j = s, e
    while i < j:
        while i <= e and arr[s] >= arr[i]: #피봇과 i 비교 / 피봇과 같은 값이면? 왼쪽에 두자
            i += 1
        while arr[s] < arr[j]: #피봇과 j 비교
            j -= 1
        if i < j: #j가 피봇까지 쭉 가므로 i는 무조건 j보다 큰 시점이 오게됨.
            arr[i], arr[j] = arr[j], arr[i]
        #주의 사항: 경계 체크를 해줘야함. 


    #헤쳐모여 끝났으므로 arr[s]와 arr[j]를 교환
    arr[s], arr[j] = arr[j], arr[s]
    quick_sort(s, j - 1) #피봇 j 위치 전후
    quick_sort(j+1, e)

arr = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8, 4, 3]
N = len(arr)
quick_sort(0, N-1)

print(arr)