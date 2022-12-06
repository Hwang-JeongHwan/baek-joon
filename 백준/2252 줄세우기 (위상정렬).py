# https://www.acmicpc.net/problem/2252
from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    q = deque()
    result =[]
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    #print(q)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(len(result)):
        print(result[i], end=' ')
n, m  = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()