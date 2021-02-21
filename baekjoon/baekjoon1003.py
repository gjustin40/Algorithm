t = int(input())
n_list = list()

for _ in range(t):
    n_list.append(int(input()))

for n in n_list:
    zero_count = 1
    one_count = 0

    for _ in range(n):
        zero_count, one_count = one_count, zero_count
        one_count = zero_count + one_count
        
    print(zero_count, one_count)
