N = int(input())
nums = {}
for _ in range(N):
    num = int(input())
    
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

nums_sorted = sorted(nums.items(), key=lambda x: (x[1], -x[0]), reverse=True)


print(nums_sorted[0][0])
