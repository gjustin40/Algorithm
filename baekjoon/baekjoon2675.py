t = int(input())
new_list = []
for _ in range(t):
    r, S = input().split()
    r = int(r)
    
    new = str()
    
    for s in S:
        new = new + s*r
    print(new)
