alpha_list = sorted(list(set('abcdefghijklmnopqrstuvwxyz')))

input_string = input()
output = list()
for i, alpha in enumerate(alpha_list):
    
    if alpha in input_string:
        output.append(input_string.index(alpha))
    else:
        output.append(-1)
        
for a in output:
    print(a, end=' ')

##########################
# 진짜 똑똑한 분이네...
# 이렇게 줄일 수 있구나....

for i in range(26):
    print(n.find(chr(ord('a')+i)), end= ' ')
