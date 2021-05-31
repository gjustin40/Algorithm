N = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

dp[1] = 1
for i in range(2, N+1):
    temp = 0
    result = 0
    for j in range(1, i):
        if nums[j] < nums[i]:
            result = max(result, dp[j])
            
    dp[i] = result + 1

print(max(dp))
