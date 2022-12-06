import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    united = []
    united.append((x, y))
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    total = graph[x][y]
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= n:
                continue
            if visited[x][y] == 0:
                if r <= abs(graph[x][y] - graph[nx][ny]) <= l:
                    visited[nx][ny] = 1
                    united.append((nx, ny))
                    queue.append((nx, ny))
                    count += 1
                    total += graph[x][y]
    total = total // count
    for x, y in united:
        graph[x][y] = total
n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
total = 0
while True:
    count = 0
    visited = [[0] * n for _ in range(2)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)
                count += 1
    
    if count == n * n: # 모든 인구이동 즉 모든 나라를 방문했으면 종료
        break
    total += 1
print(total)