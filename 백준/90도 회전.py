# 회전 전의 열번호 = 회전후의 행 번호
# 회전 후의 열 번호 = n - 1 - 회전전의 행번호

# n = 3
# before        after
# (0, 0)        (0, 2) graph[i][j] = graph[j][n - i - 1]
# (0, 1)        (1, 2) graph[i][j] = graph[j][n - i - 1]
# (1, 0)        (0, 1) new[j][n - i - 1] = graph[i][j]


graph = [[1,2,3,4], [6,7,8,9], [10,11,12,13]]

n = len(graph)
m = len(graph[0])

new = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        new[j][n - i - 1] = graph[i][j]

    print(graph, new)