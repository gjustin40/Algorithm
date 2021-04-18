T = int(input())

for _ in range(T):
    N = int(input())
    dp_list = [0,1,1,1,2,2]
    
    for i in range(6, N+1):
        dp_list.append(dp_list[i-3] + dp_list[i-2])
        
    print(dp_list[N])
