
N, K = map(int, input().split())
coin_list = []
for _ in range(N):
    coin_list.append(int(input()))
    
count = 0
count_sum = 0
for coin in reversed(coin_list):
    if K // coin >= 1:
        count = K // coin
        K -= count * coin # 나머지로 해도 됨 >> K = K % coin
        
        count_sum += count # 위를 나머지로 하면 바로 count_sum하면 됨 >> count += K // coin
        
print(count_sum)
