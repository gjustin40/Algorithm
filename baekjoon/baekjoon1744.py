
N = int(input())
num_plus, num_minu, num_one, num_zero = [], [], [], []
count_plus, count_minu, count_one, count_zero = 0, 0, 0, 0 
for _ in range(N):
    num = int(input())
    if num < 0:
        num_minu.append(num)
        count_minu += 1
    elif num > 1:
        num_plus.append(num)
        count_plus += 1
    elif num == 1:
        num_one.append(num)
        count_one +=1
    else:
        num_zero.append(num)
        count_zero += 1

result = 0
result += sum(num_one)
    
if ((num_plus) and (len(num_plus) % 2 == 0)):
    num_plus = sorted(num_plus, reverse=True)
    for i in range(0, len(num_plus), 2):
        result += num_plus[i] * num_plus[i+1]


elif ((num_plus) and (len(num_plus) % 2 != 0)):
    num_plus = sorted(num_plus, reverse=True)
    for i in range(0, len(num_plus)-1, 2):
        result += num_plus[i] * num_plus[i+1]
    result += num_plus[-1]

if ((num_minu) and (len(num_minu) % 2 == 0)):
    num_minu = sorted(num_minu, reverse=True)
    for i in range(0, len(num_minu), 2):
        result += num_minu[i] * num_minu[i+1]


elif ((num_minu) and (len(num_minu) % 2 != 0)):
    num_minu = sorted(num_minu)
    for i in range(0, len(num_minu)-1, 2):
        result += num_minu[i] * num_minu[i+1]
    
    if count_zero:
        result += num_minu[-1]*0
    else:
        result += num_minu[-1]


print(result)
