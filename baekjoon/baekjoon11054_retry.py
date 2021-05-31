N = int(input())
nums = list(map(int, input().split()))

nums_reverse = list(reversed(nums))

dp_up = [1] * N
dp_down = [1] * N

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)
        if nums_reverse[j] < nums_reverse[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

result = [x+y for x,y in zip(dp_up, list(reversed(dp_down)))]
print(max(result)-1)
