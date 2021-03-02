N = int(input())

count = 2
while N != 1:
    if N%count == 0:
        N = N/count
        print(count)
        
    elif N%count != 0:
        count += 1       
        
## 근데 시간이 너무 올래 걸림
## 다른 사람들 중 매우 짧은 사람도 있던데...우쨰한거지
