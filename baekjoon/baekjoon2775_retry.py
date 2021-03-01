
t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f0 = [i for i in range(1, num+1)] # 0층 인원

    for f in range(floor):
        for n in range(1, num):
            f0[n] += f0[n-1]
            
    print(f0[-1])
    
## 진짜 사람들은 천재인 것 같다....
## 어떻게 이런 생각을 했을까....
