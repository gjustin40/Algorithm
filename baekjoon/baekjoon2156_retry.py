n = int(input())
glasses = [0]
for _ in range(n):
    glasses.append(int(input()))

dp = [0] * (n+1)
dp[1] = glasses[1]
if n > 1:
    dp[2] = glasses[2] + glasses[1]
for i in range(3, n+1):
    dp[i] = max(glasses[i] + glasses[i-1] + dp[i-3], glasses[i] + dp[i-2])
    dp[i] = max(dp[i], dp[i-1])
    
print(dp[n])
