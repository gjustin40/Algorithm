x, y, w, h = map(int, input().split())
dif_list = [x, y, w-x, h-y]
print(min(dif_list))
