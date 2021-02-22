def convert(x):
    new = ''
    for i in reversed(x):
        new += i
        
    return int(new)

A, B = input().split()
new = [convert(x) for x in [A,B]]
print(max(new))

#######################################################
# 또 다른 방법(slicing 이용)

A, B = input().split()
newA = int(A[::-1])
newB = int(B[::-1])
print(newA if newA>newB else newB)
