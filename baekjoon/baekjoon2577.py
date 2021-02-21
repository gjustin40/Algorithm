multi = 1
for _ in range(3):
    
    multi = multi * int(input())

count_num = [0 for _ in range(10)]
for n in str(multi):
    count_num[int(n)] += 1
    
for i in count_num:
    print(i)
