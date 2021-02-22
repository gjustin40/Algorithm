string = input().upper()
alpha_list = set(string)

for i, s in enumerate(alpha_list):
    if i == 0:
        first = string.count(s)
        best = first
        best_alpha = s
    else:
        count = string.count(s)
        if best == count:
            best_alpha = '?'
        elif best > count:
            continue
        else:
            best = count
            best_alpha = s
            
print(best_alpha)
