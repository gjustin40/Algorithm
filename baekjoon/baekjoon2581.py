
N = int(input())
M = int(input())

def is_prime(num):
    if num == 1:
        return False
    
    elif num == 2:
        return True
        
    else:
        for i in range(2, num):
            if num%i == 0:
                return False
            
        return True
    
prime_list = []
for num in range(N, M+1):
    if is_prime(num):
        prime_list.append(num)

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
    
else:
    print(-1)
    
## 소수 구하는 함수 한 번 배워놓으니
## 관련 문제는 솔솔 풀리는구나....
## 근데 애초에 왜 이런 함수를 생각해내지 못 했니 멍충아.....ㅠㅠ
