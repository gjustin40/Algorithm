def make_non_self_num(x):
    sum_str = 0
    for s in str(x):
        sum_str += int(s)
        
    non_self_num = x + sum_str
    
    return non_self_num

non_self_num_list = list()
num_set = set(range(1,10001))

for n in range(1, 10001):
    non_self_num = make_non_self_num(n)
    non_self_num_list.append(non_self_num)
    
self_num_list = num_set - set(non_self_num_list)
for i in sorted(self_num_list):
    print(i)
