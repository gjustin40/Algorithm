T = int(input())
A, B, C = 0, 0, 0

A = T // 300
res = T % 300

B = res // 60
res = res % 60

C = res // 10
res = res % 10

if res == 0:
    print(A, B, C)
else:
    print(-1)
