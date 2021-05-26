
N = int(input())
roop_list = [int(input()) for roop in range(N)]
roop_list = sorted(roop_list, reverse=True)

result = 0
for i, roop in enumerate(roop_list):
    if result < (i+1) * roop:
        result = (i+1) * roop
        
print(result)
