def solution(brown, yellow):
    answer = [] 
    for i in range(1, yellow+1):
        if yellow % i == 0 and yellow//i >= i:
            width = yellow // i
            height = i
            
            if (width + 2) * 2 + height * 2 == brown:
                answer = [width + 2, height + 2]
                break
                
    if yellow == 1:
        return [3, 3]
    return answer