import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
   # print('x', v)
    queue = deque()
    queue.append(v)
    visited[v] = 1 

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # print(i)
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


        


    

n, m, k, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[0] = 1
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
# print(graph)
bfs(v)
# print(visited)
check = False
for i in range(1, n + 1):
    if visited[i] == k + 1:
        print(i)
        check = True
if check == False:
    print(-1)