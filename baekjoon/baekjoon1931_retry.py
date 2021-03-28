import sys

N = int(input())
time_list = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    time_list.append([a, b])
    
time_list = sorted(time_list, key=lambda x : x[0])
time_list = sorted(time_list, key=lambda x : x[1])

fin = 0
count = 0
for start, end in time_list:
    if start >= fin:
        count += 1
        fin = end
        
print(count)
