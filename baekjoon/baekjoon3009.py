x_list = []
y_list = []
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i,j in zip(set(x_list), set(y_list)):
    if x_list.count(i) == 1:
        x_result = i
    if y_list.count(j) == 1:
        y_result = j
        
print(x_result, y_result)
