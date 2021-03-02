
N = int(input())
num_list = list(map(int, input().split()))

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

count = 0
for num in num_list:
    if is_prime(num):
        count += 1

print(count)

## 하... 진짜 개 멍청하다
## 이 길은 나의 길이 아닌가....
