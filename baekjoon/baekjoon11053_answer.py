N = int(input())
nums = [0] + list(map(int, input().split()))
dp = [1] * (N+1)

for i in range(2, N+1):
    for j in range(1, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
