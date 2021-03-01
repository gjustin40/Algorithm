N = int(input())
is_exist = []

div3 = N//3 + 1
div5 = N//5 + 1

for d3 in range(div3):
    for d5 in range(div5):
        
        result = 3*d3 + 5*d5
        
        if result == N:
            is_exist.append(d3+d5)
        
if is_exist:
    print(min(is_exist))
else:
    print(-1)
    
## 내가 푼 방식....시간이 너무 오래 걸림
## 하나씩 다 뽑아서 하는거니까 오래걸리지....
