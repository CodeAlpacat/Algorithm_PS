str_num = input()
flag = str_num[0]
arr = str_num[0]
for i in range(len(str_num)):
    if str_num[i] != flag:
        arr += str_num[i]
        flag = str_num[i]
cnt = 0
if len(arr) == 1:
    print(0)
else:
    save = arr[0:2]
    for i in range(0, len(arr), 2):
        if arr[i:i+2] == save:
            cnt += 1
    print(cnt)
