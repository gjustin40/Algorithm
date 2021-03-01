N = int(input())

count = N//5
remain = N%5

while remain <= N:
    if remain%3 == 0:
        count += remain//3
        break
        
    count -= 1
    remain += 5
    
if remain > N:
    print(-1)
    
else:
    print(count)
    
## 큰 수인 5로 나눠서 최소의 갯수를 구하고
## 3의 몫을 찾아가는 방식...
