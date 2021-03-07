N = 8

pivot1 = ('WB' * 4 + 'BW' * 4) * 4
pivot2 = ('BW' * 4 + 'WB' * 4) * 4

h, w = map(int, input().split())
graph = [input() for _ in range(h)]

rst = float('inf')

for i in range(h - N + 1):
    for j in range(w - N + 1):
    from_graph_to_line = ''.join([row[j : j + N] for row in graph[i : i + N]])
    cnt1 = sum(x != y for x, y in zip(pivot1, from_graph_to_line))
    cnt2 = sum(x != y for x, y in zip(pivot2, from_graph_to_line))

    rst = min(rst, cnt1, cnt2)

print(rst)
