n = int(input())
tri = [[0]]

for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, len(tri)):
    for j in range(i):
        if j == 0:
            tri[i][j] = tri[i-1][j] + tri[i][j]
            
        elif j == (i-1):
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
            
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
            
print(max(tri[n]))
