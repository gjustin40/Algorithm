n_list = []
for i in range(9):
    n = int(input())
    n_list.append(n)
max_value = max(n_list)
print(max_value)
print(n_list.index(max_value)+1)
