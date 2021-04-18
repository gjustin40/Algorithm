N = int(input())
paint_cost_list = [[0,0,0]]
dp_list = [0]

for _ in range(N):
    paint_cost_list.append(list(map(int, input().split())))
    
for i in range(1, len(paint_cost_list)):
    paint_cost_list[i][0] = min(paint_cost_list[i-1][1], paint_cost_list[i-1][2]) + paint_cost_list[i][0]
    paint_cost_list[i][1] = min(paint_cost_list[i-1][0], paint_cost_list[i-1][2]) + paint_cost_list[i][1]
    paint_cost_list[i][2] = min(paint_cost_list[i-1][0], paint_cost_list[i-1][1]) + paint_cost_list[i][2]
    
print(min(paint_cost_list[N][0], paint_cost_list[N][1], paint_cost_list[N][2]))
