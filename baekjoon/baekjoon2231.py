N = int(input())

for i in range(1,N+1):
    num_sum = sum(list(map(int, str(i))))
    result = num_sum + i
    
    if result == N:
        print(i)
        break
    if i == N:
        print(0)
