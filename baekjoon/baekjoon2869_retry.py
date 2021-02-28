import math

A,B,V = input().split()
A,B,V = int(A), int(B), int(V)

d = (V - B)/ (A - B)
print(math.ceil(d))

# 이거 달팽이문제.... while구문 안 쓰고 풀기
