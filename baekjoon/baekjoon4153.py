while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    
    dis_list = sorted([a, b, c], reverse=True)
    if dis_list[0]**2 == dis_list[1]**2 + dis_list[2]**2:
        print('right')
    else:
        print('wrong')
