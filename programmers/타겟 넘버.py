def solution(numbers, target):
    global ans
    #조합 => 1을 고르는 경우 -1을 고르는 경우 합이 target이 되는 경우 ans += 1
    def recur(cur, total):
        global ans
        
        if cur > len(numbers):
            return
        
        if cur == len(numbers):
            if total == target:
                ans += 1
            return
        
        recur(cur + 1, total + numbers[cur])
        recur(cur + 1, total - numbers[cur])
        
    ans = 0
    recur(0, 0)
    
    return ans