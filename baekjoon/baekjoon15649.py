n, m = map(int, input().split())

number_list = [1 + i for i in range(n)]   # 숫자 리스트
check_number = [False] * n                # 중복숫자 체크
array = []

for i in range(n):
    if check_number[i]:
        continue
        
    array.append(number_list[i])
    check_number[i] = True
    
    if m == len(array):
        print(a, b)