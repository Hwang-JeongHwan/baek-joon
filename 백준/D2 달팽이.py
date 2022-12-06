from collections import deque
tc = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(direction):
    q = deque()
    q.append((1, 1, 1))
    while q:
        x, y, count = q.popleft()
        if count == n * n :
            break
        # print(x, y)
        nx = x + dx[direction % 4]
        ny = y + dy[direction % 4]
        # print(nx, ny)
        if nx < 1 or ny < 1 or nx > n or ny > n or graph[nx][ny] != 0:
            direction += 1
            q.append((x, y, count))
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny, count + 1))


for t in range(1, tc + 1):
    n = int(input())

    graph = [[0] * (n + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    bfs(0)
    # print(graph)
    print('#{}'.format(t))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j],end=' ')
        print()
