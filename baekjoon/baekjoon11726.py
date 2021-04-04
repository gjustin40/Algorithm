import sys
n = int(input())
case = [0] * 1001
case[0] = 0
case[1] = 1
case[2] = 2

for i in range(3, n+1):
    case[i] = case[i-1] + case[i-2]
    
print(case[n]%10007)
