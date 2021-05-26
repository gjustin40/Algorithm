case_list = []
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    case_list.append([L, P, V])

for i, case in enumerate(case_list):
    l, p, v = case
    result = 0

    result += (v // p) * l
    res = v % p
    if res <= l:
        result += res
    else:
        result += l
        
    print('Case {}:'.format(i+1), result)
