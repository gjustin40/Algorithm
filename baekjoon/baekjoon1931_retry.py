import sys

N = int(input())
time_list = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split()) # 그냥 input()보다 sys.stdin.readline()으로 하니까 매우 빠름
    time_list.append([a, b])                      # 추가로 jupyter notebook에서는 sys가 잘 작동하지 않음......
    
time_list = sorted(time_list, key=lambda x : x[0])
time_list = sorted(time_list, key=lambda x : x[1])

fin = 0
count = 0
for start, end in time_list:
    if start >= fin:
        count += 1
        fin = end
        
print(count)
