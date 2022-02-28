#개미
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p_direction = 1
q_direction = 1

while t>0:
    p += p_direction
    q += q_direction

    if q == h or q == 0:
        q_direction = -q_direction
    if p == w or p == 0:
        p_direction = -p_direction
    t -= 1

print(p, q)


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())



if ((p+t) // w) % 2 == 0:
    x = (p+t) % w
else:
    x = w - (p+t) % w

if ((q+t) // h) % 2 == 0:
    y = (q+t) % h
else:
    y = h - (q+t) % h

print(x, y)