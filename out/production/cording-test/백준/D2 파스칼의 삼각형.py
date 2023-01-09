tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if j == 1:
                left = 0
            else:
                left = graph[i - 1][j - 1]
            
            if i == j:
                right = 0
            else:
                right = graph[i - 1][j]
            graph[i][j] = (left + right)
    print('#{}'.format(t))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] != 0:
                print(graph[i][j], end=' ')
        print()
