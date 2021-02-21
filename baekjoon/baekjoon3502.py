div_list = []
for _ in range(10):
    n = int(input())
    div = n%42
    div_list.append(div)
    
print(len(set(div_list)))
