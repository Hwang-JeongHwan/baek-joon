dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, s):
    global result
    if len(s) == 7:
        if s not in data:
            data.append(s)
            result += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue

        dfs(nx, ny, s + str(graph[nx][ny]))






tc = int(input())
for t in range(1, tc + 1):
    graph = []
    for _ in range(4):
        data = list(map(int, input().split()))
        graph.append(data)
    data = []
    result = 0
    # print(graph)
    for i in range(4):
        for j in range(4):
            s = str(graph[i][j])
            dfs(i, j, s)
    print('#{} {}'.format(t, result))