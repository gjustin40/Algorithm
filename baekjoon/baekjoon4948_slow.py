def is_prime(num):
    if num == 1:
        return False
    
    elif num == 2:
        return True
    
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
            
        return True
    
T = int(input())

for _ in range(T):
    n = int(input())
    n2 = int(n/2)
    a, b = n2, n2
    while True:
        if is_prime(n2):
            print(f'{n2} {n2}')
            break
            
        else:
            a += 1
            b -= 1
            if (is_prime(a) and is_prime(b)):
                print(f'{b} {a}')
                break              
