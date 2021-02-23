alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha_time_dict = {}
time = 3

for i, alpha in enumerate(alpha_list):
    for a in alpha:
        alpha_time_dict[a] = time        
    time += 1
    
dial = input()
time_sum = 0
for alpha in dial:
    time = alpha_time_dict[alpha]
    time_sum += time
    
print(time_sum)
###############################################################################################
alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

dial = input()

time = 0
for i in dial:
    for j in alpha_list:
        if i in j:
            time += alpha_list.index(j) + 3
            
print(time)
