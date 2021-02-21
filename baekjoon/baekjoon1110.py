first = x
count = 0
while True:
    a = x % 10 # 1의 자리
    b = x // 10 # 10의 자리
    new = a+b
    
    final = str(a)+str(new%10)
    count += 1
    if int(final) == first:
        break
    else:
        x = int(final)
print(count)
