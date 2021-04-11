import sys
N = int(sys.stdin.readline())

dp_list = [0,1,2,3]

for i in range(4, N+1):
    dp_list.append((dp_list[i-1] + dp_list[i-2]) % 15746)
    
print(dp_list[N])

# 예시 몇 개 나열해보면 그냥 피보나치 수열
# 하지만 그냥 append하면 메모리 초과 발생
