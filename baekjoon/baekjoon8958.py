n = int(input())

for _ in range(n):
    quiz = input()
    
    count = 0
    sum_count = 0
    for q in quiz:
        count += 1
        if q=='X':
            count = 0
            
        sum_count += count
        
    print(sum_count)
