import sys

nums = [0] * 10001
for _ in range(int(sys.stdin.readline())):
     nums[int(sys.stdin.readline())] += 1
        

for i in range(len(nums)):
    if nums[i]:
        for j in range(nums[i]):
            print(i)
