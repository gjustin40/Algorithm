n, x = input().split()
n_list = list(input().split())

n, x = int(n), int(x)
n_list = list(map(int, n_list))

output = ''
for n in n_list:
    if n < x:
        output = output + ' {}'.format(n)
        
print(output.strip())
