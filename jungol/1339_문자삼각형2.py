n=int(input())
while n%2==0:
    print("INPUT ERROR")
    n=int(input())

a=0
b=((n+1)//2)-1
for i in range(n):
    c=b*b
    for j in range(a+1):
        print(chr(65+(c+i)%26),end=' ')
        c=c-(n-(j*2)-1)
    if i<(n//2):
        a += 1
    else:
        a-=1
    print()