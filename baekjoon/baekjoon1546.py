n = int(input())
score_list = list(map(int, list(input().split())))

new_score = [s/max(score_list)*100. for s in score_list]
mean_score = sum(new_score) / n

print(mean_score)
