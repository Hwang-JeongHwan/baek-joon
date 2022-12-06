from collections import deque
def bfs(a, count):
    q = deque()
    q.append((a, count))
    visited[a] = 1
    while q:
        now, count = q.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = count + 1
                q.append((i, count + 1))



n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


bfs(a, 0)

print(visited[b])