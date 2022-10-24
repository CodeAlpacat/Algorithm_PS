from collections import deque 
def solution(queue1, queue2):
    answer = 0
    #그리디, 나머지는 시간초과 각
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    if (sum_q1 + sum_q2) % 2 == 1:
        return -1
    
    for i in range(3 * len(queue1)):
        if sum_q1 < sum_q2:
            sum_q1 += queue2[0]
            sum_q2 -= queue2[0]
            queue1.append(queue2.popleft())
        elif sum_q1 > sum_q2:
            sum_q1 -= queue1[0]
            sum_q2 += queue1[0]
            queue2.append(queue1.popleft())
        else:
            return answer
        answer += 1
            
    return -1