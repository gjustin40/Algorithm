import math as m

M, N = map(int, input().split())
def get_prime(M, N):
    
    prime_list = [True]*(N+1)
    max_prime = int(m.sqrt(N)) + 1 

    for i in range(2, max_prime+1):
        if prime_list[i]:
            for j in range(i+i, N+1, i):
                prime_list[j] = False
    for a in range(M, N+1):
        if prime_list[a]:
            print(a)

if M == 1:
    get_prime(2, N)
else:
    get_prime(M, N)
    
## 에라토스테스의 체 방법을 사용하니 완전 빠르다...
## 수학자들은 천재임
