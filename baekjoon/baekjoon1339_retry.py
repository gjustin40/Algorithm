N = int(input())
words, alpha_to_num = [], {}
for _ in range(N):
    word = input()
    words.append(word)
    for w in word:
        alpha_to_num[w] = 0

for word in words:
    for i in range(len(word)):
        num = 10**(len(word) - i - 1)
        alpha_to_num[word[i]] += num

num_list = alpha_to_num.values()
num_list = sorted(num_list, reverse=True)

result = 0
for i in range(len(num_list)):
    result += (num_list[i]*(9-i))
result
