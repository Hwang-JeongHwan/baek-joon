# 노드와 간선이 아닌
# 보드형식 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
import heapq
def dfs(dist, x, y):
    q = []
    heapq.heappush(q, (dist, x, y))
    distance[x][y] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난 경우 continue
            if nx < 0 or ny < 0 or nx >= n or ny >= n:

                continue
            # 현재 = 지금까지 온 거리 + 다음 갈곳
            temp = dist + graph[nx][ny]
            # distance 배열에 저장된 좌표의 값이 현재 값보다 크면
            # 갱신하고 heapq에 넣어줌
            if distance[nx][ny] > temp:
                distance[nx][ny] = temp
                print(nx, ny, temp)
                heapq.heappush(q, (temp, nx, ny))


tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = []
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    for _ in range(n):
        graph.append(list(input()))

    for i in range(n):
        for j in range(n):
            graph[i][j] = int(graph[i][j])
    result = []
    dfs(0, 0, 0)
    print('#{} {}'.format(t, distance[-1][-1]))
    # print(graph)

