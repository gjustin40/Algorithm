prime_list = [True] * 100001
prime_list[1] = False

for i in range(2, 100):
    for j in range(2*i, 10001, i):
        prime_list[j] = False
        
T = int(input())
for i in range(T):
    n = int(input())
    n2 = int(n/2)
    for j in range(n2, 1, -1):
        if (prime_list[j] and prime_list[n-j]):
            print(j, n-j)
            break
