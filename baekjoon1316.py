#그룹 단어 체커
# a~z를 전부 True로 놓고 문자열에서 찍힌 문자를 다른 문자로 바뀔 때, False로 바꿈.
# ex) abcda -> a에서 b로 바뀌니 a에 해당하는 index가 ord(a) - 97을 False로 바꿈.
# 만약 탐색 도중에 False인 문자가 다시 나오면 continue하고 count 추가 X
# 문자열 set과 list_groupNum의 False 수 +1이 같아야 그룹넘버임.
N = int(input())
count = 0
for _ in range(N):
    X = input()
    error = 0
    for i in range(len(X)-1):
         if X[i] != X[i+1]:
            new_X = X[i+1:]
            if new_X.count(X[i])>0:
                error +=1
                
    if error ==0:
        count +=1       
        


print(count)