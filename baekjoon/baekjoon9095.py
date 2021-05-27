import itertools

T = int(input())
for _ in range(T):
    N = int(input())
    a = [1,2,3]
    case_list = []
    for i in range(1,N+1):
        case_list += [combi for combi in itertools.product(a, repeat=i) if sum(combi) == N]

    print(len(case_list))
