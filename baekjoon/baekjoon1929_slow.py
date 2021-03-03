
import math as m
M, N = map(int, input().split())

def is_prime(n):
    if n == 1:
        return False
    
    elif n == 2:
        return True
    
    else:
        for i in range(2, int(m.sqrt(n))+1):
            if n%i == 0:
                return False
            
        return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)
        
## 기존 방법에서 반복문 n의 값을 루트값으로 변경해준 것
## 졸라 느림.....
