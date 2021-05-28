string = input()
zero = len(list(filter(None, string.split('1'))))
one = len(list(filter(None, string.split('0'))))

print(min(zero, one))
