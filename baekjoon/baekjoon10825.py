
N = int(input())
grade_list = []
for _ in range(N):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    grade_list.append([name, a, b, c])

grade_list_sorted = sorted(grade_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for grade in grade_list_sorted:
    print(grade[0])
