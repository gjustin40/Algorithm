N = int(input())
nums = [0] + [int(input())for _ in range(N)]
    
dp = [0] * (N+1)
dp[1] = nums[1]
if N > 1:
    dp[2] = nums[1] + nums[2]

for i in range(3, N+1):
    dp[i] = max(nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2])

print(dp[N])
