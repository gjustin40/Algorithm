A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

if C <= B:
    x = -1
else:
    x = int(A/(C-B)) + 1
    
print(x)
