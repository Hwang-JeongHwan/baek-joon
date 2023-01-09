import sys
input = sys.stdin.readline
from collections import deque
def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    total = 0
    count = 0
    while queue:
        x, y = queue.popleft()
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    queue.append((nx, ny))
                    total += graph[nx][ny]
                    count += 1
                    visited[nx][ny] = 1
    print(total, count)
    return total//count


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
graph = []
visited = [[0] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
check_point = []
