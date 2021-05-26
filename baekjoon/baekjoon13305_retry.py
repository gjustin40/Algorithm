
N = int(input())
km_list = list(map(int, input().split()))
cost_list = list(map(int, input().split()))

result = 0
before_cost = cost_list[0]

for i in range(N-1):
    if before_cost > cost_list[i]:
        before_cost = cost_list[i]
    result += before_cost * km_list[i]
    
print(result)
