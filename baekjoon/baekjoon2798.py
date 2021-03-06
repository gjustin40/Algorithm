N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
nums_sum_list = []
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            nums_sum = nums[a] + nums[b] + nums[c]
            if nums_sum <= M:
                nums_sum_list.append(nums_sum)

print(max(nums_sum_list))

## 브루트 포스는 '모든 경우의 수를 맹목적으로 찾는 방법'이라고 한다....
## 그래서 진짜 다 찾음 ^^
## 밑에 list로 안 만들고 바로 값으로 찾는 방법도 있음

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
result = 0
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            nums_sum = nums[a] + nums[b] + nums[c]
            if nums_sum <= M:
                result = max(result, nums_sum)
            
print(result)
