T = int(input())
case_list = []

for _ in range(T):
    case_list.append(list(map(int, input().split())))
    

for case in case_list:
    H, W, N = case
    
    if N%H == 0:
        XX = N//H
        YY = H
                
    else:
        XX = N//H + 1
        YY = N%H
        
    print(f'{YY}{XX:02}')

## 새로운 표현법
## print 할때 빈 0넣는 방법 -> 위 코드 참고
