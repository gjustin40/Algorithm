
n = int(input())
day_list = []
pay_list = []
max_pay = [0]*(n+1)

for _ in range(n):
    d, p = input().split()
    day_list.append(int(d))
    pay_list.append(int(p))
    
for i in range(n-1, -1, -1):
    if i + day_list[i] > n:
        max_pay[i] = max_pay[i + 1]
        
    else:
        max_pay[i] = max(max_pay[i + 1], pay_list[i] + max_pay[i + day_list[i]])
        
print(max_pay[0])

## 너무 어려워서 참고를 많이 했다.
## 나중에 다시 꼭 풀어봐야하는 문제..
## dp 너무 어렵다 ㅠㅠ
