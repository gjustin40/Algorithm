N = int(input())

body_list = []
for _ in range(N):
    kg, cm = map(int, input().split())
    body_list.append((kg, cm))
    
for i in range(N):
    k1, c1 = body_list[i]
    rank = 1
    for j in range(N):
        if i == j:
            continue
        k2, c2 = body_list[j]
        
        if ((k1 < k2) and (c1 < c2)):
            rank += 1
            
    print(rank, end = ' ')
