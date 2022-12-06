# https://www.acmicpc.net/problem/14567
from collections import deque
import sys
input = sys.stdin.readline
def topology_sort():
    q = deque()
    result = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 1))
    
    while q:
        now, count = q.popleft()
        result.append((now, count))
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, count + 1))
    
    result.sort(key = lambda x:x[0])
    
    for i in range(n):
        print(result[i][1], end=' ')
        
n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    

topology_sort()

