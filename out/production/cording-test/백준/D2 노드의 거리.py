# tc = int(input())
# for t in range(1, tc + 1):
#     v, e = map(int, input().split())
#     # graph = [[0] * (v + 1) for _ in range(v + 1)]
#     INF = int(1e9)
#     distance = [[INF] * (v + 1) for _ in range(v + 1)]
#     for a in range(v + 1):
#         for b in range(v + 1):
#             if a == b:
#                 distance[a][b] = 0
#     for _ in range(e):
#         a, b = map(int, input().split())
#         distance[a][b] = 1
#         distance[b][a] = 1
#     # print(graph)
#     for a in range(1, v + 1):
#         for b in range(1, v + 1):
#             for k in range(1, v + 1):
#                 distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
#
#     start, end = map(int, input().split())
#     # print(distance)
#     if distance[start][end] == INF:
#
#         print('#{} {}'.format(t, 0))
#     else:
#
#         print('#{} {}'.format(t, distance[start][end]))
from collections import deque
def bfs(start, count):
    q = deque()
    q.append((start, count))
    visited[start] = 1
    while q:
        now, count = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = count + 1
                q.append((i, count + 1))



tc = int(input())
for t in range(1, tc + 1):
    v, e = map(int, input().split())
    visited = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())
    bfs(start, 0)
    if visited[end] == 0:
        print('#{} {}'.format(t, 0))
    else:
        print('#{} {}'.format(t, visited[end]))