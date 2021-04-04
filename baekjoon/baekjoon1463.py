
N = int(input())
dp_list = [0, 0, 1, 1] # 각각 n이 0 1 2 3일 때 최소의 수

for i in range(4, N+1):
    
    dp_list.append(dp_list[i-1]+1)
    
    if i % 2 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i//2] + 1)
        
    if i % 3 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i//3] + 1)
        
print(dp_list[N])
