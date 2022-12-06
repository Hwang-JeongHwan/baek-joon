tc = int(input())
for t in range(1, tc + 1):
    n, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    total = 0
    # for i in range(n):
    #     x = 0
    #     y = 0
    #     for j in range(n):
    #         if graph[i][j] == 1:
    #             x += 1
    #         if graph[j][i] == 1:
    #             y += 1
        
    #     if x == k:
    #         total += 1

    #     if y == k:
    #         total += 1
    for i in range(n):
        x = 0
        for j in range(n):
            if graph[i][j] == 1:
                x += 1
                if x == k:
                    if j + 1 < n and graph[i][j + 1] == 0:
                        total += 1
                        x = 0
                    if j == n - 1:
                        total += 1
            else:
                x = 0
    # print('total',total)
    for i in range(n):
        y = 0
        for j in range(n):
            if graph[j][i] == 1:
                y += 1
                if y == k:
                    if j + 1 < n and graph[j + 1][i] == 0:
                        total += 1
                        y = 0
                    if j == n - 1:
                        total += 1
            else:
                y = 0


    print('#{} {}'.format(t, total))