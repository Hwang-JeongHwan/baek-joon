def dfs(x, count):

    global result

    result = max(result, count)
    for i in graph[x]:
        if visited[i] == False:
            visited[i] = True
            dfs(i,count + 1)
            visited[i] = False



tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    result = 1

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n + 1):
        if visited[i] == False:

            dfs(i, 0)

    print('#{} {}'.format(t, result))

