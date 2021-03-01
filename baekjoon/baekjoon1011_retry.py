for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    distance = y-x

    count = 0
    count_sum = 0

    while True:

        if count_sum >= distance:
            break
        else:
            count += 1
            count_sum += 2*count

    move = distance - (count_sum - 2*count)
    if move <= count:
        print(2*count -1)
    else:
        print(2*count)
        
## 경우의 수 다 나열해서 규칙 찾기...
## 에바참친데...
## 차이(distance) : 1 2 /  3 4 5 6/  7 8 9 10 11 12/  13 14 15 16 17 18 19 20 21/  22 23 24
## 횟수(count)    : 1 2 /  3 3 4 4/  5 5 5 6  6  6/   7  7  7  7  7  8  8  8  8/   9  9   9
