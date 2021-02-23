n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())

count = 0
for word in word_list:
    if len(set(word)) == len(word):
        count += 1
        continue
        
    else:
        is_seq = []
        for alpha in set(word):
            start = word.find(alpha)
            end = word.rfind(alpha)
            is_seq.append((word.count(alpha) == (end-start+1)))
            
        if sum(is_seq) == len(is_seq):
            count += 1
print(count)

# 나의 아이디어
# 단어(word)속에 존재하는 알파벳(alpha)을 확인할 때
# 알파벳이 연속적이라면 처음(find)과 마지막(rfind)의 index의 (차이-1)은 곧 갯수와 같을 것이다.
# 하지만 연속적이지 않으면 같이 않다.
