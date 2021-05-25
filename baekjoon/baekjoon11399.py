import sys
N = int(sys.stdin.readline())
p_list = list(map(int, sys.stdin.readline().split()))
p_list = sorted(p_list)
p_cost = []

for i in range(N):
    if i == 0:
        p_cost.append(p_list[0])
    else:
        p_cost.append(p_cost[i-1] + p_list[i])
        
print(sum(p_cost))
