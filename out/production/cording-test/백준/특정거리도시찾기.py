
import sys
input = sys.stdin.readline
from collections import deque
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        now = q.popleft()
        #print(now)
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

flag = False


bfs(x)
#print(visited)
for i in range(1, n + 1):
    if visited[i] == k + 1:
        flag = True
        print(i)

if flag == False:
    print(-1)