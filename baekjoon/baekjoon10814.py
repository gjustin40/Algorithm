import sys

N = int(sys.stdin.readline())
name_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    name_list.append([i, age, name])

name_sorted = sorted(name_list, key=lambda x: (x[1], x[0]))
for name in name_sorted:
    print(name[1], name[2])
