N = int(input())
res = 1000 - N

result = 0
for coin in [500, 100, 50, 10, 5, 1]:
    count = res // coin
    res = res % coin
    result += count
    
print(result)
