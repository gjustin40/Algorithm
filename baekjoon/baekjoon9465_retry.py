N = int(input())
for _ in range(N):
    n = int(input())
    nnn = []
    for _ in range(2):
        nnn.append(list(map(int, input().split())))
    
    nnn[0][1] += nnn[1][0]
    nnn[1][1] += nnn[0][0]

    for i in range(2, n):
        nnn[0][i] += max(nnn[1][i-1], nnn[1][i-2])
        nnn[1][i] += max(nnn[0][i-1], nnn[0][i-2]) 

    print(max(nnn[0][n-1], nnn[1][n-1]))
