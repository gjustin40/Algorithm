N, M = map(int, input().split())
rectangle_list = []
for _ in range(N):
    rectangle_list.append(input())

answer_line = ['BWBWBWBW', 'WBWBWBWB']
count_sum_list = []
for i in range(M-7): # 가로의 시작index
    
    for j in range(N-7): # 세로의 시작index
        count1_sum = 0
        count2_sum = 0
        
        for k, line in enumerate(rectangle_list[j:j+8]): # 세로 8개
            rectangle_for_line = line[i:i+8] # 가로 8개
            
            if k%2 == 0:
                count1 = sum([a != b for a,b in zip(rectangle_for_line, answer_line[0])]) # 첫 줄 시작이 2가지 경우가 있으니
                count2 = sum([a != b for a,b in zip(rectangle_for_line, answer_line[1])]) # 2가지 경우 다 계산해줌
            else:
                count1 = sum([a != b for a,b in zip(rectangle_for_line, answer_line[1])])
                count2 = sum([a != b for a,b in zip(rectangle_for_line, answer_line[0])])
                
            count1_sum += count1
            count2_sum += count2
        count_sum_list.append(min(count1_sum, count2_sum))
        
print(min(count_sum_list))
