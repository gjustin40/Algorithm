string = input().strip()
if len(string) == 0:
    print(0)
else:
    word_list = string.split(' ')
    print(len(word_list))
