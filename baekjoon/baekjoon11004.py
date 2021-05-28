import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums_sorted = sorted(nums)
print(nums_sorted[K-1])
