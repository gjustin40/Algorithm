def get_prime(M, N):
    
    prime_list = [True]*(N+1)
    max_prime = int(N**0.5) + 1 
    primes = []
    for i in range(2, max_prime+1):
        if prime_list[i]:
            for j in range(i+i, N+1, i):
                prime_list[j] = False
    for a in range(M, N+1):
        if prime_list[a]:
            primes.append(a)
            
    return primes
            
while True:
    n = int(input())
    if n == 0:
        break
    n2 = n*2
            
    if n == 1:
        print(len(get_prime(2, 3)) -1)
    else:
        print(len(get_prime(n+1, n2)))
        
## 그 수학자가 쓴 수소찾기 공식 이용
