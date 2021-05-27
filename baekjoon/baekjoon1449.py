N, L = map(int, input().split())
locations = list(map(int, input().split()))
locations = sorted(locations)

start = locations[0] - 0.5
end = start + L
cnt = 1
for i in range(1, N):
    if (locations[i] >= start) and (locations[i] <= end):
        continue
    start = locations[i] - 0.5
    end = start + L
    cnt += 1
    
print(cnt)
