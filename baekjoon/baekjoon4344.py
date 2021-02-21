n = int(input())
for _ in range(n):
    n_list = list(map(int, list(input().split())))
    num = n_list[0]
    score_list = n_list[1:]
    
    mean = sum(score_list) / num
    mean_up_num = sum([int(s>mean) for s in score_list])
    
    student_ratio = mean_up_num/num * 100
    
    print('%0.3f%%' % round(student_ratio, 3))
